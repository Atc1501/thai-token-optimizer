# thai-token-optimizer

ลดการกิน Token ของภาษาไทยใน AI Agents และ LLMs ลง 60–75% ให้ใกล้เคียงกับการใช้ภาษาอังกฤษ โดยไม่ลดทอนความแม่นยำของโมเดลและไม่ต้องใช้ไวยากรณ์ย่อตอนพิมพ์สั่งงาน

---

## ปัญหา

Tokenizer ของโมเดลตระกูล GPT, Claude และ Gemini หั่นตัวอักษรภาษาไทยละเอียดกว่าภาษาอังกฤษ 2.5 ถึง 4 เท่า เมื่อโมเดลใช้ภาษาไทยในการคิดวิเคราะห์ (`<thinking>`), สั่งงาน Subagents หรือเขียนคอมเมนต์ในโค้ด โควต้า Context Window จะเต็มเร็วและตอบช้าลงอย่างมาก

## หลักการทำงาน

1. **English Internal Reasoning**: ใช้ภาษาอังกฤษในกระบวนการคิดวิเคราะห์ (`<thinking>`), การวางแผน และการส่งงานระหว่าง Subagents (ลด Token หลังบ้านลง ~70–82%)
2. **Direct Thai Output**: ตอบกลับผู้ใช้เป็นภาษาไทยที่กระชับ ตรงประเด็น ตัดคำเกริ่นทักทายและไม่ทวนคำถามซ้ำ
3. **Technical Terms**: คงคำศัพท์เทคนิค (`Config`, `Database`, `API`, `Function`) และคอมเมนต์ในโค้ดเป็นภาษาอังกฤษ
4. **Smart Code Economy**: สร้างฟีเจอร์ครบ 100% ในรอบแรก แต่เมื่อสั่งแก้ไขโค้ดในรอบถัดไปจะแก้เฉพาะจุด (Surgical Edit) ไม่พ่นโค้ดทั้งไฟล์ซ้ำ และจำกัดขนาดข้อมูลจำลอง (Mock Data) ไม่ให้บวม

---

## วิธีติดตั้ง

รองรับ Antigravity, Gemini CLI, Claude Code และ Codex

### วิธีที่ 1: คัดลอกไฟล์ `SKILL.md` โดยตรง
โคลนโปรเจกต์ลงเครื่องแล้วคัดลอกไฟล์ `SKILL.md` ไปไว้ในโฟลเดอร์สกิล:

```powershell
git clone https://github.com/Atc1501/thai-token-optimizer.git
cd thai-token-optimizer
.\install.ps1
```

เมื่อรัน `.\install.ps1` จะมีเมนูให้เลือกโหมด:
- `1` **Install Skill Only**: เรียกใช้เฉพาะเมื่อพิมพ์ `@thai-token-optimizer`
- `2` **Enable Global Rule (Always-On)**: เพิ่มกฎลงใน `GEMINI.md` ให้ทำงานอัตโนมัติในทุกแชท
- `3` **Disable Global Rule**: ปิดโหมดอัตโนมัติ กลับไปเป็นโหมดเรียกใช้เอง
- `4` **Uninstall All**: ถอนการติดตั้งทั้งหมด

### วิธีที่ 2: สำหรับโปรแกรมอื่นๆ
- **Cursor / Windsurf**: คัดลอกไฟล์ [`templates/cursor-rules.mdc`](templates/cursor-rules.mdc) ไปไว้ที่ `.cursor/rules/thai-token-optimizer.mdc` หรือ `.windsurfrules`
- **ChatGPT / Gemini AI Studio**: คัดลอกข้อความจาก [`templates/system-prompt-chatgpt.md`](templates/system-prompt-chatgpt.md) ไปวางในช่อง Custom Instructions

---

## ผลการทดสอบ (Benchmark)

ทดสอบจากงานสั่งสร้างเว็บ E-Commerce เต็มรูปแบบ (เปรียบเทียบระหว่างการใช้ภาษาไทยปกติ, การเปิดใช้สกิล และการใช้ภาษาอังกฤษล้วน):

| ส่วนประกอบ (Turn Breakdown) | ไทยปกติ (No Skill) | ไทย + สกิลนี้ | อังกฤษล้วน (English) | ผลลัพธ์ |
| :--- | :---: | :---: | :---: | :--- |
| **User Prompt** | 131 | **42** | 32 | ห่างจากอังกฤษ 10 tokens |
| **Chain-of-Thought (คิดในหัว)** | 776 | **140** | 140 | เท่ากับภาษาอังกฤษ (ลดลง 82.0%) |
| **ข้อความอธิบาย (Delivery Text)** | 805 | **237** | 128 | ลดลง 70.5% |
| **รวมส่วนภาษา (Prompt + CoT + Text)** | **1,712** | **419** | **300** | **ประหยัดลง 75.5%** |
| **Code (HTML/CSS/JS ชุดเดียวกัน)** | 4,679 | **4,679** | 4,679 | โค้ดครบสมบูรณ์เท่ากัน 100% |
| **รวมทั้งหมดต่อรอบ** | **6,391** | **5,098** | **4,979** | **ต่างจากอังกฤษล้วนเพียง 2.3% (119 tokens)** |

---

## โครงสร้างไฟล์

- [`SKILL.md`](SKILL.md) — กฎหลักของสกิล
- [`install.ps1`](install.ps1) / [`install.sh`](install.sh) — สคริปต์คัดลอกไฟล์ในเครื่อง
- [`templates/`](templates/) — กฎสำหรับ Cursor, ChatGPT และ Google AI Studio
- [`scripts/`](scripts/) — สคริปต์ Python สำหรับทดสอบวัดค่า Token ด้วย `tiktoken`

## License

[MIT](LICENSE)
