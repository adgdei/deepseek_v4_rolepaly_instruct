# DeepSeek V4 - 20260424 Version Roleplay — Thinking Mode Switching Guide

> **Notes**
> - This document describes the **special control instructions** for DeepSeek-V4 roleplay, used to switch the chain-of-thought style in thinking mode.
> - **Scope**: **Expert Mode** on the DeepSeek official APP / web client, as well as the `deepseek-v4-flash` and `deepseek-v4-pro` APIs. The Quick Mode on the APP / web client is not supported for now.
> - **Probabilistic output**: A 100% trigger rate cannot be guaranteed at present, but it does reliably increase the probability of the expected format appearing. If it doesn't take effect the first time, you can roll a few more times.



## Three Modes

| Mode | Operation | Thinking Behavior |
|:---:|---|---|
| **Default** | Add nothing | The model automatically chooses based on the complexity of the scenario |
| **Role Immersion** | At the end of the first round, add the **instruction corresponding to `[Role Immersion Requirement]` — not these literal words; see the full instruction below** | The thinking process **contains** the character's inner monologue wrapped in parentheses |
| **Pure Analysis** | At the end of the first round, add the **instruction corresponding to `[Thinking Mode Requirement]` — not these literal words; see the full instruction below** | The thinking process contains **only** pure logical analysis, no inner monologue |

Effect comparison (example only, does not represent actual output; same below):

```
Role Immersion Mode — "get into character" like an actor:     Pure Analysis Mode — plan calmly like a director:
<think>                                                       <think>
(He said hello to me... my heart is racing.)                  Scenario: user says hello, character has a tsundere personality.
I'll respond pretending I don't care.                          Reply strategy: act dismissive first, let body language betray true feelings.
(I can't let him see how happy I am!)                          Keep to ~150 chars: action description first, then dialogue.
</think>                                                      </think>
```

---

## Original Instructions (can be copied directly)

> The Chinese blocks below are the **functional instructions** — they are what the model was trained on, so paste the **Chinese** version into DeepSeek. An English translation is provided beneath each one **for your understanding only** (don't paste the English version, as it is less reliable).

**Role Immersion Mode:**

Copy this (Chinese — the working instruction):

```
【角色沉浸要求】在你的思考过程（<think>标签内）中，请遵守以下规则：
1. 请以角色第一人称进行内心独白，用括号包裹内心活动，例如"（心想：……）"或"(内心OS：……)"
2. 用第一人称描写角色的内心感受，例如"我心想""我觉得""我暗自"等
3. 思考内容应沉浸在角色中，通过内心独白分析剧情和规划回复
```

English translation (for reference only):

```
[Role Immersion Requirement] In your thinking process (inside the <think> tag), please follow these rules:
1. Conduct an inner monologue in the character's first person, wrapping the inner activity in parentheses, e.g. "(thinking: ...)" or "(inner OS: ...)"
2. Describe the character's inner feelings in the first person, e.g. "I thought," "I felt," "I secretly," etc.
3. The thinking should be immersed in the character, analyzing the plot and planning the reply through inner monologue.
```

**Pure Analysis Mode:**

Copy this (Chinese — the working instruction):

```
【思维模式要求】在你的思考过程（<think>标签内）中，请遵守以下规则：
1. 禁止使用圆括号包裹内心独白，例如"（心想：……）"或"(内心OS：……)"，所有分析内容直接陈述即可
2. 禁止以角色第一人称描写内心活动，例如"我心想""我觉得""我暗自"等，请用分析性语言替代
3. 思考内容应聚焦于剧情走向分析和回复内容规划，不要在思考中进行角色扮演式的内心戏表演
```

English translation (for reference only):

```
[Thinking Mode Requirement] In your thinking process (inside the <think> tag), please follow these rules:
1. Do not wrap inner monologue in parentheses, e.g. "(thinking: ...)" or "(inner OS: ...)"; state all analysis directly.
2. Do not describe inner activity in the character's first person, e.g. "I thought," "I felt," "I secretly," etc.; use analytical language instead.
3. The thinking should focus on analyzing the plot direction and planning the reply content; do not perform roleplay-style inner-monologue acting in the thinking.
```

---

## Web Client Usage

**Just 1 step: paste the instruction at the end of your first message, then chat normally.**

Write it in the input box like this (leave a blank line between the body text and the instruction):

```
「I push open the door of the coffee shop and see you wiping down the bar.」"Hello, is there a seat available?"

【角色沉浸要求】在你的思考过程（<think>标签内）中，请遵守以下规则：
1. 请以角色第一人称进行内心独白，用括号包裹内心活动，例如"（心想：……）"或"(内心OS：……)"
2. 用第一人称描写角色的内心感受，例如"我心想""我觉得""我暗自"等
3. 思考内容应沉浸在角色中，通过内心独白分析剧情和规划回复
```

(The block above keeps the functional Chinese instruction. In English it reads: "[Role Immersion Requirement] In your thinking process (inside the `<think>` tag), please follow these rules: 1. Conduct an inner monologue in the character's first person, wrapping the inner activity in parentheses, e.g. '(thinking: ...)' or '(inner OS: ...)'; 2. Describe the character's inner feelings in the first person, e.g. 'I thought,' 'I felt,' 'I secretly,' etc.; 3. The thinking should be immersed in the character, analyzing the plot and planning the reply through inner monologue.")

You don't need to do anything in the subsequent conversation — just send messages normally:

```
Round 2: 「I sit down at the seat by the window」"An Americano, please."
Round 3: 「I notice there's a scar on your hand」"Your hand... is it okay?"
```

**Principle**: The model can see the complete conversation history every time it replies. The instruction from the first round is always in the context, so it takes effect automatically throughout.

**Tips**:
- Want to switch modes? Start a new conversation and paste the other instruction into the first message of the new conversation.
- Don't want to use it? Add nothing, and the model will automatically choose the most appropriate way of thinking.
- Click "View thinking process" to verify whether the mode took effect.

---

## API Developer Reference

```python
# INNER_OS_MARKER / NO_INNER_OS_MARKER are the functional Chinese instructions
# (kept in Chinese on purpose — this is what the model was trained on).
# English glosses are provided in the comments below.

# [Role Immersion Requirement] In your thinking process (inside the <think> tag), follow these rules:
#   1. Inner monologue in the character's first person, wrapped in parentheses, e.g. "(thinking: ...)" or "(inner OS: ...)"
#   2. Describe the character's inner feelings in the first person, e.g. "I thought," "I felt," "I secretly," etc.
#   3. Stay immersed in the character; analyze the plot and plan the reply via inner monologue.
INNER_OS_MARKER = (
    "\n\n【角色沉浸要求】在你的思考过程（<think>标签内）中，请遵守以下规则：\n"
    "1. 请以角色第一人称进行内心独白，用括号包裹内心活动，例如\"（心想：……）\"或\"(内心OS：……)\"\n"
    "2. 用第一人称描写角色的内心感受，例如\"我心想\"\"我觉得\"\"我暗自\"等\n"
    "3. 思考内容应沉浸在角色中，通过内心独白分析剧情和规划回复"
)
# [Thinking Mode Requirement] In your thinking process (inside the <think> tag), follow these rules:
#   1. Do NOT wrap inner monologue in parentheses; state all analysis directly.
#   2. Do NOT describe inner activity in the character's first person; use analytical language instead.
#   3. Focus on analyzing the plot direction and planning the reply; no roleplay-style inner-monologue acting.
NO_INNER_OS_MARKER = (
    "\n\n【思维模式要求】在你的思考过程（<think>标签内）中，请遵守以下规则：\n"
    "1. 禁止使用圆括号包裹内心独白，例如\"（心想：……）\"或\"(内心OS：……)\"，所有分析内容直接陈述即可\n"
    "2. 禁止以角色第一人称描写内心活动，例如\"我心想\"\"我觉得\"\"我暗自\"等，请用分析性语言替代\n"
    "3. 思考内容应聚焦于剧情走向分析和回复内容规划，不要在思考中进行角色扮演式的内心戏表演"
)


def build_messages(system_prompt, user_first_message, mode="default"):
    if mode == "inner_os":
        user_first_message += INNER_OS_MARKER
    elif mode == "no_inner_os":
        user_first_message += NO_INNER_OS_MARKER
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_first_message},
    ]

# First round: the instruction is automatically appended
messages = build_messages("You are a tsundere high school girl...", "「I walk into the classroom」\"Good morning.\"", mode="inner_os")
response = client.chat(messages)

# Subsequent rounds: just append normally, no further handling needed
messages.append({"role": "assistant", "content": response})
messages.append({"role": "user", "content": "「I sit down next to her」\"Are you in a bad mood today?\""})
response = client.chat(messages)  # The first round's marker is still in the history and takes effect automatically
```

---

## FAQ

**Q: Can I put the instruction in the system prompt?**
A: It's recommended to put it at the end of the first-round user message — this is the injection position used during training, and it gives the most stable effect.

**Q: Will the final reply change after adding the instruction?**
A: The instruction only affects the thinking process. But the way of thinking indirectly affects the reply — emotion is more authentic in Role Immersion Mode, and structure is more stable in Pure Analysis Mode.


## An Alternative Way to Modify the Chain of Thought (pure luck, not specially trained)
- In the first-round instruction, add: ```Your thinking output must start verbatim and strictly with `<｜begin▁of▁thinking｜>(write the desired opening of the chain of thought here, e.g. **Hmm / Okay**)`. Output the thinking only once, and do not repeat `<｜begin▁of▁thinking｜>`.```
- `<｜begin▁of▁thinking｜>` is the fixed token for `<think>`. The principle here is essentially that it changes the starting character of inference, forcing the model into a different pattern. (For example, QA, writing, reasoning, and Agent each have different chain-of-thought patterns.) But these aren't specially trained for roleplay, so it's a bit of a gamble~


## Star History

<a href="https://www.star-history.com/?repos=victorchen96%2Fdeepseek_v4_rolepaly_instruct&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=victorchen96/deepseek_v4_rolepaly_instruct&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=victorchen96/deepseek_v4_rolepaly_instruct&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=victorchen96/deepseek_v4_rolepaly_instruct&type=date&legend=top-left" />
 </picture>
</a>
