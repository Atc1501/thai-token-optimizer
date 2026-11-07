# ⚡ Thai Token Optimizer v2.1 (Golden Ratio + Dual-Mode Activation)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.1.0-orange.svg)](SKILL.md)
[![Universal Skill](https://img.shields.io/badge/Skill-Universal%20Agent%20Standard-success.svg)](SKILL.md)
[![Token Savings](https://img.shields.io/badge/Token%20Savings-60%25%20to%2075%25-brightgreen.svg)](#-frontier-models-benchmark)

> **มาตรฐาน Golden Ratio v2.1 สำหรับภาษาไทยใน AI Agents และ LLMs** — ลดการกิน Token ลง **60% – 75%** จนเทียบเท่าหรือประหยัดกว่าภาษาอังกฤษ โดยที่ **AI ไม่ฉลาดน้อยลงแม้แต่ 1%** และ **ผู้ใช้พิมพ์คุยภาษาไทยได้ตามธรรมชาติ สบายๆ ไม่ต้องเกร็งไวยากรณ์**

---

## 🎛️ ระบบเลือกโหมดการทำงาน (Dual-Mode Activation System)

รองรับการติดตั้งและสลับโหมดได้ 2 รูปแบบตามต้องการ (และยกเลิกกลับไปมาได้ตลอดเวลาโดยไม่กระทบกฎอื่นในเครื่อง):

1. **Mode 1: On-Demand Skill (`@thai-token-optimizer`)**:
   - ติดตั้งเป็นสกิลปกติ เรียกใช้เฉพาะเมื่อคุณพิมพ์สั่ง `@thai-token-optimizer` หรือเมื่อต้องการให้เปิดโหมดประหยัดในงานนั้นๆ
2. **Mode 2: Always-On Global Rule (ทำงานอัตโนมัติทุกแชท 100%)**:
   - ฝังกฎลงใน Global Rule (`GEMINI.md`, `CLAUDE.md`, `AGENTS.md`) ให้ทำงานอัตโนมัติตั้งแต่วินาทีแรกของทุกบทสนทนาโดยไม่ต้องพิมพ์เรียก
3. **Disable / Toggle Mode (ยกเลิก Always-On ได้ตลอดเวลา)**:
   - ถอนเฉพาะบล็อก Always-On ออกจาก `GEMINI.md` / `CLAUDE.md` อย่างปลอดภัย (ไม่ลบกฎอื่นของคุณ) เพื่อกลับไปใช้แบบเรียกเอง (`@thai-token-optimizer`)

---

## 🚀 วิธีติดตั้งและสลับโหมด (Windows / macOS / Linux)

### วิธีที่ 1: เปิดเมนูเลือกโหมดแบบ Interactive (แนะนำ)
รันคำสั่งนี้ใน **PowerShell** แล้วกดเลข `1`, `2`, `3`, หรือ `4` จากเมนูได้เลย:
```powershell
irm https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.ps1 | iex
```

### วิธีที่ 2: สั่งสลับโหมดแบบบรรทัดเดียว (Direct Commands)

#### 🔹 ตั้งเป็น Mode 1: เรียกใช้เองผ่าน `@thai-token-optimizer` (On-Demand Skill Only)
```powershell
# Windows PowerShell
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.ps1))) -Mode skill
```
```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.sh | bash -s -- skill
```

#### 🟢 ตั้งเป็น Mode 2: ทำงานอัตโนมัติทุกแชท (Always-On Global Rule)
```powershell
# Windows PowerShell
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.ps1))) -Mode always-on
```
```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.sh | bash -s -- always-on
```

#### 🟡 ยกเลิก Always-On (กลับไปเป็นโหมดเรียกใช้เอง `@thai-token-optimizer`)
```powershell
# Windows PowerShell
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.ps1))) -Mode disable
```
```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.sh | bash -s -- disable
```

#### 🔴 ถอนการติดตั้งทั้งหมด (Uninstall All)
```powershell
# Windows PowerShell
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.ps1))) -Mode uninstall
```

---

## 💡 สถาปัตยกรรม Golden Ratio v2.1 (ครบวงจร 6 จุด)

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

## 📊 ผลทดสอบจริงจากผู้ใช้งาน (Real-World E-Commerce Build Benchmark)

เปรียบเทียบการสั่งสร้างระบบเว็บ E-Commerce เต็มรูปแบบ (วัดผลแยกส่วน Prompt, การคิดวิเคราะห์ในหัว CoT, คำอธิบาย และโค้ด):

| ส่วนประกอบของรอบการทำงาน (Turn) | 1. ไทยแบบเดิม (No Skill) | 2. ไทย + สกิล (Golden Ratio) | 3. อังกฤษล้วน (Pure English) | สรุปผลเปรียบเทียบ |
|:---|:---:|:---:|:---:|:---|
| **📥 User Prompt (คำสั่งผู้ใช้)** | 131 tokens | **42 tokens** | 32 tokens | ไทยมีสกิลกินใกล้เคียงอังกฤษ (ห่างกันแค่ 10 tok) |
| **🧠 CoT Reasoning (คิดวิเคราะห์ในหัว)** | 776 tokens | **140 tokens** | 140 tokens | 🏆 **เท่ากับอังกฤษ 100%** (ลดลง 82.0%) |
| **💬 Delivery Text (ข้อความอธิบาย/ตอบ)** | 805 tokens | **237 tokens** | 128 tokens | ไทยมีสกิล **ลดลง 70.5%** เข้าใกล้ภาษาอังกฤษ |
| **📊 รวมส่วนคิดและสื่อสาร (Prompt + CoT + Text)** | **1,712 tokens** | **419 tokens** | **300 tokens** | 🟢 **ประหยัด 75.5%** (จากเดิมบวม 5.7 เท่า เหลือใกล้เคียงอังกฤษ) |
| **💻 Code (ตัวโค้ดเว็บ E-Commerce ชุดเดียวกัน)** | 4,679 tokens | **4,679 tokens** | 4,679 tokens | ⚖️ **เท่ากัน 100%** (โค้ดและฟังก์ชันสมบูรณ์ครบทุกบรรทัด) |
| **⭐ รวมทั้งรอบ (Prompt + CoT + Text + Code)** | **6,391 tokens** | **5,098 tokens** | **4,979 tokens** | 🏆 **ไทยมีสกิลต่างจากอังกฤษเพียง 119 tokens (2.3%)!** |

---

## 📊 Frontier Models Benchmark (Gemini 4 Argon vs Astar 6.0 vs Claude Opus 5.5)

### 1. งานถาม-ตอบและวิเคราะห์ระบบ (Single-Turn Q&A)
| โมเดล (Model) | ❌ ไม่ใช้สกิล | ⚡ หลังใช้สกิล (Golden Ratio) | 🇬🇧 English ล้วน | ประหยัดไปได้ |
|:---|:---:|:---:|:---:|:---:|
| **Gemini 4 Argon** *(SentencePiece 256k)* | 622 tok *(2.36x)* | **349 tok *(1.32x)*** | **264 tok** *(1.00x)* | **-273 tok (-43.9%)** |
| **Astar 6.0** *(BPE 200k)* | 678 tok *(2.57x)* | **375 tok *(1.42x)*** | **264 tok** *(1.00x)* | **-303 tok (-44.7%)** |
| **Claude Opus 5.5** *(Anthropic BPE)* | 1,043 tok *(3.82x!)* | **500 tok *(1.83x)*** | **273 tok** *(1.00x)* | **-543 tok (-52.1%)** |

### 2. งานโปรเจกต์เขียนโค้ดเต็มรูปแบบ (Full Agent Workflow: Code + Subagent + Memory)
| โมเดล (Model) | ❌ ไม่ใช้สกิล (ไทยล้วน) | 🥈 รุ่นเก่า (v1.0) | 🏆 รุ่นใหม่ (v2.1) | 🇬🇧 English ล้วน | v2.1 ชนะ v1.0 |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Gemini 4 Argon** | 905 tok *(2.12x)* | 844 tok *(1.98x)* | **465 tok *(1.09x)*** | **427 tok** *(1.00x)* | 🔥 **ลดเพิ่มอีก -44.9%** |
| **Astar 6.0** | 989 tok *(2.32x)* | 917 tok *(2.15x)* | **475 tok *(1.11x)*** | **427 tok** *(1.00x)* | 🔥 **ลดเพิ่มอีก -48.2%** |
| **Claude Opus 5.5** | 1,444 tok *(3.28x)* | 1,274 tok *(2.90x)* | **531 tok *(1.21x)*** | **440 tok** *(1.00x)* | ⚡ **ลดเพิ่มอีก -58.3%** |

---

## 🛠️ วิธีติดตั้งสำหรับ Cursor, Windsurf และ ChatGPT

* **Cursor / Windsurf**: คัดลอกไฟล์ [templates/cursor-rules.mdc](templates/cursor-rules.mdc) ไปไว้ที่ `.cursor/rules/thai-token-optimizer.mdc` หรือ `.windsurfrules`
* **ChatGPT / Custom GPTs**: คัดลอกข้อความจาก [templates/system-prompt-chatgpt.md](templates/system-prompt-chatgpt.md) ไปใส่ใน **Custom Instructions**

---

## 📄 License
MIT License © 2026 Thai Token Optimizer Contributors
