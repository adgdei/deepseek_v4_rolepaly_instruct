# 🎉 Roleplay Feedback Post Lottery Record · Round 2 (2026.05.28)

## Background

The comment section of the Xiaohongshu "DeepSeek-V4 Roleplay Feedback Survey Post" (note_id: `6a0ac4ce000000003601e8f6`) collected user feedback. After the first round drew 1 lucky participant to receive a sticker, an additional 20 sticker slots were obtained, so 20 more candidates are drawn using the same probability formula.

---

## Lottery Rules

### Eligibility

- Source: all commenters in the post's comment section (including sub-replies)
- Valid comment: content length ≥ 5 characters (pure emoji / invalid content excluded)
- User uniqueness: distinguished by Xiaohongshu `user_id` (identical nicknames such as "momo" are Xiaohongshu's default nickname and actually belong to different users; counted independently by user_id)
- Excluded:
  - The post author "Chenxiaoli" (user_id: `639931c70000000026007c49`)
  - The first-round winner "Xingyujian" (user_id: `64a136a8000000001f005dd1`)

### Weight Formula (same as Round 1)

```
weight = sqrt(total comment characters) × log₂(number of comments + 1)
```

| Factor | Method | Reason |
|------|---------|------|
| Total comment characters | Square root `sqrt()` | Encourages detailed feedback while preventing overly long comments from gaining an excessive advantage |
| Number of comments | Logarithm `log₂(n+1)` | Encourages repeated feedback while preventing volume-spamming from dominating |
| Multiplying the two | Multiplicative combination | Considers both quality (length) and engagement (frequency) |

### Drawing Method

- Weighted random draw without replacement (after each selection the chosen user is removed, and the remaining users are drawn again by weight)
- A total of 20 distinct winners are drawn

---

## Lottery Parameters

| Parameter | Value |
|------|-----|
| Draw time | 2026-05-28 15:26:26 |
| Number of participating users | 512 |
| Total valid comments | 1,213 |
| Random seed string | `deepseek_roleplay_lottery_round2_2026-05-28 15:26:26_xhs_6a0ac4ce000000003601e8f6` |
| SHA-256 hash | `41b25f7d8d41c68818dddad92bf5692288a069938a7ddcd61a871462d8b3e2ad` |
| Seed value (first 16 hex digits) | `4733951151165261448` |
| Random library | Python `random.choices()` with seed, drawn sequentially without replacement |

### Reproducibility

Anyone can verify the lottery result with the following code:
```python
import random, hashlib, math

seed_str = "deepseek_roleplay_lottery_round2_2026-05-28 15:26:26_xhs_6a0ac4ce000000003601e8f6"
seed_hash = hashlib.sha256(seed_str.encode()).hexdigest()
seed_int = int(seed_hash[:16], 16)
random.seed(seed_int)
# Reproduce by using the same user list and weights, repeatedly calling random.choices + removing the winner
```

---

## Lottery Result

### 🏆 Round 2 Winner List (20 people)

| No. | User | user_id | Comments | Total chars | Win probability |
|:----:|------|---------|:------:|:------:|:--------:|
| 1 | Xiangyucangshuqiu | `5f7322da0000000001008908` | 5 | 766 | 0.563% |
| 2 | Niyushenhai | `65228beb000000002a028087` | 10 | 738 | 0.740% |
| 3 | Wangyue🌙cheng | `5bea7cc63718ed0001fa812f` | 1 | 50 | 0.056% |
| 4 | Buchiguxingren | `665db8df000000000d02711e` | 4 | 189 | 0.251% |
| 5 | Sanshengxue | `5da93ca50000000001006097` | 47 | 5,591 | 3.288% |
| 6 | Apollo | `601106ed000000000100a86a` | 1 | 10 | 0.025% |
| 7 | Diedaizhongde Miss Buhuo | `5b2dcb336b58b7158d042133` | 2 | 328 | 0.226% |
| 8 | momo#5f0c | `667d67000000000007005f0c` | 2 | 264 | 0.203% |
| 9 | momo#796f | `5babb8435eceda00016c796f` | 4 | 382 | 0.357% |
| 10 | Liuhuazhaoyan | `660c2fae000000000600c201` | 8 | 1,976 | 1.110% |
| 11 | Jingshengjianjiao | `68a9b291000000001901242d` | 4 | 181 | 0.246% |
| 12 | Qunianjinrcimenzhong, Renmiantaohuaxiangyinghong | `678652cb000000000801ce04` | 1 | 92 | 0.076% |
| 13 | Yibaoweishengzhi💗 | `68fd8d4500000000370059bb` | 4 | 509 | 0.412% |
| 14 | Weirenshengqidao | `6534b2c7000000000301fe74` | 13 | 2,372 | 1.460% |
| 15 | Xianhuadashi | `5c3821d3000000000703e9a3` | 6 | 362 | 0.421% |
| 16 | Shenyeyanyu | `626ba5ef0000000021027151` | 4 | 570 | 0.437% |
| 17 | Ani | `65e878b40000000005009693` | 5 | 518 | 0.463% |
| 18 | momo#04fd | `6571c2df00000000190104fd` | 39 | 4,511 | 2.815% |
| 19 | Xiaohongshu6921FE40 | `69214b1e000000003700ae25` | 3 | 740 | 0.428% |
| 20 | Baiqiang | `64b5fe8a000000002a037fc2` | 20 | 1,467 | 1.325% |

---

## Probability Distribution Notes

- The winner with the highest probability is "Sanshengxue" (3.288%), with 47 comments totaling 5,591 characters, the most active contributor
- The winner with the lowest probability is "Apollo" (0.025%), with only 1 comment of 10 characters, demonstrating the randomness of the lottery
- The probabilities of the 20 winners range from 0.025% to 3.288%, covering both highly active and low-activity users
- The first-round winner "Xingyujian" was excluded to ensure prizes are distributed to more different users

---

## Weight Ranking Top 20 (all participants)

> Note: the nickname "momo" is Xiaohongshu's default nickname and actually belongs to different users, distinguished by `#last 4 of user_id`.

| Rank | User | user_id | Comments | Total chars | Probability |
|:----:|------|---------|:------:|:------:|:----:|
| 1 | Sanshengxue | `5da93ca50000000001006097` | 47 | 5,591 | 3.288% |
| 2 | momo#04fd | `6571c2df00000000190104fd` | 39 | 4,511 | 2.815% |
| 3 | Yangren.YRWAN | `629d930d00000000150193b4` | 25 | 4,192 | 2.396% |
| 4 | 1900 | `5af0493111be107f87f054dd` | 15 | 2,715 | 1.641% |
| 5 | Shilüru lvru | `680c3c42000000000e01fc28` | 17 | 2,368 | 1.598% |
| 6 | Weirenshengqidao | `6534b2c7000000000301fe74` | 13 | 2,372 | 1.460% |
| 7 | Shenbai | `65efc57c000000000500bf67` | 14 | 2,150 | 1.426% |
| 8 | momo#8793 | `63ff30430000000010028793` | 12 | 2,299 | 1.397% |
| 9 | Baiqiang | `64b5fe8a000000002a037fc2` | 20 | 1,467 | 1.325% |
| 10 | Qiufeng | `655ed4790000000002028dcc` | 16 | 1,499 | 1.246% |
| 11 | Naladejingyu | `69abed530000000033027134` | 12 | 1,818 | 1.242% |
| 12 | Qianlijing | `69eb64ea0000000001007801` | 10 | 1,827 | 1.164% |
| 13 | Shenlanji | `58135c5782ec393140114822` | 11 | 1,603 | 1.130% |
| 14 | Liuhuazhaoyan | `660c2fae000000000600c201` | 8 | 1,976 | 1.110% |
| 15 | Liushuang | `65b1e9ef000000000e003ef9` | 9 | 1,452 | 0.997% |
| 16 | Luoshuiqiaobianchunrixie, Biliuqingqianjianqiongsha | `5fd2be6c000000000101edfb` | 13 | 1,044 | 0.969% |
| 17 | 👀 | `6263f64e000000001000e672` | 8 | 1,429 | 0.944% |
| 18 | Huguangsheng | `68d2712a000000002102ff5e` | 11 | 1,105 | 0.938% |
| 19 | Xixuegexia | `62f19802000000001f017373` | 8 | 1,284 | 0.894% |
| 20 | Shenxiantaitaifanwokuangchi | `660f86f9000000000b00ea0a` | 8 | 1,030 | 0.801% |

---

*The lottery program code is in `lottery_0528.py`; it can be re-run to verify result consistency*
