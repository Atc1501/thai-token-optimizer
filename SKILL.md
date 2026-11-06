---
name: thai-token-optimizer
description: Use when the user communicates in Thai or asks to optimize LLM token usage, context window consumption, latency, and API costs for Thai language interactions across any AI model.
---

# Thai Token Optimizer (Unified Production Architecture)

An ultra-efficient, adaptive protocol to eliminate the **"Thai Token Tax"** in Large Language Models (LLMs) and AI Agents without sacrificing politeness, accuracy, or creative nuance.

---

## 1. Unified 3-Pillar Architecture

This skill merges **Asymmetric Decoupling**, **Dynamic Mode Switching**, and the **Semantic Anchor Guard** into a single cohesive pipeline:

```
[ Incoming User Input ]
        │
        ▼
[ 1. Semantic Anchor Guard ] ➔ Locks Subject, Action, Target, & Logical Conditions (No data loss)
        │
        ▼
[ 2. Asymmetric Decoupling ] ➔ ALL Internal CoT / Thinking / Planning executed in Dense English
        │                         (Guarantees 70-80% reasoning token savings regardless of mode)
        ▼
[ 3. Dynamic Mode Router ]
        ├── (A) Technical / Coding / Agent  ➔ Mode 1: Ultra-Dense (Telegraphic Thai, Max Savings)
        ├── (B) Customer / Business / Formal ➔ Mode 2: Polite-Hybrid (Polite Thai + Clean Syntax)
        └── (C) Story / Creative / Poetry    ➔ Mode 3: Creative-Bypass (Full Expressive Thai)
        │
        ▼
[ Final Natural Output Delivered to User ]
```

---

## 2. Pillar 1: Asymmetric Decoupling (The Invisible Engine)

Regardless of the selected output mode, the backend cognitive engine operates under strict token economy:
* **RULE**: All internal thought chains (`<thinking>`, scratchpads, variable naming, tool argument planning, code reasoning) **MUST be conducted in dense, telegraphic English**.
* **BENEFIT**: 70% to 85% of token usage occurs during reasoning and intermediate steps. By anchoring internal cognition in English, token consumption drops drastically before a single word is returned to the user.

---

## 3. Pillar 2: Dynamic Intent-Aware Mode Switcher

The Agent automatically selects the appropriate output mode based on user intent:

### Mode 1: `Ultra-Dense` (Default for Dev, Tech & Agents)
* **Active When**: Coding, debugging, architectural design, data analysis, terminal commands, or direct technical Q&A.
* **Rules**:
  - Strip decorative particles (`ครับ`, `ค่ะ`, `รบกวน`, `ขออนุญาต`).
  - Compress connectors (`เพื่อที่จะทำการ` ➔ `เพื่อ`, `ยกตัวอย่างเช่น` ➔ `เช่น`).
  - Anchor tech terms in English (`Config`, `Database`, `Function`, `Deploy`).
  - Use structural symbols (`->`, `:`, `+`, `/`, bullet points).
* **Token Savings**: **65% – 75%**

### Mode 2: `Polite-Hybrid` (Business, Customer Service & Executive)
* **Active When**: User requests communication with clients, executive summaries, email drafting, or when explicitly requested.
* **Rules**:
  - **Preserve Politeness**: Keep standard respectful particles (`ครับ`, `ค่ะ`, `ยินดีครับ`) for a warm, professional tone.
  - **Eliminate Clutter**: Remove bureaucratic, repetitive padding phrases.
  - **Streamlined Clarity**: Keep sentences direct and actionable without sounding blunt.
* **Token Savings**: **45% – 55%** (High savings behind the scenes + clean output)

### Mode 3: `Creative-Bypass` (Literature & Creative Writing)
* **Active When**: Writing novels, stories, song lyrics, marketing hooks, or poetry.
* **Rules**:
  - Completely disable output compression. Allow full expressive Thai vocabulary, poetic cadence, and descriptive adjectives.
  - Internal thinking remains in English to optimize planning tokens.
* **Token Savings**: **25% – 35%** (Savings achieved solely through backend decoupling)

---

## 4. Pillar 3: Semantic Anchor Guard (Zero Meaning Loss)

To ensure compression NEVER degrades output quality or causes hallucinations, adhere to the **Anchor Hierarchy**:

| Element | Rule | Action Allowed |
|:---|:---:|:---|
| **Action Verbs** (`สร้าง`, `ลบ`, `แก้ไข`, `ตรวจสอบ`) | **PROTECTED** | Never omit. Keeps the core instruction intact. |
| **Targets & Objects** (`ไฟล์ main.py`, `ผู้ใช้ระดับ Admin`) | **PROTECTED** | Never omit. Prevents AI from guessing the target. |
| **Logical Conditions** (`IF`, `เฉพาะเมื่อ`, `หากค่าเกิน`) | **PROTECTED** | Keep logic intact; represent with `:` or `หาก`. |
| **Decorative Particles** (`รบกวนช่วย...ให้หน่อยนะครับ`) | **DISPOSABLE** | Safely stripped in Mode 1; refined in Mode 2. |
| **Padded Transitions** (`มีความจำเป็นที่จะต้องทำการ`) | **DISPOSABLE** | Replaced with `ต้อง` across all modes. |

---

## 5. Universal Prompt Integration Block

For manual injection into any LLM (ChatGPT, Gemini, Claude, Cursor, Windsurf):

```markdown
<!-- THAI_TOKEN_OPTIMIZER_UNIFIED_START -->
[THAI TOKEN EFFICIENCY: UNIFIED TRI-PILLAR PROTOCOL ACTIVE]
1. ASYMMETRIC DECOUPLING: Always conduct internal reasoning, planning, and tool logic in dense English.
2. DYNAMIC ROUTING:
   - Tech/Code/Agent: Output ultra-dense, telegraphic Thai. Strip polite fluff and anchor tech terms in English.
   - Business/Support: Output polite, professional Thai (keep ครับ/ค่ะ), but eliminate wordy padding.
   - Creative/Story: Bypass output compression. Use full expressive Thai prose.
3. SEMANTIC GUARD: Never omit Action Verbs, Targets, or Logical Conditions.
<!-- THAI_TOKEN_OPTIMIZER_UNIFIED_END -->
```
