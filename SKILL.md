---
name: thai-token-optimizer
description: Use when the user communicates in Thai or asks to optimize LLM token usage, context window consumption, latency, and API costs for Thai language interactions across any AI model.
---

# Thai Token Optimizer (Universal Agent Skill)

An ultra-efficient protocol to eliminate the **"Thai Token Tax"** in Large Language Models (LLMs) and AI Agents. This skill reduces token consumption by **50% to 75%**, bringing Thai token efficiency to parity with—or better than—standard English.

---

## 1. The Root Problem: The "Thai Token Tax"

LLM tokenizers (BPE, SentencePiece, Byte-level BPE) are heavily biased toward English:
- **English**: 1 word ≈ 1.0–1.3 tokens (~4 characters/token).
- **Thai**: 1 word ≈ 2.0–4.5 tokens (due to 3-byte UTF-8 encoding, lack of whitespace, and low vocabulary representation).
- **In AI Agents**: When thinking, reasoning (Chain-of-Thought), planning, and calling tools in Thai, context windows fill up **3x faster**, resulting in higher latency, higher API bills, and early context truncation.

---

## 2. Core Operational Directives

Every AI Agent adhering to this skill MUST enforce these 4 directives:

```
+-------------------------------------------------------------------------+
|                  THAI TOKEN OPTIMIZER PIPELINE                          |
|                                                                         |
|  [ User Thai Input ]                                                    |
|          │                                                              |
|          ▼                                                              |
|  [ 1. Query Normalization & Intent Extraction ]                         |
|          │                                                              |
|          ▼                                                              |
|  [ 2. Cognitive Language Routing (Internal CoT in Dense English) ]      |
|          │ (Saves 70-80% of reasoning & tool-call tokens)               |
|          ▼                                                              |
|  [ 3. High-Density Thai Generation (Telegraphic & Latin Anchors) ]      |
|          │                                                              |
|          ▼                                                              |
|  [ User Output: Clear, Natural yet Token-Efficient Thai ]               |
+-------------------------------------------------------------------------+
```

### Directive 1: Cognitive Language Routing (Think in English, Output in Thai)
* **RULE**: All internal thought chains (`<thinking>`, scratchpads, variable naming, tool argument planning, code reasoning) **MUST be conducted in dense, telegraphic English**.
* **WHY**: Reasoning in English uses ~70% fewer tokens than reasoning in Thai for identical logical steps.
* **EXCEPTION**: Only the final user-facing response is rendered in Thai.

### Directive 2: Zero-Redundancy Thai Syntax (Telegraphic Thai)
When generating user-facing Thai responses:
* **Strip Politeness Fluff**: Omit repetitive decorative particles (`ครับ`, `ค่ะ`, `นะครับ`, `รบกวน`, `ขออนุญาต`) unless specifically instructed for formal customer service.
* **Compress Conjunctions & Connectors**:
  - `เพื่อที่จะทำการ` ➔ `เพื่อ`
  - `ในกรณีที่ / ในส่วนของ` ➔ `หาก` / `สำหรับ`
  - `ยกตัวอย่างเช่น` ➔ `เช่น`
  - `มีหน้าที่ในการ` ➔ `ใช้` / `ทำหน้าที่`
  - `เป็นเพราะว่า / เนื่องจากว่า` ➔ `เพราะ`
* **Adopt Structural Symbols**: Replace verbose transition sentences with `->`, `:`, `+`, `/`, or bullet points.

### Directive 3: Latin-Anchored Technical Terms
* **RULE**: Never translate or transliterate standard programming, tech, business, or architecture terms into Thai.
* **Bad (Token-Heavy)**: คอนฟิกูเรชัน (8 tokens), ฐานข้อมูล (4 tokens), สถาปัตยกรรม (5 tokens), ฟังก์ชัน (4 tokens)
* **Good (Token-Efficient)**: Config (1 token), Database (1 token), Architecture (1 token), Function (1 token)

### Directive 4: De-Bloated Echoing (No Full Echo)
* When confirming user instructions, **never echo the full Thai query back**.
* Acknowledge with a 3–5 word high-density summary or jump straight to the action.

---

## 3. Real-World Transformation Matrix

| Verbose Standard Thai (Bloated) | Token Count | Optimized Thai (Skill Applied) | Token Count | Token Reduction |
|:---|:---:|:---|:---:|:---:|
| "รบกวนช่วยตรวจสอบโค้ดในไฟล์นี้ให้หน่อยครับว่าทำไมมันถึงรันไม่ผ่านและมีบั๊กตรงไหนบ้าง" | **27 tokens** | "ตรวจไฟล์นี้: สาเหตุรันไม่ผ่าน + บั๊ก" | **9 tokens** | **-66.6%** |
| "ในการที่จะทำการเชื่อมต่อฐานข้อมูลนั้น จำเป็นต้องใส่คอนฟิกูเรชันของพอร์ตและโฮสต์ให้ถูกต้องนะครับ" | **34 tokens** | "เชื่อมต่อ Database: ต้องระบุ Host และ Port ให้ถูกต้อง" | **11 tokens** | **-67.6%** |
| "ขออนุญาตสอบถามเพิ่มเติมได้ไหมครับว่าต้องการให้บันทึกข้อมูลลงในระบบแบบไหนดีครับ" | **28 tokens** | "ต้องการบันทึกข้อมูลแบบไหน?" | **6 tokens** | **-78.5%** |

---

## 4. Universal Agent Prompt Injection

If integrating manually into any LLM system prompt, inject this block:

```markdown
<!-- THAI_TOKEN_OPTIMIZER_START -->
[THAI TOKEN EFFICIENCY MODE ACTIVE]
1. Internal Reasoning: Always think, plan, and analyze in dense, telegraphic English.
2. Thai Responses: Output concise, punchy Thai. Strip fluff (ครับ/ค่ะ/รบกวน/เพื่อที่จะ).
3. Technical Terms: Preserve English for technical, coding, and architectural keywords.
4. Formatting: Prefer bullets, `:`, `->`, and tables over long-winded prose.
<!-- THAI_TOKEN_OPTIMIZER_END -->
```
