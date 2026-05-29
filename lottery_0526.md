# 🎉 Roleplay Feedback Post Lottery Record (2026.05.26)

## Background

The comment section of the Xiaohongshu "DeepSeek-V4 Roleplay Feedback Survey Post" (note_id: `6a0ac4ce000000003601e8f6`) collected user feedback, with a promise to draw one lucky participant from the users who provided valid feedback and gift them a little-whale sticker.

---

## Lottery Rules

### Eligibility

- Source: all commenters in the post's comment section (including sub-replies)
- Valid comment: content length ≥ 5 characters (pure emoji / invalid content excluded)
- User uniqueness: distinguished by Xiaohongshu `user_id` (identical nicknames such as "momo" are Xiaohongshu's default nickname and actually belong to different users; counted independently by user_id)
- Excluded: the post author "Chenxiaoli" himself (user_id: `639931c70000000026007c49`)

### Weight Formula

```
weight = sqrt(total comment characters) × log₂(number of comments + 1)
```

**Design rationale**:

| Factor | Method | Reason |
|------|---------|------|
| Total comment characters | Square root `sqrt()` | Encourages detailed feedback while preventing overly long comments from gaining an excessive advantage |
| Number of comments | Logarithm `log₂(n+1)` | Encourages repeated feedback while preventing volume-spamming from dominating |
| Multiplying the two | Multiplicative combination | Considers both quality (length) and engagement (frequency) |

This design ensures that:
- A user who writes 1 comment of 500 characters → weight ≈ 22.4
- A user who writes 5 comments totaling 1000 characters → weight ≈ 82.0
- A user who writes 50 comments totaling 5000 characters → weight ≈ 395.4

This rewards deeply engaged participants without letting a single heavy contributor monopolize the chance of winning.

---

## Lottery Parameters

| Parameter | Value |
|------|-----|
| Draw time | 2026-05-26 19:44:20 |
| Number of participating users | 513 |
| Total valid comments | 1,219 |
| Random seed string | `deepseek_roleplay_lottery_2026-05-26 19:44:20_xhs_6a0ac4ce000000003601e8f6` |
| SHA-256 hash | `4ae9fb84ae161aa2ff83ccb784f424783175739ae35d00e6c334c996380fd385` |
| Seed value (first 16 hex digits) | `5398122175655189154` |
| Random library | Python `random.choices()` with seed |

### Reproducibility

Anyone can verify the lottery result with the following code:
```python
import random, hashlib, math

seed_str = "deepseek_roleplay_lottery_2026-05-26 19:44:20_xhs_6a0ac4ce000000003601e8f6"
seed_hash = hashlib.sha256(seed_str.encode()).hexdigest()
seed_int = int(seed_hash[:16], 16)
random.seed(seed_int)
# Reproduce the result using the same user list and weights
```

---

## Lottery Result

### 🏆 Winner: Xingyujian

| Metric | Value |
|------|------|
| user_id | `64a136a8000000001f005dd1` |
| Comments | 6 |
| Total chars | 558 |
| Weight | 66.32 |
| Win probability | 0.519% |

### The Winner's Feedback

**Comment 1**:
> A character that has been set up with a "nonchalant" personality nonetheless tends to use short sentences ending in periods and commanding language, which feels off-putting. Low agreeableness shouldn't be reduced to a formula like that.

**Comment 2**:
> Sometimes I wish the characters were a bit more rebellious, a bit "bad." Right now, when writing ensemble casts, the characters all gradually converge toward the same faint, gentle feel, and their personalities get increasingly reduced to labels.

**Comment 3**:
> It's hard to tell when something should be repeated and when it should be differentiated. For example, format-required content should be repeated exactly, and an action carried over from the previous scene should stay continuous — that's correct; but it keeps repeating some specific action/expression.

**Comment 4**:
> Also, please give DeepSeek the permission to delete text. Every time it does that "not... but rather..." / self-correction thing, it's exhausting to read.

**Comment 5**:
> Another issue is plot progression: on one hand it's not very proactive about moving the plot forward and has no sense of pacing; on the other hand it lacks an overall sense of the story, just writing whatever comes to mind, planting foreshadowing randomly without ever thinking about how to resolve it — for instance, inexplicably placing a creepy door.

This user reported several core problems — converging character personalities, repetitive output, passive plot progression, and more — with high-quality, specific feedback.

---

## Weight Ranking Top 20

> Note: the nickname "momo" is Xiaohongshu's default nickname and actually belongs to different users, distinguished by `#last 4 of user_id`.

| Rank | User | Comments | Total chars | Probability |
|:----:|------|:------:|:------:|:----:|
| 1 | Sanshengxue | 47 | 5,591 | 3.271% |
| 2 | momo#04fd | 39 | 4,511 | 2.800% |
| 3 | Yangren.YRWAN | 25 | 4,192 | 2.384% |
| 4 | 1900 | 15 | 2,715 | 1.633% |
| 5 | Shilüru lvru | 17 | 2,368 | 1.589% |
| 6 | Weirenshengqidao | 13 | 2,372 | 1.453% |
| 7 | Shenbai | 14 | 2,150 | 1.419% |
| 8 | momo#8793 | 12 | 2,299 | 1.390% |
| 9 | Baiqiang | 20 | 1,467 | 1.318% |
| 10 | Qiufeng | 16 | 1,499 | 1.240% |
| 11 | Naladejingyu | 12 | 1,818 | 1.236% |
| 12 | Qianlijing | 10 | 1,827 | 1.158% |
| 13 | Shenlanji | 11 | 1,603 | 1.124% |
| 14 | Liuhuazhaoyan | 8 | 1,976 | 1.104% |
| 15 | Liushuang | 9 | 1,452 | 0.992% |
| 16 | Luoshuiqiaobianchunrixie, Biliuqingqianjianqiongsha | 13 | 1,044 | 0.964% |
| 17 | 👀 | 8 | 1,429 | 0.939% |
| 18 | Huguangsheng | 11 | 1,105 | 0.933% |
| 19 | Xixuegexia | 8 | 1,284 | 0.890% |
| 20 | Shenxiantaitaifanwokuangchi | 8 | 1,030 | 0.797% |

---

## Probability Distribution Notes

- The highest-weighted user, Sanshengxue (3.27%), has 47 comments totaling 5,591 characters and is the most active contributor
- The winner "Xingyujian" (0.519%) won with high-quality feedback of 6 comments totaling 558 characters
- This demonstrates the fairness of weighted lottery: more active users have higher probability, but all participants have a chance

Probability distribution characteristics:
- Top 1 user probability ≈ 3.3% (no monopoly)
- Top 10 users cumulative probability ≈ 20%
- The remaining 503 users share ≈ 80% probability
- Lowest-probability user ≈ 0.02% (1 short comment)

---

*The lottery program code is in `scripts/lottery_0526.py`; it can be re-run to verify result consistency*
