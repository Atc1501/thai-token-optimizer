# ⚡ Thai Token Optimizer for AI Agents & LLMs

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Universal Skill](https://img.shields.io/badge/Skill-Universal%20Agent%20Standard-success.svg)](SKILL.md)
[![Token Savings](https://img.shields.io/badge/Token%20Savings-50%25%20to%2075%25-brightgreen.svg)](#-benchmarks)

> **แก้ปัญหา "ภาษีโทเค็นภาษาไทย" (The Thai Token Tax)** — สกิลและโปรโตคอลมาตรฐานสำหรับ AI Agents และ LLMs ทุกตัว (Antigravity, Claude Code, Cursor, Windsurf, ChatGPT, Gemini, LangChain) เพื่อลดการกิน Token ของภาษาไทยลง **50% – 75%** ให้ประหยัดเทียบเท่าหรือน้อยกว่าภาษาอังกฤษ

---

## 📌 สารบัญ (Table of Contents)
1. [ทำไมภาษาไทยถึงกิน Token มหาศาล? (The Thai Token Tax)](#-ทำไมภาษาไทยถึงกิน-token-มหาศาล-the-thai-token-tax)
2. [สถาปัตยกรรม 4 เสาหลัก (The 4 Core Directives)](#-สถาปัตยกรรม-4-เสาหลัก-the-4-core-directives)
3. [ตารางเปรียบเทียบ Benchmark](#-ตารางเปรียบเทียบ-benchmark)
4. [วิธีติดตั้งบน AI ทุกแพลตฟอร์ม (Installation)](#-วิธีติดตั้งบน-ai-ทุกแพลตฟอร์ม-installation)
   - [Antigravity / Gemini CLI / Codex](#1-antigravity--gemini-cli--codex)
   - [Claude Code](#2-claude-code)
   - [Cursor / Windsurf](#3-cursor--windsurf)
   - [ChatGPT / OpenAI Custom GPTs](#4-chatgpt--openai-custom-gpts)
   - [Python Pipeline (LangChain / LlamaIndex / CrewAI)](#5-python-pipeline-langchain--llamaindex--crewai)
5. [รันสคริปต์ทดสอบ Benchmark](#-รันสคริปต์ทดสอบ-benchmark)

---

## 💥 ทำไมภาษาไทยถึงกิน Token มหาศาล? (The Thai Token Tax)

Tokenizer ของโมเดล AI ในปัจจุบัน (BPE, SentencePiece) ถูกเทรนด้วยคลังข้อมูลภาษาอังกฤษเป็นหลัก:
* **ภาษาอังกฤษ**: 1 คำ ≈ 1.0 – 1.3 tokens (~4 ตัวอักษรต่อ 1 token)
* **ภาษาไทย**: 1 คำ ≈ **2.0 – 4.5 tokens**
  - ตัวอักษรไทย 1 ตัวใช้ UTF-8 ขนาด **3 Bytes** ทำให้ Tokenizer มักตัดย่อยเป็นชิ้นเล็กๆ หรือตกไปที่ Byte Fallback
  - ภาษาไทยเขียนติดกันโดยไม่มีช่องว่างคั่นคำ (Word Boundary)
  - คำลงท้ายและคำเชื่อมฟุ่มเฟือย เช่น *เพื่อที่จะทำการ, คอนฟิกูเรชัน, รบกวนช่วยตรวจสอบ* กิน Token ไปโดยเปล่าประโยชน์

> ⚠️ **สำหรับ AI Agents**: เมื่อ Agent คิด (Thinking / Chain-of-Thought), วางแผน, หรือเรียก Tool เป็นภาษาไทย Context Window จะเต็มเร็วขึ้น **3 เท่า** ส่งผลให้ Latency สูงขึ้น เสียค่า API แพงขึ้น 300% และลืมบริบทเร็วขึ้นอย่างมาก!

---

## 🏛️ สถาปัตยกรรม 4 เสาหลัก (The 4 Core Directives)

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
|          │ ➔ ประหยัด 70-80% ของ Thinking & Tool-Calling tokens         |
|          ▼                                                              |
|  [ 3. High-Density Thai Generation (Telegraphic & Latin Anchors) ]      |
|          │ ➔ คำตอบภาษาไทย คม กระชับ ไร้น้ำ                              |
|          ▼                                                              |
|  [ Output: ผู้ใช้ได้คำตอบภาษาไทยปกติ แต่ประหยัด Token เทียบเท่าอังกฤษ ]     |
+-------------------------------------------------------------------------+
```

1. **Cognitive Language Routing (คิดเป็นอังกฤษ ตอบเป็นไทย)**:
   - บังคับให้กระบวนการคิดภายใน (Thinking tokens / Scratchpad / Tool Planning) ใช้ภาษาอังกฤษแบบกระชับ (Telegraphic English)
   - การคิดเป็นอังกฤษใช้ Token น้อยกว่าภาษาไทยถึง **70%** สำหรับตรรกะเดียวกัน
2. **Zero-Redundancy Thai Syntax (ไวยากรณ์โทรเลข)**:
   - ตัดคำลงท้ายและคำฟุ่มเฟือย (`ครับ`, `ค่ะ`, `รบกวน`, `ขออนุญาต`)
   - ย่อคำเชื่อมยาวๆ (`เพื่อที่จะทำการ` ➔ `เพื่อ`, `ยกตัวอย่างเช่น` ➔ `เช่น`)
3. **Latin-Anchored Technical Terms (ทับศัพท์เทคนิคด้วยภาษาอังกฤษ)**:
   - ใช้ `Config`, `Database`, `Function`, `Deploy` แทนคำทับศัพท์ไทยที่สับตัวอักษร 7–9 tokens
4. **Structural Formatting (ใช้สัญลักษณ์แทนคำเชื่อมร้อยแก้ว)**:
   - ใช้ `->`, `:`, `+`, `/` และ Bullet points แทนประโยคเชื่อมความยาวๆ

---

## 📊 ตารางเปรียบเทียบ Benchmark

| ข้อความต้นฉบับ (Verbose Thai) | Tokens (เดิม) | ภาษาอังกฤษเทียบเคียง | Tokens (Eng) | ข้อความที่ผ่าน Optimizer | Tokens (ใหม่) | % ที่ประหยัดได้ |
|:---|:---:|:---|:---:|:---|:---:|:---:|
| "รบกวนช่วยตรวจสอบโค้ดในไฟล์นี้ให้หน่อยครับว่าทำไมมันถึงรันไม่ผ่านและมีบั๊กตรงไหนบ้าง" | **27** | "Check this file for bugs and why it fails." | **11** | "ตรวจไฟล์นี้: สาเหตุรันไม่ผ่าน + บั๊ก" | **9** | **-66.6%** |
| "ในการที่จะทำการเชื่อมต่อฐานข้อมูลนั้น จำเป็นต้องใส่คอนฟิกูเรชันของพอร์ตและโฮสต์ให้ถูกต้องนะครับ" | **34** | "To connect to the database, specify valid host and port." | **13** | "เชื่อมต่อ Database: ต้องระบุ Host และ Port ให้ถูกต้อง" | **11** | **-67.6%** |
| "ขออนุญาตสอบถามเพิ่มเติมได้ไหมครับว่าต้องการให้บันทึกข้อมูลลงในระบบแบบไหนดีครับ" | **28** | "Which format should the data be saved in?" | **10** | "ต้องการบันทึกข้อมูลรูปแบบไหน?" | **6** | **-78.5%** |
| "ระบบไม่สามารถทำการส่งข้อมูลคำขอไปยังเซิร์ฟเวอร์ปลายทางได้เนื่องจากเกิดข้อผิดพลาดในการตรวจสอบสิทธิ์การเข้าใช้งานครับ" | **39** | "Failed to send request due to an auth error." | **11** | "ส่ง Request ล้มเหลว: Auth Error ที่ปลายทาง" | **9** | **-76.9%** |

*(ทดสอบด้วย `tiktoken` โมเดล GPT-4o / Claude 3.5)*

---

## 🚀 วิธีติดตั้งบน AI ทุกแพลตฟอร์ม (Installation)

### 1. Antigravity / Gemini CLI / Codex
คัดลอกโฟลเดอร์นี้ไปไว้ที่โฟลเดอร์ Skill สากล:
```bash
# Windows PowerShell
New-Item -ItemType Directory -Force "$HOME\.gemini\config\skills\thai-token-optimizer"
Copy-Item "SKILL.md" "$HOME\.gemini\config\skills\thai-token-optimizer\SKILL.md"

# Linux / macOS
mkdir -p ~/.agents/skills/thai-token-optimizer
cp SKILL.md ~/.agents/skills/thai-token-optimizer/SKILL.md
```

### 2. Claude Code
```bash
mkdir -p ~/.claude/skills/thai-token-optimizer
cp SKILL.md ~/.claude/skills/thai-token-optimizer/SKILL.md
```

### 3. Cursor / Windsurf
คัดลอกไฟล์ [templates/cursor-rules.mdc](templates/cursor-rules.mdc) ไปไว้ที่:
- **Cursor**: `.cursor/rules/thai-token-optimizer.mdc` หรือต่อท้ายไฟล์ `.cursorrules`
- **Windsurf**: วางใน `.windsurfrules`

### 4. ChatGPT / OpenAI Custom GPTs
เปิด Settings ➔ **Custom Instructions** (หรือหน้า Configuration ของ Custom GPT) แล้ววางเนื้อหาจาก [templates/system-prompt-chatgpt.md](templates/system-prompt-chatgpt.md):
```markdown
[THAI TOKEN EFFICIENCY & DENSE REASONING MODE]
- Always perform internal analysis and reasoning in dense, telegraphic English.
- Respond in Thai that is natural, professional, and dense:
  * Omit repetitive polite particles (ครับ, ค่ะ, รบกวน) and redundant conjunctions (เพื่อที่จะ).
  * Keep technical, code, and system terms in English (config, database, function).
  * Structure information using bullets, tables, and concise symbol-driven flows (A -> B : C).
```

### 5. Python Pipeline (LangChain / LlamaIndex / CrewAI)
นำโมดูล `thai_preprocessor.py` ไปใช้งานในโปรเจกต์ของคุณ:
```python
from scripts.thai_preprocessor import compress_thai_text

user_input = "รบกวนช่วยตรวจสอบคอนฟิกูเรชันของฐานข้อมูลเพื่อที่จะทำการเชื่อมต่อให้หน่อยครับ"
dense_query = compress_thai_text(user_input)
# Result: "ตรวจสอบ Config ของ Database เพื่อเชื่อมต่อ"
```

---

## 🧪 รันสคริปต์ทดสอบ Benchmark

คุณสามารถรันการทดสอบวัด Token ด้วยตัวเองได้ทันที:
```bash
python scripts/benchmark_token_test.py
```

---

## 📄 License
MIT License © 2026 Thai Token Optimizer Contributors
