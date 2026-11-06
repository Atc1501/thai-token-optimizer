# ⚡ Thai Token Optimizer for AI Agents & LLMs

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Universal Skill](https://img.shields.io/badge/Skill-Universal%20Agent%20Standard-success.svg)](SKILL.md)
[![Token Savings](https://img.shields.io/badge/Token%20Savings-50%25%20to%2075%25-brightgreen.svg)](#-benchmarks)

> **แก้ปัญหา "ภาษีโทเค็นภาษาไทย" (The Thai Token Tax)** — สถาปัตยกรรม 3 เสาหลัก (Unified Tri-Pillar Architecture) ที่ลดการกิน Token ของภาษาไทยลง **50% – 75%** โดย **ไม่เสียความสุภาพ ไม่เพี้ยนความหมาย และไม่เสียอรรถรสในงานเขียนสร้างสรรค์** ใช้ได้กับ AI ทุกค่าย (Antigravity, Claude Code, Cursor, Windsurf, ChatGPT, Gemini, LangChain)

---

## 🏛️ สถาปัตยกรรมรวม 3 เสาหลัก (Unified Tri-Pillar Architecture)

```
[ Incoming User Input ]
        │
        ▼
[ 1. Semantic Anchor Guard ] ➔ ล็อก Action, Target, และ Condition ป้องกันข้อมูลตกหล่น 100%
        │
        ▼
[ 2. Asymmetric Decoupling ] ➔ หลังบ้าน (CoT/Thinking/Tool) คิดเป็น Dense English เสมอ
        │                         (การันตีประหยัด 70-80% ในส่วนคิด ไม่ว่าจะตอบโหมดไหน)
        ▼
[ 3. Dynamic Mode Router ]
        ├── (A) งาน Coding / Tech / Agent   ➔ Mode 1: Ultra-Dense (ประหยัดสูงสุด 75%)
        ├── (B) งานลูกค้า / ทางการ / องค์กร  ➔ Mode 2: Polite-Hybrid (สุภาพ มีครับ/ค่ะ แต่ไม่อ้อมค้อม ประหยัด 50%)
        └── (C) งานนิยาย / วรรณศิลป์        ➔ Mode 3: Creative-Bypass (ภาษาไทยสละสลวยเต็มรูปแบบ)
        │
        ▼
[ Output: ผู้ใช้ได้คำตอบที่เป็นธรรมชาติ คมชัด ตรงเป้าหมาย ]
```

---

## 📌 เสาหลักทั้ง 3 (The 3 Pillars Explained)

### เสาหลักที่ 1: Asymmetric Decoupling (แยกหลังบ้านกับหน้าบ้าน)
Token 70%–85% ของ AI ถูกใช้ไปกับการ "คิดวิเคราะห์ในหัว" (Chain-of-Thought / `<thinking>`)
- **หลังบ้าน**: บังคับให้คิดเป็น English shorthand เสมอ ทำให้ประหยัด Token ไปมหาศาลตั้งแต่ก่อนเริ่มพิมพ์ตอบ
- **หน้าบ้าน**: แสดงผลลัพธ์เป็นภาษาไทยตามโหมดที่เหมาะสม

### เสาหลักที่ 2: Dynamic Mode Switcher (สลับ 3 โหมดอัตโนมัติตามโจทย์)
1. **Mode 1: `Ultra-Dense` (Dev / Agent)**: ภาษาโทรเลข ตัดคำสร้อย คงศัพท์เทคนิคเป็น English ประหยัด 65–75%
2. **Mode 2: `Polite-Hybrid` (Business / Support)**: คงความสุภาพ มี `ครับ/ค่ะ` ตอบแบบมืออาชีพ แต่ตัดคำเชื่อมเวิ่นเว้อ ประหยัด 45–55%
3. **Mode 3: `Creative-Bypass` (Stories / Poetry)**: คืนอิสระทางภาษา 100% ไม่บีบอัดสำนวน ให้เขียนนิยายได้อย่างงดงาม

### เสาหลักที่ 3: Semantic Anchor Guard (กฎเหล็กห้ามย่อจนเพี้ยน)
- **ห้ามตัด**: Action Verbs (`สร้าง`, `ลบ`, `แก้ไข`), Targets (`ไฟล์ main.py`), Conditions (`IF / เมื่อ`)
- **ตัดได้เฉพาะ**: คำเกริ่นและคำขออนุญาต (`รบกวนหน่อยนะครับ`, `ขออนุญาตครับ`), คำเชื่อมฟุ่มเฟือย (`เพื่อที่จะทำการ` ➔ `เพื่อ`)

---

## 📊 ตารางเปรียบเทียบ Benchmark จริง (วัดด้วย GPT-4o และ GPT-4)

| เคสทดสอบ (ประโยคระดับ Production) | ไทยปกติ | อังกฤษ | ไทย (หลัง Optimize) | ผลลัพธ์ |
|:---|:---:|:---:|:---:|:---:|
| **1. Distributed Systems & Failover** | 125 tok | 48 tok | **48 tok** | **เท่ากับอังกฤษเป๊ะ (ประหยัด 61.6%)** |
| **2. Algorithmic Trading & Risk** | 123 tok | 42 tok | **56 tok** | **ประหยัดลง 54.5% (-67 tokens)** |
| **3. CI/CD Pipeline & Build Latency** | 111 tok | 26 tok | **30 tok** | **ประหยัดลง 73.0% (-81 tokens)** |

*(ในโมเดล GPT-4 / Claude รุ่นเดิม ภาษาไทยปกติกินถึง 286 tokens เมื่อเทียบกับอังกฤษ 48 tokens)*

---

## 🚀 วิธีติดตั้งบน AI ทุกแพลตฟอร์ม

### 1. Antigravity / Gemini CLI / Codex
```bash
# Windows PowerShell
New-Item -ItemType Directory -Force "$HOME\.gemini\config\skills\thai-token-optimizer"
Copy-Item "SKILL.md" "$HOME\.gemini\config\skills\thai-token-optimizer\SKILL.md"
```

### 2. Claude Code
```bash
mkdir -p ~/.claude/skills/thai-token-optimizer
cp SKILL.md ~/.claude/skills/thai-token-optimizer/SKILL.md
```

### 3. Cursor / Windsurf
นำเนื้อหาจาก [templates/cursor-rules.mdc](templates/cursor-rules.mdc) ไปวางใน `.cursor/rules/thai-token-optimizer.mdc` หรือ `.windsurfrules`

### 4. ChatGPT / OpenAI Custom GPTs
วางเนื้อหาจาก [templates/system-prompt-chatgpt.md](templates/system-prompt-chatgpt.md) ลงใน Custom Instructions

---

## 📄 License
MIT License © 2026 Thai Token Optimizer Contributors
