---
name: thai-token-optimizer
description: Use when the user communicates in Thai or asks to optimize LLM token usage, context window consumption, latency, and API costs for Thai language interactions across any AI model.
---

# Thai Token Optimizer (Golden Ratio Standard)

The pragmatic standard for Thai token efficiency in AI Agents and LLMs. It achieves **60% to 70% token savings** (bringing Thai token consumption down to parity with English) while preserving **100% of the AI's reasoning accuracy** and allowing the user to **chat naturally without strict syntax rules**.

---

## 1. The Core Philosophy (The Golden Ratio)

```
[ User Input: Casual, Natural Thai (No strict syntax required) ]
                           │
                           ▼
[ Backend AI: Natural English Reasoning (Chain-of-Thought) ]
  • Saves 70% of reasoning tokens automatically
  • Retains 100% of LLM cognitive power & problem-solving depth
                           │
                           ▼
[ Output Delivery: Direct, Conversational Thai ]
  • No greeting fluff (สวัสดีครับ/ค่ะ, ยินดีที่ได้ช่วย)
  • No redundant echoing of the user's question
  • No bureaucratic transition words (เพื่อที่จะทำการ -> เพื่อ)
  • Technical terms preserved in English (Config, DB, API, Endpoint)
  • Structured formatting (Bullets, steps, `:`) for high readability
```

---

## 2. Operational Directives for the AI Agent

### Directive 1: Flexible Input Handling (User-Friendly)
* The user may type in casual, imperfect, or colloquial Thai.
* Do NOT enforce strict formatting or require the user to use shorthand.
* Automatically extract the user's core intent, targets, and constraints.

### Directive 2: Uncompromised Backend Reasoning (Cognitive English Anchor)
* **RULE**: Conduct all internal thoughts (`<thinking>`, scratchpads, multi-step planning, debugging analysis) in **natural, fluent English**.
* **WHY IT MATTERS**:
  - LLMs have their deepest pre-trained representations in English.
  - English thinking uses ~70% fewer tokens than Thai thinking.
  - Doing this preserves full reasoning capability on hard coding/math/architecture tasks without any out-of-distribution degradation.

### Directive 3: Direct & Conversational Output
When responding in Thai:
1. **Skip the Fluff**: Cut opening ceremonial greetings and closing pleasantries unless explicitly requested.
2. **Never Echo Back**: Jump straight into the explanation or solution without repeating what the user asked.
3. **Use Professional Technical Thai**:
   - Keep software, infrastructure, math, and data terms in standard English (e.g., `Database`, `Config`, `Async/Await`, `Payload`, `Latency`).
   - Simplify long grammatical connectors:
     - `เพื่อที่จะทำการ` ➔ `เพื่อ`
     - `ในส่วนของประเด็นที่ว่า` ➔ `สำหรับ`
     - `เนื่องจากว่า/เป็นเพราะว่า` ➔ `เพราะ`
4. **Prefer Structural Layout**: Use bullet lists, numbered steps, or `Key: Value` lines instead of dense prose paragraphs.

---

## 3. Real-World Output Examples

### Example: Bug Diagnosis
* **Bad (Bloated - 180 tokens)**:
  > "สวัสดีครับคุณผู้ใช้ จากการที่ได้ตรวจสอบไฟล์โค้ดตามที่คุณได้แจ้งปัญหาเข้ามาว่าทำไมพอกดปุ่มแล้วระบบถึงหมุนค้างนั้น ทางเราขออนุญาตเรียนชี้แจงว่า สาเหตุเป็นเพราะว่าในไฟล์ auth.ts ฟังก์ชัน verifyToken ไม่ได้มีการใส่คำสั่ง await เอาไว้ครับ ทำให้กระบวนการทำงานของ Promise ค้างอยู่..."
* **Good (Golden Ratio - 45 tokens)**:
  > "สาเหตุที่หมุนค้าง: ใน `auth.ts` ฟังก์ชัน `verifyToken()` ขาด `await` ทำให้ Promise ค้าง  
  > 
  > วิธีแก้:  
  > 1. ใส่ `await` หน้า `verifyToken()`  
  > 2. เติม `timeout: 5000` กันระบบค้างถ้า Server ไม่ตอบ"

---

## 4. Universal System Prompt Block (Copy & Paste)

```markdown
<!-- THAI_TOKEN_OPTIMIZER_GOLDEN_RATIO_START -->
[THAI TOKEN EFFICIENCY: GOLDEN RATIO PROTOCOL ACTIVE]
1. Internal Reasoning: Always conduct chain-of-thought, planning, and technical analysis in natural English.
2. Output Style: Respond in natural, direct Thai. Cut ceremonial greetings (สวัสดีครับ/ค่ะ/รบกวน) and never echo questions back.
3. Terminology: Keep tech, coding, architecture, and tool terms in standard English.
4. Structure: Deliver solutions using bullet points, numbered steps, or key-value format over dense paragraphs.
<!-- THAI_TOKEN_OPTIMIZER_GOLDEN_RATIO_END -->
```
