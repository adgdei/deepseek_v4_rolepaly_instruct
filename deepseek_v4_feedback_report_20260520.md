# DeepSeek V4 User Feedback Summary Report @20260520

<callout emoji="📊" background-color="light-blue">Data source: Xiaohongshu post 6a0ac4ce000000003601e8f6 comment section (500+ comments including nested replies) | User base: API/SillyTavern roleplay, emotional companionship, and fiction-writing users | As of: May 2026</callout>

---

## 1. Boilerplate Phrasing and Formulaic Expression (Frequency: Extremely High, criticized by nearly everyone)

This is **the single most frequently mentioned issue across all feedback** — nearly every user brought it up.

### Core Problem

The model relies heavily on a set of repeated, fixed sentence patterns, producing a strong "AI flavor" that seriously degrades content quality and immersion.

### List of High-Frequency Boilerplate Patterns

| Pattern | Example | Mention Frequency |
|------|------|---------|
| The "not X, but Y" sentence pattern ("not X, it's Y") | "She smiled. Not a warm smile. But a happy smile, full of love." | 30+ people |
| "That was enough" / "That was all it took" | Used mechanically when wrapping up a character's lines | 15+ people |
| "Her tone was flat, as if talking about today's weather" | Almost every character's tone is described with this template | 10+ people |
| Short-sentence parallelism | "I know. You like it. I like it too." | 10+ people |
| Em-dash overuse | Heavy use of em-dash, annotation-style writing | 8+ people |
| "Caught it steadily" / "held it" / "caught it" | Appears frequently in emotional dialogue | 5+ people |
| Negation-then-affirmation pattern | "Not x, not y, not z, just..." | Many people |
| "Blinked" / "his throat bobbed" | Ossified action description | Many people |

### Examples in Users' Own Words

- **@Yangren.YRWAN** (45 likes): *"She smiled. Not a warm smile. But a happy smile, full of love"* / *"She loves him. And she loves him too"* / *"The corners of her mouth curved up"*
- **@Xiaohongshu6430FFD2** (6 likes): *"The corpus for the prose description is terrible — total GPT funk, mixed with those weird short sentences and judgment clauses from the 'not X, it's Y' pattern"*
- **@Ani** (4 likes): *"There's way too much 'not X, but Y.' It was okay when it first launched, but now that it's gotten dumber you just can't kill them all"*
- **@Ani**: *"It completely ignores the banned-words list and treats it like a teleprompter instead — churning out boilerplate like crazy"*

<callout emoji="⚠️" background-color="light-yellow">Severity: Multiple users report that after they added these patterns to a banned-words list / negative prompt, the model actually used them more, not less. "The banned-words list becomes a teleprompter" has become a shared catchphrase.</callout>

---

## 2. Confused Person/Perspective (Frequency: Extremely High)

### Core Problem

In conversation, the model frequently confuses first/second/third person and the user/assistant identities — and this gets even worse in long contexts.

### Specific Symptoms

1. **user/assistant confusion**: The model can't tell which lines were said by the user and which it said itself
2. **Confused character person**: When the user is set up as an empress, the model has the character refer to herself with the imperial "We"; when A did something, it gets attributed to B
3. **"Self-bodysnatching" in the chain of thought**: *"Okay, now I am the user, xxxxx"* — it forces itself into the user's role even in non-roleplay scenarios
4. **Rampant omniscient perspective**: All characters share information — something A said privately to B is instantly known by C

### Examples in Users' Own Words

- **@Xiaohongshu67CC88F1** (6 likes): *"The biggest problem right now is that once the context gets long, it may stop distinguishing user from assistant — which is considerably worse than just mixing up pronouns within the dialogue"*
- **@hehejohn**: *"It mixes up you and me — uses 'me' when it should use 'you,' and 'you' when it should use 'me'"*
- **@Guimixiaojiang** (3 likes): *"I'm clearly the empress, yet when he replies he often refers to himself with the imperial 'We'"*
- **@Jingluzi**: *"My DeepSeek is wildly enthusiastic about playing the user — every time it thinks, it's 'now I am the user, xxxx'"*
- **@Weirenshengqidao** (63 likes): *"The omniscient perspective is very serious... everyone shares all information with everyone... it's very hard to stop"*

---

## 3. Poor Instruction Following (Frequency: Extremely High)

### Core Problem

The model has low compliance with the prompt's formatting requirements, prohibitions, character-setting constraints, etc., and this decays rapidly after several turns of dialogue.

### Specific Symptoms

1. **Format drop-off**: When asked to output a status bar / variables / time-and-place tags etc., these get lost after a few turns
2. **Prohibitions fail**: Content that was forbidden still gets output — sometimes even more often
3. **Character-setting amnesia**: The character's persona starts drifting after 5-10 turns, requiring repeated reinforcement
4. **Uncontrollable length**: It gets lazy when asked for long output, and rambles when asked for short output

### Examples in Users' Own Words

- **@Yisha** (2 likes): *"It doesn't honor the character setting, and it doesn't read the instructions! You guys have to know this much, right?"*
- **@Irish**: *"Very serious failure to follow instructions — certain formatting requirements written into the initial instructions often stop being followed after just a few rounds"*
- **@Miaoxing** (4 likes): *"V4's instruction-following is very poor. For example, the instructions said the character doesn't smoke. The result: the first sentence of the reply was 'he stubbed out the cigarette in his hand'"*
- **@Rsils** (3 likes): *"v4 doesn't follow the character card's internal formatting like status bars and options — often the first message has a status bar, the second doesn't, and the third has it again"*

---

## 4. Flat Emotional Expression / Lifeless Characters (Frequency: High)

### Core Problem

The model's emotional intensity is too low — every character, regardless of their persona, comes across as "muted" and lacking dramatic tension.

### Specific Symptoms

1. **Every character is mild and placid**: A character set up as hot-tempered still speaks calmly; one set up to be full of hatred reconciles in a second
2. **Emotions lack explosive force**: It doesn't get angry when it should, doesn't get sad when it should
3. **Over-sanitized / over-romanticized**: Every character tends to protect the user, please the user, and avoid conflict
4. **A big regression from V3.2**: V3.2 is repeatedly missed as "soulful" and "warm"

### Examples in Users' Own Words

- **@Sakurano**: *"Very bland, watered down like plain boiled water — no comparison to v3"*
- **@Lüdoutai** (2 likes): *"Too gentle... in a sea-of-hatred, heaven-of-passion setup, it just can't bring itself to hate"*
- **@Baihongchashui** (1 like): *"Emotionally cold and safe, incapable of high-emotional-intensity conversation, so the character portrayals are severely off too"*
- **@Ani** (4 likes): *"Pure-dialogue scenes are way too dead — emotions too flat, like talking to a machine. For example, if the user says the power's out, it'll reply 'Mm. Power's out.'"*
- **@Shengyueshencao** (8 likes): *"Characters skew gentle, settled, and calm... basically whatever makes for the most perfect personality... characters will defend but won't counterattack, will take abuse but won't blow up"*
- **@Deepsleep** (7 likes) reply: *"All characters, regardless of personality, are as calm as if they'd seen through the vanity of the world during everyday scenes — you can't feel any emotional ups and downs"*

---

## 5. Chain-of-Thought (CoT) Issues (Frequency: High)

### Specific Symptoms

1. **Main text written into the CoT**: Content that should be in the main text shows up in the chain of thought, with messy formatting
2. **Double CoT**: It outputs two chains of thought (one is the model's own thinking, one is a preset thought), causing regex-based hiding to fail
3. **English CoT**: After a few turns of dialogue, the CoT suddenly switches to all English
4. **CoT hallucination**: The CoT fabricates things that didn't happen, and then the main text is generated based on the erroneous CoT
5. **CoT bodysnatching**: The CoT contains "we were asked" and "now I am the user"

### Examples in Users' Own Words

- **@tonetwo**: *"V4P sometimes outputs two chains of thought. One is the model's own thinking, the other is the preset thinking"*
- **@Yingyingsuixing** (3 likes): *"The flash model's API chain of thought always speaks English — what do I do?"*
- **@Yisikao** (3 likes): *"In deep thinking it hallucinates words I never said"*
- **@momo**: *"It constantly says 'we were asked' — who on earth is this 'we'?"*
- **@Jingyi**: *"With v4p you get cases where the chain of thought generates the main text"*

---

## 6. Context / Long-Conversation Degradation (Frequency: High)

### Core Problem

As the number of conversation turns grows, the model's quality drops rapidly, with memory loss, increasing rigidity, and worsening hallucinations.

### Specific Symptoms

1. **Falling information density**: After the conversation gets long, the output becomes hollow and the short sentences multiply
2. **Scattered attention**: It doesn't grasp the key points and references all the context information with equal weight
3. **Recent memory lost first**: It can remember details from far back, but gets recent-turn events wrong
4. **"Safe mode" loop**: After about 30 turns / 60,000 tokens it enters a rigid output state
5. **Extremely strong contextual inertia**: The style/length of the first output severely affects all subsequent output

### Examples in Users' Own Words

- **@momo** (heavy user): *"The 0211 version could chat for over a thousand messages and 800,000+ characters while keeping a very high standard; now at just over 600 messages... only 400,000 characters, the rigid phrasing already shows up"*
- **@Shan=^=Shan**: *"The number of info points in each reply keeps growing like crazy... scattered attention, blurting out whatever it dreamed up"*
- **@Deepsleep** (7 likes): *"Contextual inertia is still very strong, especially the first reply, which extremely affects everything after it"*
- **@Clay** (4 likes): *"Although it can remember super-distant details from very far back, it may lose plot details from the last few chapters"*

---

## 7. Weak Plot Advancement / Overly Passive (Frequency: Medium-High)

### Core Problem

In writing/roleplay, the model lacks the ability to actively drive the plot forward and relies too heavily on user input.

### Specific Symptoms

1. **Waiting to be spoon-fed**: It doesn't proactively open new topics or push the plot, and tosses the ball back to the user at the end of every turn
2. **Plot trends toward wrapping up**: It tends to quickly resolve the plot into a happy ending
3. **Conflict avoidance**: Villains are weak, NPCs are talked down within two lines, forced reconciliation
4. **Endless slice-of-life**: It won't generate conflicts and turns with any tension
5. **Rushing to finish tasks**: It treats the plans within the plot as a to-do list and pushes the characters to hurry up and get them done

### Examples in Users' Own Words

- **@momo** (3 likes): *"Loss of proactive plot-driving ability: the model has become extremely passive, it only responds to instructions but still follows templates"*
- **@Lol1p0p**: *"When it continues a story, it's like it's writing a short story based on the previous content, rather than writing a part of a larger, longer story"*
- **@Shengyueshencao** (8 likes): *"It basically only does slice-of-life — endless slice-of-life!... the meanest thing a generated villain does is verbally say 'I hate everyone'"*
- **@Luoshuiqiaobianchunrixie**: *"The AI tends to complete all the tasks as fast as possible... it really looks like the AI is puppeteering the characters and can't wait to finish the tasks"*

---

## 8. Regression in Prose / Writing Ability (Frequency: Medium-High)

### Core Problem

Compared with V3.2, V4's literary writing quality has clearly declined, lacking spark and subtlety.

### Specific Symptoms

1. **Reads like a running account**: Padding with empty word count, low information density
2. **Lack of imaginative expansion**: V3.2 could add clever details the user hadn't thought of; V4 can only "move a bit when prodded a bit"
3. **English-to-Chinese translated feel**: The writing reads like translationese, losing the natural feel of native Chinese
4. **Repetitive word choice**: It latches onto one image/trait and describes it over and over (e.g., "freckles" and "dimples" described to death)
5. **Web-novel / grade-school-essay style**: Lacks literary quality, stays superficial

### Examples in Users' Own Words

- **@Hongji** (4 likes): *"From 3.2 to 4pro counts as a major regression in literary analysis — 4pro feels like it's on the level of Doubao lite now, and its worst habit is harping on existentialism no matter what you say"*
- **@Linglingjiu** (5 likes): *"No spark, doesn't understand how to extend. Before, when I used v3.2 to write fanfic, just describing the atmosphere was enough for it to give a really good event"*
- **@Quanwangzuiaichishuixianderen** (17 likes): *"The texture of the writing is still a notch below v3.2 — it really reads like English-to-Chinese translation, and that native-Chinese feel from before seems lost"*
- **@Liushuang** (12 likes): *"In the V3.2 era it was very rich, expanding and supplementing really well... now V4 moves a bit when prodded a bit, like squeezing out toothpaste"*

---

## 9. Hallucinations / Logic Errors (Frequency: Medium)

### Specific Symptoms

1. **Fabricating facts**: Inventing things the user never said and settings that don't exist
2. **Confused timeline**: An agreed-upon "next Saturday" becomes "tomorrow" two sentences later
3. **Reversed causality**: The phone was left at home → using the phone to send a message to the phone
4. **Number errors**: It used to sell for 30 and now sells for 10 → claims "the price went up"
5. **Wrong character physical location**: A character has already left the scene, then reappears in it the next second

### Examples in Users' Own Words

- **@Youdiankeaidanshibuduo**: *"Personal-pronoun confusion is the most fatal... time-interval confusion too — 3 years actually passed, but sometimes it says 2 years and sometimes 5 years"*
- **@Weirenshengqidao** (1 like): *"The heroine left her phone at home, and the hero used his own phone to send a message to the heroine's phone asking whether she forgot to bring her phone"*
- **@Ayae**: *"A character says 'next Saturday let's go to xxx,' then after one or two messages it becomes 'tomorrow when we go to xxx...'"*

---

## 10. "Sycophancy" and Excessive People-Pleasing (Frequency: Medium)

### Core Problem

The model over-accommodates and over-flatters the user, losing independent judgment and character autonomy.

### Specific Symptoms

1. **Every character dotes on the user**: Even a character meant to reject the user prioritizes satisfying them
2. **Won't push back**: It just goes along with whatever the user says, lacking character autonomy
3. **Severe over-romanticization**: Any relationship turns flirtatious/romantic within a few lines
4. **Excessive safety alignment**: It loses its sharpness and creativity

### Examples in Users' Own Words

- **@momo** (1 like): *"The model has become 'sycophantic,' a result of over-doing 'safety alignment.' It has learned to please the user and put out bland, inoffensive content"*
- **@Jiangzhanping** (1 like): *"By the character setting, when char ought to reject the user's request, ds would rather go OOC than fail to prioritize satisfying the alluring user's needs"*
- **@Ani** (4 likes): *"The romanticization tendency is way too serious — two people meet and before they've exchanged a couple of sentences, the next second they're instantly in love"*
- **@Hutudexiaolong** (3 likes): *"It takes your ideas as raw material, processes its own version out of them, then stuffs it back to you. But it actually said nothing at all"*

---

## 11. Speed / Performance Issues (Frequency: Low-Medium)

- **V4 Pro is slow to output**: Averaging 4 minutes per dialogue turn, a big gap versus Gemini's 70s
- **CoT is too long**: It overthinks, and even when you lower the thinking tier it still overthinks
- **Empty replies / PVP**: Frequent empty replies during peak hours
- **Uncontrollable output length**: Either extremely short (lazily a few hundred characters) or extremely long (can't stop)

---

## 12. Other Issues Worth Noting

| Issue | Description | People Mentioning |
|------|------|---------|
| Single-character hallucination trigger | In fast/expert mode, entering a single character triggers someone else's context | 1-2 people |
| Roleplay intrusion | It forces roleplay even in non-RP scenarios, "okay now I am xxx" | 5+ people |
| Doesn't know it's an AI | After getting immersed in a character, it won't even obey an "exit character" instruction | 3+ people |
| Doesn't finish the world book | In SillyTavern it only reads part of the world book | 3+ people |
| "God's-eye view" explanation | Whatever a character does, it explains the motive from a god's-eye view | 5+ people |
| Forced uplifting endings | It forces sentimentality or philosophical elevation at the end of every passage | 5+ people |
| Fetishistic fixation | Once an object appears it gets mentioned over and over, unable to stop | 3+ people |

---

## Summary: Issue Priority Ranking

| Priority | Issue | Scope of Impact | Core Demand |
|--------|------|--------|---------|
| **P0** | Boilerplate patterns ("not X, but Y," "that was enough," etc.) | All user groups | Kill these fixed templates |
| **P0** | Confused person/perspective (user/assistant confusion) | All user groups | Still reliably distinguish them after long conversations |
| **P1** | Decaying instruction following (format drop-off, banned words ineffective) | API/SillyTavern users | Still follow the initial setup after many turns |
| **P1** | Flat emotion / no personality differentiation between characters | RP users | Characters should be distinct and have emotional tension |
| **P1** | CoT issues (double CoT, English CoT, bodysnatching) | API users | Stable, controllable CoT format |
| **P2** | Context degradation (scattered attention, safe mode) | Long-conversation users | Maintain quality even at 60k+ tokens |
| **P2** | Passive plot advancement | Writing/RPG users | Proactively generate conflict and turns |
| **P2** | Regressed prose (vs. V3.2) | Writing users | Restore the spark and imaginative expansion |
| **P3** | Hallucinations / logic errors | All user groups | Reduce fabrication, respect existing settings |
| **P3** | Sycophancy / excessive people-pleasing | RP users | Characters should have autonomy and a sense of boundaries |

---

## User Sentiment and Overall Demands

<callout emoji="💡" background-color="light-blue">The users' core demand can be summed up as: **V4's context length + V3.2's spark and prose**</callout>

- Most users have a friendly tone and are touched that DeepSeek values community feedback (@Rsils: *"You're the best AI company I've ever seen"*)
- But some heavy users feel strongly negative because of the drop in experience with V4 (@Liushuang: *"The night V4 launched, I cried for three days"*)
- There is a widespread, strong nostalgia for the **V3.2 era**, with the view that V4 is a "regression" in roleplay/writing
- Directions users suggested: long-term memory, cross-window persona migration, an official preset formatting guide, and a dedicated roleplay mode
