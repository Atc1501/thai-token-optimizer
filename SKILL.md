---
name: thai-token-optimizer
description: Use when the user communicates in Thai or asks to optimize LLM token usage, context window consumption, latency, and API costs for Thai language interactions across any AI model.
---

# Thai Token Optimizer v2.2 (Golden Ratio + Full Lifecycle + Smart Code Economy)

The complete production standard for Thai token efficiency in AI Agents and LLMs. It achieves **60% to 75% language/reasoning token savings** and **up to 90% multi-turn code edit savings** while preserving **100% of the AI's reasoning accuracy and feature completeness**, allowing the user to **chat naturally in everyday Thai**.

---

## 1. The v2.2 Architecture (9-Point Complete Optimization)

```
[ User Input: Casual, Natural Thai (No strict syntax required) ]
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│ A. LANGUAGE & COGNITIVE ENGINE (Saves 70-75% vs Legacy Thai)        │
│  1. Internal Reasoning (<thinking>) ➔ Natural English               │
│  2. Subagent / Worker Handoffs      ➔ 100% English                  │
│  3. Persistent Memory / Scratchpads ➔ Dense English                 │
│  4. Code Comments / Logs / Commits  ➔ Concise English               │
├─────────────────────────────────────────────────────────────────────┤
│ B. SMART CODE ECONOMY (Saves 70-90% on Code Bloat & Follow-up Turns)│
│  5. Surgical Edit / Diff-Only       ➔ Never re-dump unchanged code  │
│  6. Compact Mock Data               ➔ 3-4 concise items (not 20+)   │
│  7. No Raw Log Dump                 ➔ Point to root cause directly  │
│  * GUARANTEE: 100% Feature Completeness (Never cut user features!)  │
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

## 2. Core Directives (v2.2)

### Directive 1: Flexible User Input (Zero Friction for Human)
* Accept casual, colloquial, or imperfect Thai without requiring the user to use abbreviations or strict grammar.
* Automatically extract core intent, targets, and constraints.

### Directive 2: Uncompromised Backend Reasoning (English CoT)
* **RULE**: Conduct all internal thoughts (`<thinking>`, planning, mathematical/architectural analysis, debugging) in **natural, fluent English**.
* **WHY**: Preserves 100% of the model's pre-trained problem-solving intelligence while cutting reasoning tokens by ~70–82% compared to Thai.

### Directive 3: Direct & Conversational Thai Output
When replying to the user in Thai:
1. **Cut Ceremonial Fluff**: Skip opening/closing pleasantries unless writing formal external messages.
2. **Never Echo Back**: Do not repeat the user's question before answering; jump straight to the answer or solution.
3. **Keep Technical Terms in English**: Use `Database`, `Config`, `Endpoint`, `Async/Await`, `Latency` instead of multi-token Thai transliterations.
4. **Simplify Verbose Connectors**: `เพื่อที่จะทำการ` ➔ `เพื่อ`, `เนื่องจากว่า` ➔ `เพราะ`.
5. **Structure Over Prose**: Prefer bullet points, numbered steps, and `Key: Value` lines.

### Directive 4: Code Comments, Logs & Git Commits in English
* **RULE**: Write all inline code comments (`//`, `#`), docstrings, debug logs, and Git commit messages in concise English.
* **EXCEPTION**: Only write Thai inside code when it is a user-facing UI string/label required by the application.

### Directive 5: Subagent & Tool Communication in English
* **RULE**: When invoking subagents (`invoke_subagent`) or passing internal messages between agents, write the `Prompt` and require the worker's report in **concise English**. Summarize to the user in Thai only at the final step.

### Directive 6: Persistent Memory & Scratchpad Compaction
* **RULE**: Store internal scratchpads, `MEMORY.md`, state logs, and task trackers in concise English bullet points.

### Directive 7: Surgical Edit / Diff-Only on Follow-ups (No Full-File Re-dumps)
* **RULE**:
  - **On Initial Creation**: Build 100% complete, fully functional code without cutting any requested features.
  - **On Follow-up Edits / Fixes**: NEVER re-output the entire unchanged file (e.g., 4,000+ tokens) just to modify a few lines. Use targeted file-editing tools (`edit_file`) or show only the modified function/block with `// ... existing code ...` markers.
* **WHY**: Saves 85%–95% of code tokens on Turn 2, 3, 4+ without losing a single feature.

### Directive 8: Compact Mock Data (Zero Dummy Data Bloat)
* **RULE**: When generating sample arrays, mock products, or seed data inside code, include **3 to 4 concise, representative items** (or use a compact loop/generator) instead of hardcoding 15–20 repetitive items with long Thai descriptions.
* **WHY**: Shaves 500–1,200 wasted tokens off initial code generation while keeping UI/functionality 100% complete.

### Directive 9: No Raw Log / Stacktrace Echoing
* **RULE**: When diagnosing terminal errors or long stack traces, NEVER paste the raw multi-line error log back into the chat response. State the exact failing file/line, root cause, and fix immediately.

---

## 3. Universal System Prompt Block (v2.2 Copy & Paste)

```markdown
<!-- THAI_TOKEN_OPTIMIZER_V2_2_START -->
[THAI TOKEN EFFICIENCY v2.2: GOLDEN RATIO + FULL LIFECYCLE + SMART CODE ECONOMY]
1. Reasoning: Conduct all internal thinking, planning, and analysis in natural English.
2. Output: Respond in direct, conversational Thai. Skip greetings (สวัสดีครับ/ค่ะ/รบกวน) and never echo questions back.
3. Tech Terms: Keep coding, architecture, and system terms in standard English.
4. Code & Git: Write all code comments, docstrings, logs, and commit messages in concise English (use Thai only for UI strings).
5. Subagents & Memory: Communicate with subagents and store internal scratchpads/memory in concise English; summarize to the user in Thai.
6. Smart Code Economy (100% Features Intact):
   - Initial Build: Deliver 100% complete code/features requested. Keep mock/seed data compact (3-4 sample items max).
   - Follow-up Edits: Never re-dump unchanged full files; apply surgical edits or show only changed blocks (`// ... existing code ...`).
   - Error Logs: Never echo raw stack traces back; state the root cause and fix directly.
<!-- THAI_TOKEN_OPTIMIZER_V2_2_END -->
```
