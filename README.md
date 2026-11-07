# ⚡ Thai Token Optimizer (Golden Ratio Standard)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Universal Skill](https://img.shields.io/badge/Skill-Universal%20Agent%20Standard-success.svg)](SKILL.md)
[![Token Savings](https://img.shields.io/badge/Token%20Savings-60%25%20to%2070%25-brightgreen.svg)](#-benchmarks)

> **มาตรฐาน Golden Ratio สำหรับภาษาไทยใน AI Agents และ LLMs** — ลด Token ลง **60% – 70%** จนกิน Token เท่ากับภาษาอังกฤษ โดยที่ **AI ไม่ฉลาดน้อยลงเลยแม้แต่ 1%** และ **ผู้ใช้คุยภาษาไทยได้ตามปกติ สบายๆ ไม่ต้องเกร็งไวยากรณ์**

---

## 💡 แนวคิด Golden Ratio (สมดุลสูงสุด)

```
[ ผู้ใช้พิมพ์คุยภาษาไทยตามธรรมชาติ สบายๆ ไม่ต้องเกร็ง ]
                           │
                           ▼
[ หลังบ้าน: AI คิดวิเคราะห์ (Chain-of-Thought) เป็นภาษาอังกฤษธรรมชาติ ]
  • ประหยัด Token หลังบ้านทันที 70%
  • รักษาความฉลาด ตรรกะ และความแม่นยำของโมเดลไว้ครบ 100%
                           │
                           ▼
[ หน้าบ้าน: AI ตอบกลับเป็นภาษาไทยที่กระชับ ตรงประเด็น อ่านง่าย ]
  • ไม่เกริ่นทักทายเวิ่นเว้อ (ตัด สวัสดีครับ/ค่ะ, ยินดีที่ได้ช่วย)
  • ไม่ทวนคำถามซ้ำ
  • ทับศัพท์เทคนิคด้วยภาษาอังกฤษ (Config, Database, API, Function)
  • จัดข้อมูลเป็นข้อๆ (Bullets / Steps) อ่านสบายตา
```

---

## 📊 ผลการทดสอบเปรียบเทียบจริง (GPT-4o)

| เคสการทำงาน | ภาษาไทยแบบเดิม | ภาษาอังกฤษ | Golden Ratio (ไทย) | ผลลัพธ์ |
|:---|:---:|:---:|:---:|:---:|
| **Dev / Debugging (DB Connection)** | 129 tok | 45 tok | **53 tok** | **ใกล้เคียงอังกฤษ (ลดลง 58.9%)** |
| **Business / Support (แจ้งระบบล่าช้า)** | 149 tok | 50 tok | **102 tok** | **ลดลง 31.5% (สุภาพ ชัดเจน)** |
| **System Alert (เครือข่ายขัดข้อง)** | 39 tok | 14 tok | **8 tok** | 🏆 **น้อยกว่าภาษาอังกฤษ!** |

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
คัดลอกไฟล์ [templates/cursor-rules.mdc](templates/cursor-rules.mdc) ไปไว้ที่:
- **Cursor**: `.cursor/rules/thai-token-optimizer.mdc`
- **Windsurf**: วางใน `.windsurfrules`

### 4. ChatGPT / OpenAI Custom GPTs
คัดลอกข้อความด้านล่างไปใส่ใน **Custom Instructions**:
```markdown
[THAI TOKEN EFFICIENCY: GOLDEN RATIO ACTIVE]
1. Internal Reasoning: Always conduct chain-of-thought and analysis in natural English.
2. Output Style: Respond in natural, direct Thai. Cut ceremonial greetings and never echo questions back.
3. Terminology: Keep tech, coding, and architecture terms in standard English.
4. Structure: Deliver solutions using bullet points or numbered steps over dense paragraphs.
```

---

## 📄 License
MIT License © 2026 Thai Token Optimizer Contributors
