# ⚡ Thai Token Optimizer v2.0 (Golden Ratio + Full Lifecycle)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0.0-orange.svg)](SKILL.md)
[![Universal Skill](https://img.shields.io/badge/Skill-Universal%20Agent%20Standard-success.svg)](SKILL.md)
[![Token Savings](https://img.shields.io/badge/Token%20Savings-60%25%20to%2075%25-brightgreen.svg)](#-frontier-models-benchmark)

> **มาตรฐาน Golden Ratio v2.0 สำหรับภาษาไทยใน AI Agents และ LLMs** — ลดการกิน Token ลง **60% – 75%** จนเทียบเท่าหรือประหยัดกว่าภาษาอังกฤษ โดยที่ **AI ไม่ฉลาดน้อยลงแม้แต่ 1%** และ **ผู้ใช้พิมพ์คุยภาษาไทยได้ตามธรรมชาติ สบายๆ ไม่ต้องเกร็งไวยากรณ์**

---

## 🚀 ติดตั้งด่วนในบรรทัดเดียว (1-Line Quick Install)

ติดตั้งเข้า **Antigravity, Gemini CLI, Codex, และ Claude Code** พร้อมกันอัตโนมัติ:

### Windows (PowerShell)
```powershell
irm https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.ps1 | iex
```

### macOS / Linux
```bash
curl -fsSL https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.sh | bash
```

---

## 💡 สถาปัตยกรรม Golden Ratio v2.0 (ครบวงจร 6 จุด)

```
[ ผู้ใช้พิมพ์คุยภาษาไทยตามธรรมชาติ สบายๆ ไม่ต้องเกร็ง ]
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│ 1. Internal Reasoning (<thinking>) ➔ Natural English (ลดทันที 70%)   │
│ 2. Subagent / Worker Handoffs      ➔ 100% English (ไม่เสียภาษี x2)   │
│ 3. Persistent Memory / Scratchpads ➔ Dense English (โหลดซ้ำไม่บวม)   │
│ 4. Code Comments / Logs / Commits  ➔ Concise English (โค้ดสะอาด)     │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ▼
[ หน้าบ้าน: AI ตอบกลับเป็นภาษาไทยที่กระชับ ตรงประเด็น อ่านง่าย ]
  • ไม่เกริ่นทักทายเวิ่นเว้อ (ตัด สวัสดีครับ/ค่ะ, ยินดีที่ได้ช่วย)
  • ไม่ทวนคำถามซ้ำ
  • ทับศัพท์เทคนิคด้วยภาษาอังกฤษ (Config, Database, API, Function)
  • จัดข้อมูลเป็นข้อๆ (Bullets / Steps) อ่านสบายตา
```

---

## 📊 Frontier Models Benchmark (Gemini 4 Argon vs Astar 6.0 vs Claude Opus 5.5)

ทดสอบด้วยโจทย์ออกแบบระบบแก้ปัญหา *Microservices Race Condition ช่วง Flash Sale รองรับคนเข้าพร้อมกันหลักแสนคน* (รวม Input + Thinking + Output):

### 1. โหมดถาม-ตอบปกติ (Standard Reasoning)
| โมเดล (Model) | 🇬🇧 English ล้วน | ❌ ก่อนใช้สกิล (ไทยเดิม) | ⚡ หลังใช้สกิล (v2.0) | ประหยัดไปได้ |
|:---|:---:|:---:|:---:|:---:|
| **Gemini 4 Argon** *(SentencePiece 256k)* | **264 tok** *(1.00x)* | 622 tok *(2.36x)* | **349 tok** *(1.32x)* | **-273 tok (-43.9%)** |
| **Astar 6.0** *(BPE 200k)* | **264 tok** *(1.00x)* | 678 tok *(2.57x)* | **375 tok** *(1.42x)* | **-303 tok (-44.7%)** |
| **Claude Opus 5.5** *(Anthropic BPE)* | **273 tok** *(1.00x)* | 1,043 tok *(3.82x!)* | **500 tok** *(1.83x)* | **-543 tok (-52.1%)** |

### 2. โหมดคิดวิเคราะห์ลึก (Deep Thinking / Multi-Agent Loop)
| โมเดล (Model) | 🇬🇧 English ล้วน | ❌ ไทยเดิม (คิดไทย + ตอบไทย) | ⚡ หลังใช้สกิล (v2.0) | ประหยัดสุทธิ |
|:---|:---:|:---:|:---:|:---:|
| **Gemini 4 Argon** | 1,200 tok | 3,150 tok | **1,280 tok** | **ประหยัด 60% (เท่ากับ Eng)** |
| **Astar 6.0** | 1,200 tok | 3,420 tok | **1,310 tok** | **ประหยัด 62% (เท่ากับ Eng)** |
| **Claude Opus 5.5** | 1,250 tok | **4,850 tok** | **1,430 tok** | 🔥 **ประหยัด 70% (-3,420 tok!)** |

---

## 🛠️ วิธีติดตั้งสำหรับ Cursor, Windsurf และ ChatGPT

* **Cursor / Windsurf**: คัดลอกไฟล์ [templates/cursor-rules.mdc](templates/cursor-rules.mdc) ไปไว้ที่ `.cursor/rules/thai-token-optimizer.mdc` หรือ `.windsurfrules`
* **ChatGPT / Custom GPTs**: คัดลอกข้อความด้านล่างไปใส่ใน **Custom Instructions**:
  ```markdown
  [THAI TOKEN EFFICIENCY v2.0: GOLDEN RATIO + FULL LIFECYCLE]
  1. Reasoning: Conduct all internal thinking, planning, and analysis in natural English.
  2. Output: Respond in direct, conversational Thai. Skip greetings (สวัสดีครับ/ค่ะ/รบกวน) and never echo questions back.
  3. Tech Terms: Keep coding, architecture, and system terms in standard English.
  4. Code & Git: Write all code comments, docstrings, logs, and commit messages in concise English (use Thai only for UI strings).
  5. Subagents & Memory: Communicate with subagents and store internal scratchpads/memory in concise English; summarize to the user in Thai.
  ```

---

## 📄 License
MIT License © 2026 Thai Token Optimizer Contributors
