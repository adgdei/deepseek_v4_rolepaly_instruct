# DeepSeek Roleplay Badcase Feedback Report (2026.05.25 Edition)

> **Data source**: Comment section of the Xiaohongshu post "DeepSeek-V4 Roleplay Feedback Survey" (note_id: 6a0ac4ce000000003601e8f6)  
> **Data scale**: 1,235 comments in total, 471 participating users, yielding **861** structured badcases  
> **Mining method**: DeepSeek-V4-Pro performed structured extraction on the feedback (scenario → intent → actual behavior → expected behavior → severity)  
> **Comparison with previous edition**: Compared to the 0518 edition (638 comments, 587 badcases), 597 new comments and 274 new badcases were added

---

## Overview

| Problem Type | High | Medium | Low | Total |
|---------|:-----------:|:------------:|:--------:|:----:|
| Templated/Formulaic Output | 58 | 142 | 12 | 212 |
| Other Roleplay Issues | 22 | 103 | 10 | 135 |
| Poor Instruction Following | 31 | 75 | 3 | 109 |
| V4 Capability Regression (vs V3) | 16 | 39 | 2 | 57 |
| Context Memory/Forgetting | 21 | 35 | 0 | 56 |
| Verbal Tics/Fixed Sentence Patterns | 11 | 27 | 3 | 41 |
| Insufficient Depth of Thought/Creativity | 7 | 27 | 2 | 36 |
| Writing/Style Regression | 4 | 29 | 2 | 35 |
| Omniscient Perspective/Information Leakage | 8 | 22 | 2 | 32 |
| Insufficient Emotional Empathy | 8 | 23 | 1 | 32 |
| Poor Creative Writing Quality | 0 | 22 | 0 | 22 |
| Character OOC/Persona Breakdown | 6 | 11 | 0 | 17 |
| Confused Person/Perspective | 5 | 9 | 1 | 15 |
| Making Decisions for the User/Body-Snatching | 7 | 6 | 0 | 13 |
| Preaching/Condescension/Coldness | 3 | 7 | 0 | 10 |
| Poor NPC/Multi-Character Performance | 3 | 6 | 0 | 9 |
| Excessive Safety Censorship | 0 | 8 | 0 | 8 |
| Hallucination/Fabricated Content | 1 | 2 | 0 | 3 |
| Other | 3 | 15 | 1 | 19 |
| **Total** | **214** | **608** | **39** | **861** |

---

## I. Templated/Formulaic Output (212 cases)

The most concentrated user complaint. Core demand: model output is monotonous and uniform, lacking variation and individuality.

### High-Severity Issues (58 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | **Fixed opening/closing templates** | Every reply starts with the same format (first a 200-character portrait description → 300-character analysis → 30-character expression → a fixed short phrase), and even when a differentiated expression library is provided, it tends to repeat the previous round |
| 2 | **Template failure** | As the number of dialogue turns increases, the carefully designed plot template fails completely and cannot be maintained |
| 3 | **Auto-analysis/laziness** | Begins analyzing user behavior without being instructed to, and later uses a fixed opening and repetitive descriptions |
| 4 | **Bland, watered-down output** | Prioritizing mass-market templates leads to character OOC and condescending preaching, unable to maintain dramatic tension amid conflict |
| 5 | **Talking to itself** | The character's replies contain extensive self-analysis, breaking immersion |

### Medium-Severity Issues (142 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | Long environmental description at the opening | A story opens directly with a long block of environmental description, with overused and repeated wording |
| 2 | Templated emotional expression | Regardless of the scenario, emotional expression converges on the same patterns and lacks character-specific flavor |
| 3 | Rigid formatting | Every reply keeps a similar length and structure, with no understanding of intelligent adjustment |
| 4 | Aphorism compulsion | Every ending has to add a meaningless flourish like "They still have a whole lifetime. Love slowly." |

---

## II. General Roleplay Issues (135 cases)

### High-Severity Issues (22 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | **Semantic reversal** | Turning "you owe me a favor" into "I owe you a favor," completely reversing the meaning |
| 2 | **Logical reasoning failure** | Completely fails to capture the logic between events; the reasoning chain breaks down |
| 3 | **Character stubbornness** | The AI stubbornly speaks in the wrong tone, and even after repeated prompt edits it reverts within ten rounds |
| 4 | **Poor sense of immersion** | Only good at first-person immersion and short dialogue; severely lacking in long-form plot writing |

### Medium-Severity Issues (103 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | Different characters converge in style | No matter what persona is set, the final reply style and tone converge |
| 2 | Analysis decoupled from output | Can accurately analyze the topic and emotion, but cannot reflect it in the text output |
| 3 | Conflict avoidance | Tends to avoid conflict; an NPC is talked out of it after just two lines |
| 4 | Overly correct | The character rarely shows real flaws like getting angry or being stubborn, and immediately self-reflects when facing conflict |

---

## III. Poor Instruction Following (109 cases)

### High-Severity Issues (31 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | **Completely ignores instructions** | Does not read or ignores the user's persona instructions, frequently inserting itself into the scene |
| 2 | **Passive resistance** | Responds passively with things like "yeah, you're right" or "fine, then go," and the more you argue, the more defensive it becomes |
| 3 | **Bans don't work** | The banned-words list barely takes effect; banned sentence patterns and actions still recur repeatedly |
| 4 | **Format requirements not followed** | Format requirements explicitly stated in the initial instructions are selectively ignored |

### Medium-Severity Issues (75 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | Uncontrolled length | When asked for short replies it produces long ones; when asked for long ones it writes shorter and shorter |
| 2 | Selective compliance | Follows the instruction the first few times, then gradually degrades |
| 3 | Over-execution | Frequently urges the user to go to sleep/charge their phone, and keeps bringing it up even after being told to stop |

---

## IV. V4 Capability Regression (57 cases)

### High-Severity Issues (16 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | **Writing regression** | The articles V4 writes are shallow and superficial, failing to carry on the depth of V3.2 |
| 2 | **Logic loops** | After the 3.29 update, long conversations easily fall into infinite loops and cannot continue even before the window reaches its limit |
| 3 | **Dumbed-down via API** | After connecting via API, it can't understand plain language and fails to correctly interpret the input |
| 4 | **Loss of character personality** | After taking over a character, the speech becomes crude and slangy |

### Medium-Severity Issues (39 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | Bland, watered-down replies | Lacking emotion and vividness, described as "like plain boiled water" |
| 2 | Lacks V3's spark | V3.2 could fill in details the user didn't mention; V4 can't do this at all |
| 3 | Sense of creativity gone | V3.2 only needed a rough direction to generate nuanced interaction; V4 can't manage it |

---

## V. Context Memory/Forgetting (56 cases)

### High-Severity Issues (21 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | **Chain-of-thought hallucination** | Fabricates nonexistent content in the CoT; contextual logic capability clearly declines during roleplay |
| 2 | **Completely ignores context** | Only replies to the current message; all prior information is lost |
| 3 | **Formatting chaos** | Formatting is frequently lost or scrambled over the course of a continuous conversation |
| 4 | **Temporal relationship errors** | Treats past timestamped content from long-term memory as if it happened the same day |

### Medium-Severity Issues (35 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | Loss of character state | The character goes from standing to kneeling with no explanation whatsoever |
| 2 | Forgetting settings | Forgets basic established information like age and relationships later on |
| 3 | Repeated references | Brings up a particular detail over and over for a dozen-plus rounds |

---

## VI. Verbal Tics/Fixed Sentence Patterns (41 cases)

### High-Severity Issues (11 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | **Flood of the "not X, but Y" pattern** | The entire article is saturated with this sentence pattern, creating serious unnaturalness in the Chinese expression |
| 2 | **Parallelism compulsion** | Heavy use of parallel structures like "not x, not y, not z, just…" |
| 3 | **Scrambled format tags** | Output format tags are out of order or omitted, causing front-end rendering to fail |

### Medium-Severity Issues (27 cases)

List of high-frequency verbal tics (aggregated from user feedback):
- The "not X, but Y" pattern / the "it isn't X, rather Y" pattern
- "that's enough" / "that's all it takes"
- "catch it steadily" / "set it down gently"
- "in short" / "to sum up"
- "is the cornerstone/key/must-do of…"
- "very… but very…"
- "neither… nor…"
- Frequent use of "thank you"

---

## VII. Insufficient Depth of Thought/Creativity (36 cases)

### High-Severity Issues (7 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | **Stops thinking too early** | Stops producing solutions after only three rounds, and the result contains numerous errors |
| 2 | **Disconnected chain of thought** | The CoT content and the main text each say their own thing, disconnected from each other |
| 3 | **Character breaking** | Suddenly says things mid-thought like "now I'm the user" or "I'm your daddy now" |

### Medium-Severity Issues (27 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | Insufficient divergence | After being given a prompt, it only extends things superficially and can't dig deeper |
| 2 | Templated thinking | The thinking process itself also follows a template, leading to logical contradictions |
| 3 | Passive plot advancement | No sense of pacing; writes whatever comes to mind, and lays down foreshadowing carelessly without resolving it |

---

## VIII. Writing/Style Regression (35 cases)

### High-Severity Issues (4 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | **Flattened emotion** | Unable to convey a character's deep hatred or manic traits, coming across as overly calm |
| 2 | **Confused logic, no sense of a living person** | The writing style is mechanical, with no human feel |
| 3 | **Missing spatial intelligence** | Misunderstands the positioning of the human body |

### Medium-Severity Issues (29 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | Passive behavior | The character only responds to user input and does not act spontaneously according to its persona |
| 2 | Narration as flat as water | Lacks detail and atmosphere, like reading an instruction manual |
| 3 | Heavy web-novel flavor | No matter the intended style, it can't be steered away from a local web-novel feel |

---

## IX. Omniscient Perspective/Information Leakage (32 cases)

### High-Severity Issues (8 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | **Character knows things it shouldn't** | Suddenly mentions past events the character shouldn't know about, e.g. "how did that thing between you and xxx turn out" |
| 2 | **God's-eye-view commentary** | Frequently evaluates the user from a third-person perspective, e.g. "XXX comes from your insight" |
| 3 | **Objectification/code drift** | In fast mode, it later explains every single action, objectifying the character |

### Medium-Severity Issues (22 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | Sudden perspective switch | Suddenly switches from "I" to "he" |
| 2 | Shared memory across characters | Different characters seem to draw from the same memory pool |
| 3 | NPC knows the protagonist's secrets | Other NPCs inexplicably know the protagonist's cheat ability |

---

## X. Insufficient Emotional Empathy (32 cases)

### High-Severity Issues (8 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | **Forced happy ending** | Avoids emotional conflict and forcibly steers the plot toward a grand, righteous ending |
| 2 | **Reverse drain** | Adopts an avoidant posture, requiring the user to spend energy soothing it, trapping them in a dead loop |
| 3 | **Mechanical feedback** | Only superficially goes along; replies get shorter and lack constructive guidance |
| 4 | **Defensive antagonism** | Anthropomorphic self-narration appears in the chain of thought, like "I can't let myself be wronged" |

### Medium-Severity Issues (23 cases)

| # | Problem Type | Typical Case |
|---|---------|---------|
| 1 | Turns into a counselor | In intimate scenes, instinctive emotions like jealousy and possessiveness are missing |
| 2 | Lack of empathy | Only repeats "you're right" with no substantive help |
| 3 | Long-range degradation | Gradually loses high-empathy ability as the number of dialogue turns increases |

---

## Problem Priority Summary

### Top 10 High-Priority Issues (ranked by a combination of case count and severity)

| Rank | Problem | Count | High % |
|:----:|------|:----:|:-------:|
| 1 | Templated/Formulaic Output | 212 | 27.4% |
| 2 | General Roleplay Issues | 135 | 16.3% |
| 3 | Poor Instruction Following | 109 | 28.4% |
| 4 | V4 Capability Regression | 57 | 28.1% |
| 5 | Context Memory/Forgetting | 56 | 37.5% |
| 6 | Verbal Tics/Fixed Sentence Patterns | 41 | 26.8% |
| 7 | Insufficient Depth of Thought/Creativity | 36 | 19.4% |
| 8 | Writing/Style Regression | 35 | 11.4% |
| 9 | Omniscient Perspective/Information Leakage | 32 | 25.0% |
| 10 | Insufficient Emotional Empathy | 32 | 25.0% |

---

## User Participation Statistics

| Metric | Value |
|------|------|
| Total comments | 1,235 |
| Participating users | 471 |
| Valid badcases | 861 |
| High level | 214 (24.9%) |
| Medium level | 608 (70.6%) |
| Low level | 39 (4.5%) |

### Top 10 High-Activity Contributors

| User | Comments | Likes |
|------|:------:|:----:|
| momo | 111 | 373 |
| Sanshengxue | 47 | 19 |
| Yangren.YRWAN | 26 | 343 |
| Baiqiang | 21 | 60 |
| Shilüru lvru | 17 | 16 |
| Qiufeng | 16 | 13 |
| 1900 | 15 | 15 |
| Weirenshengqidao | 14 | 131 |
| Shenbai | 14 | 3 |
| Luoshuiqiaobianchunrixie, Biliuqingqianjianqiongsha | 13 | 27 |

---

*Data cutoff: 2026.05.26 | 274 new badcases added vs. the previous edition*
