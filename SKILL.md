---
name: thai-token-optimizer
description: Use when the user communicates in Thai or asks to optimize token usage, context consumption, and response conciseness for Thai language interactions.
---

# Thai Token Optimizer (v2.2 Style & Token Guidelines)

A formatting and language convention guide designed to reduce token overhead when working with Thai prompts in Large Language Models.

---

## 1. Core Guidelines

### 1.1 Natural Thai Input
- Accept casual, conversational Thai from the user without requiring special shorthand or strict syntax.

### 1.2 English Internal Analysis
- Conduct internal analysis, step-by-step planning, and technical reasoning in clear, natural English.
- Keep subagent prompts, intermediate worker summaries, and scratchpad notes in concise English to reduce multi-byte UTF-8 token fragmentation.

### 1.3 Concise Thai Responses
When writing the final response to the user in Thai:
- Start directly with the answer or solution without ceremonial greetings (`สวัสดีครับ/ค่ะ`) or repeating the user's question back.
- Keep standard technical, programming, and architecture terms in English (`Config`, `Database`, `API`, `Function`, `Endpoint`).
- Prefer short connectors (`เพื่อ` instead of `เพื่อที่จะทำการ`, `เพราะ` instead of `เนื่องจากว่า`).
- Format explanations with bullet points, numbered steps, or tables for readability.

### 1.4 Code & Repository Conventions
- Write inline code comments, docstrings, debug logs, and Git commit messages in concise English.
- Use Thai inside source code only for user-facing UI labels and messages.

### 1.5 Code Editing & Data Efficiency
- **Initial Implementation**: Deliver complete, working code covering all requested features. Keep sample or mock data arrays compact (3–4 representative items rather than long repetitive lists).
- **Follow-up Edits**: When modifying existing code, apply targeted edits or show only the updated functions/blocks (`// ... existing code ...`) rather than repeating the entire unchanged file.
- **Error Diagnosis**: When addressing error logs or stack traces, state the root cause and fix directly without echoing the full raw log back.
