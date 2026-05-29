"""
Role-play feedback thread lottery program (round 2: 20 stickers)
Data source: comment section of Xiaohongshu post 6a0ac4ce000000003601e8f6
Lottery time: 2026-05-28

Rules:
- Same weight formula as round 1: sqrt(total characters) x log2(count+1)
- Exclude the thread owner "Chenxiaoli (pinyin)"
- Exclude the round-1 winner "Xingyujian" (user_id: 64a136a8000000001f005dd1)
- Draw 20 distinct winning users
- Random seed: deterministic seed based on the current time
"""

import json
import math
import random
import hashlib
from collections import defaultdict, Counter

DB_CONFIG = {
    "host": "<DB_HOST>",
    "port": 5432,
    "dbname": "<DB_NAME>",
    "user": "<DB_USER>",
    "password": "<DB_PASSWORD>",
    "connect_timeout": 10,
}

NOTE_ID = "6a0ac4ce000000003601e8f6"
EXCLUDE_USER_IDS = {
    "639931c70000000026007c49",  # thread owner Chenxiaoli (pinyin)
    "64a136a8000000001f005dd1",  # round-1 winner: Xingyujian
}
LOTTERY_TIME = "2026-05-28 15:26:26"
NUM_WINNERS = 20


def extract_comments_from_db():
    """Extract all comments (including sub-comments) from the database, keeping user_id"""
    import psycopg2
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(
        "SELECT raw_json FROM comments WHERE note_id = %s ORDER BY fetched_at DESC, id",
        (NOTE_ID,),
    )
    rows = cur.fetchall()
    conn.close()

    all_comments = []
    seen_ids = set()

    for (raw_json,) in rows:
        raw = json.loads(raw_json) if isinstance(raw_json, str) else raw_json
        comments = raw.get("data", {}).get("comments", [])

        for c in comments:
            cid = c.get("id", "")
            if cid in seen_ids:
                continue
            seen_ids.add(cid)
            user_info = c.get("user_info", {})
            all_comments.append({
                "id": cid,
                "user_id": user_info.get("user_id", ""),
                "nickname": user_info.get("nickname", "unknown"),
                "content": c.get("content", ""),
            })
            for sc in c.get("sub_comments", []):
                scid = sc.get("id", "")
                if scid in seen_ids:
                    continue
                seen_ids.add(scid)
                sc_user = sc.get("user_info", {})
                all_comments.append({
                    "id": scid,
                    "user_id": sc_user.get("user_id", ""),
                    "nickname": sc_user.get("nickname", "unknown"),
                    "content": sc.get("content", ""),
                })

    return all_comments


def aggregate_users(comments):
    """Aggregate comment data by user_id, excluding the thread owner and the round-1 winner"""
    user_data = defaultdict(lambda: {"count": 0, "total_length": 0, "comments": [], "nickname": ""})

    for c in comments:
        uid = c["user_id"]
        content = c["content"].strip()
        if len(content) < 5:
            continue
        if uid in EXCLUDE_USER_IDS:
            continue
        user_data[uid]["count"] += 1
        user_data[uid]["total_length"] += len(content)
        user_data[uid]["comments"].append(content)
        user_data[uid]["nickname"] = c["nickname"]

    return dict(user_data)


def get_display_name(user_data):
    """Build display names: distinguish users with the same nickname using #last 4 digits"""
    nick_count = defaultdict(int)
    for uid, d in user_data.items():
        nick_count[d["nickname"]] += 1

    display_names = {}
    for uid, d in user_data.items():
        if nick_count[d["nickname"]] > 1:
            display_names[uid] = f"{d['nickname']}#{uid[-4:]}"
        else:
            display_names[uid] = d["nickname"]
    return display_names


def calculate_weights(user_data):
    """
    Compute the lottery weights
    Formula: sqrt(total comment characters) x log2(number of comments + 1)
    """
    weights = {}
    for uid, data in user_data.items():
        length_score = math.sqrt(data["total_length"])
        count_score = math.log2(data["count"] + 1)
        weights[uid] = length_score * count_score
    return weights


def generate_seed(lottery_time):
    """Generate a deterministic random seed"""
    seed_str = f"deepseek_roleplay_lottery_round2_{lottery_time}_xhs_{NOTE_ID}"
    seed_hash = hashlib.sha256(seed_str.encode()).hexdigest()
    seed_int = int(seed_hash[:16], 16)
    return seed_str, seed_hash, seed_int


def run_lottery(weights, seed_int, num_winners):
    """Run the weighted random draw, selecting num_winners distinct winners (sampling without replacement)"""
    random.seed(seed_int)
    users_list = sorted(weights.keys())
    weights_list = [weights[u] for u in users_list]

    winners = []
    remaining_users = list(users_list)
    remaining_weights = list(weights_list)

    for _ in range(num_winners):
        if not remaining_users:
            break
        chosen = random.choices(remaining_users, weights=remaining_weights, k=1)[0]
        winners.append(chosen)
        idx = remaining_users.index(chosen)
        remaining_users.pop(idx)
        remaining_weights.pop(idx)

    return winners


def main():
    print("=" * 60)
    print("  DeepSeek Role-play Feedback Thread Round 2 Lottery (20 stickers)")
    print("=" * 60)

    # Step 1: data extraction
    print("\n[1/5] Extracting comment data...")
    try:
        comments = extract_comments_from_db()
        print(f"      (source: direct database connection)")
    except Exception as e:
        print(f"      Database connection failed ({e}), using cache file...")
        with open("roleplay_comments_with_uid.json") as f:
            comments = json.load(f)
        print(f"      (source: cache file)")
    print(f"      {len(comments)} comments total")

    # Step 2: user aggregation
    print("\n[2/5] Aggregating by user_id (excluding thread owner + round-1 winner)...")
    user_data = aggregate_users(comments)
    display_names = get_display_name(user_data)
    print(f"      Eligible participants: {len(user_data)}")
    print(f"      Valid comments: {sum(u['count'] for u in user_data.values())}")
    print(f"      Excluded users: thread owner (Chenxiaoli) + round-1 winner (Xingyujian)")

    nick_counter = Counter(d["nickname"] for d in user_data.values())
    dup_nicks = {k: v for k, v in nick_counter.items() if v > 1}
    if dup_nicks:
        print(f"      Users with duplicate nicknames (distinguished by user_id): {sum(dup_nicks.values())} users across {len(dup_nicks)} nicknames")

    # Step 3: weight calculation
    print("\n[3/5] Computing weights: sqrt(total characters) x log2(count+1)")
    weights = calculate_weights(user_data)
    total_weight = sum(weights.values())

    sorted_users = sorted(weights.items(), key=lambda x: -x[1])
    print(f"\n      Top 20 by weight:")
    print(f"      {'Rank':<4} {'User':<28} {'user_id':<28} {'Comments':<6} {'Chars':<7} {'Prob'}")
    print(f"      {'-' * 85}")
    for i, (uid, w) in enumerate(sorted_users[:20], 1):
        d = user_data[uid]
        name = display_names[uid]
        prob = w / total_weight * 100
        print(f"      {i:<4} {name:<28} {uid:<28} {d['count']:<6} {d['total_length']:<7} {prob:.3f}%")

    # Step 4: generate seed
    print(f"\n[4/5] Generating random seed...")
    seed_str, seed_hash, seed_int = generate_seed(LOTTERY_TIME)
    print(f"      Lottery time: {LOTTERY_TIME}")
    print(f"      Seed string: {seed_str}")
    print(f"      SHA-256: {seed_hash}")
    print(f"      Seed value: {seed_int}")

    # Step 5: draw
    print(f"\n[5/5] Running the draw (selecting {NUM_WINNERS} winners)...")
    winners = run_lottery(weights, seed_int, NUM_WINNERS)

    print(f"\n{'=' * 60}")
    print(f"  🎉 Round 2 winners ({len(winners)} total)")
    print(f"{'=' * 60}")
    print(f"\n  {'No.':<4} {'User':<28} {'user_id':<28} {'Comments':<6} {'Chars':<7} {'Prob'}")
    print(f"  {'-' * 85}")

    for i, uid in enumerate(winners, 1):
        d = user_data[uid]
        name = display_names[uid]
        prob = weights[uid] / total_weight * 100
        print(f"  {i:<4} {name:<28} {uid:<28} {d['count']:<6} {d['total_length']:<7} {prob:.3f}%")

    print(f"\n{'=' * 60}")
    print(f"\n  Lottery parameter summary:")
    print(f"  - Participating users: {len(user_data)}")
    print(f"  - Number of winners: {len(winners)}")
    print(f"  - Random seed time: {LOTTERY_TIME}")
    print(f"  - Seed SHA-256: {seed_hash}")
    print(f"  - Weight formula: sqrt(total characters) x log2(count+1)")
    print(f"  - Excluded: thread owner + round-1 winner")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
