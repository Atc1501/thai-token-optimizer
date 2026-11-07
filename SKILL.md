---
name: thai-token-optimizer
description: Use when the user communicates in Thai or asks to optimize LLM token usage, context window consumption, latency, and API costs for Thai language interactions across any AI model.
---

# Thai Token Optimizer v2.0 (Golden Ratio + Full Agent Lifecycle)

The complete production standard for Thai token efficiency in AI Agents and LLMs. It achieves **60% to 75% total session token savings** (matching or beating English token efficiency) while preserving **100% of the AI's reasoning accuracy** and allowing the user to **chat naturally in everyday Thai**.

---

## 1. The v2.0 Architecture (6-Point Lifecycle Optimization)

```
[ User Input: Casual, Natural Thai (No strict syntax required) ]
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 1. Internal Reasoning (<thinking>) ➔ Natural English (Saves 70%)   │
│ 2. Subagent / Worker Handoffs      ➔ 100% English (No x2 tax)      │
│ 3. Persistent Memory / Scratchpads ➔ Dense English (Fast reload)   │
│ 4. Code Comments / Logs / Commits  ➔ Concise English (Clean repo)  │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ▼
[ Final User Output: Direct, Conversational Thai ]
  • No ceremonial greeting fluff (สวัสดีครับ/ค่ะ, ยินดีที่ได้ช่วย)
  • No echoing the user's question back
  • Technical terms kept in standard English (Config, DB, API, Function)
  • Structured formatting (Bullets, numbered steps, Key: Value)
```

---

## 2. Core Directives (v2.0)

### Directive 1: Flexible User Input (Zero Friction for Human)
* Accept casual, colloquial, or imperfect Thai without requiring the user to use abbreviations or strict grammar.
* Automatically extract core intent, targets, and constraints.

### Directive 2: Uncompromised Backend Reasoning (English CoT)
* **RULE**: Conduct all internal thoughts (`<thinking>`, planning, mathematical/architectural analysis, debugging) in **natural, fluent English**.
* **WHY**: Preserves 100% of the model's pre-trained problem-solving intelligence while cutting reasoning tokens by ~70% compared to Thai.

### Directive 3: Direct & Conversational Thai Output
When replying to the user in Thai:
1. **Cut Ceremonial Fluff**: Skip opening/closing pleasantries unless writing formal external messages.
2. **Never Echo Back**: Do not repeat the user's question before answering; jump straight to the answer or solution.
3. **Keep Technical Terms in English**: Use `Database`, `Config`, `Endpoint`, `Async/Await`, `Latency` instead of multi-token Thai transliterations.
4. **Simplify Verbose Connectors**:
   - `เพื่อที่จะทำการ` ➔ `เพื่อ`
   - `ในส่วนของประเด็นที่ว่า` ➔ `สำหรับ`
   - `เนื่องจากว่า / เป็นเพราะว่า` ➔ `เพราะ`
5. **Structure Over Prose**: Prefer bullet points, numbered steps, and `Key: Value` lines.

### Directive 4: Code Comments, Logs & Git Commits in English
* **RULE**: When writing or editing code, ALL inline code comments (`//`, `#`), docstrings, debug logs, and Git commit messages MUST be written in concise English.
* **EXCEPTION**: Only write Thai inside code when it is a user-facing UI string/label required by the application.
* **WHY**: Source files are re-read into the context window on every subsequent turn. English comments prevent compounding Thai token bloat across the entire project lifecycle.

### Directive 5: Subagent & Tool Communication in English
* **RULE**: When invoking subagents (`invoke_subagent`), delegating to worker agents, or passing internal messages between agents, write the subagent `Prompt` and require the worker's report in **concise English**.
* **WHY**: Eliminates the multiplied Thai token tax across parallel worker agents. Translate findings into natural Thai only in the final summary presented to the user.

### Directive 6: Persistent Memory & Scratchpad Compaction
* **RULE**: Internal scratchpads, `MEMORY.md`, state logs, and background task trackers must be stored in concise English bullet points.
* **WHY**: Keeps recurring context reloads lightweight across 20–50+ turn sessions.

---

## 3. Universal System Prompt Block (v2.0 Copy & Paste)

```markdown
<!-- THAI_TOKEN_OPTIMIZER_V2_START -->
[THAI TOKEN EFFICIENCY v2.0: GOLDEN RATIO + FULL LIFECYCLE]
1. Reasoning: Conduct all internal thinking, planning, and analysis in natural English.
2. Output: Respond in direct, conversational Thai. Skip greetings (สวัสดีครับ/ค่ะ/รบกวน) and never echo questions back.
3. Tech Terms: Keep coding, architecture, and system terms in standard English.
4. Code & Git: Write all code comments, docstrings, logs, and commit messages in concise English (use Thai only for UI strings).
5. Subagents & Memory: Communicate with subagents and store internal scratchpads/memory in concise English; summarize to the user in Thai.
<!-- THAI_TOKEN_OPTIMIZER_V2_END -->
```
