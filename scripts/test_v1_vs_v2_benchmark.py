import sys
import tiktoken

sys.stdout.reconfigure(encoding='utf-8')

enc_o200k = tiktoken.get_encoding("o200k_base")
enc_cl100k = tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str, is_thai: bool, model: str) -> int:
    t_200k = len(enc_o200k.encode(text))
    t_100k = len(enc_cl100k.encode(text))
    if model == "Gemini 4 Argon":
        return int(t_200k * 0.92) if is_thai else t_200k
    elif model == "Astar 6.0":
        return t_200k
    elif model == "Claude Opus 5.5":
        return int((t_200k * 0.55) + (t_100k * 0.45)) if is_thai else int(t_200k * 1.04)
    return t_200k

# Realistic Full Agent Coding Workflow (2-Turn Feature Build + Subagent + Code Readback + Memory)
workflow = {
    # 1. User Input
    "input_th": "ช่วยสร้างระบบจำกัดการยิง API (Rate Limiter) ด้วย Redis สำหรับป้องกันคนสแปมล็อกอินให้หน่อยครับ ถ้าเกิน 5 ครั้งใน 1 นาทีให้บล็อกทันที",
    "input_en": "Build a Redis-based API Rate Limiter to prevent login spam. Block immediately if requests exceed 5 per minute.",

    # 2. Internal Thinking (Main Agent)
    "thinking_th": (
        "ผู้ใช้ต้องการสร้างระบบ Rate Limiter ด้วย Redis เพื่อป้องกันการสแปมล็อกอินเกิน 5 ครั้งต่อนาที "
        "ต้องสั่งให้ Subagent ไปตรวจสอบโครงสร้างไฟล์ Auth เดิมก่อน แล้วจึงเขียนโค้ด Middleware สำหรับเช็คจำนวนครั้งด้วยคำสั่ง INCR และ EXPIRE "
        "พร้อมทั้งบันทึกสถานะงานลงในไฟล์ความจำของโปรเจกต์"
    ),
    "thinking_en": (
        "Need Redis rate limiter for login endpoint (max 5 req/min). "
        "Step 1: Dispatch subagent to inspect auth middleware. Step 2: Implement Redis INCR+EXPIRE middleware. Step 3: Log state to memory."
    ),

    # 3. Subagent Prompt + Subagent Report (Brain <-> Worker communication)
    "subagent_th": (
        "คำสั่งถึงลูกน้อง: ช่วยตรวจสอบไฟล์ระบบล็อกอินในโปรเจกต์นี้หน่อยว่าใช้เฟรมเวิร์กอะไรและมีการเชื่อมต่อ Redis ไว้ที่ไฟล์ไหนครับ\n"
        "รายงานจากลูกน้อง: ตรวจสอบเรียบร้อยแล้วครับ โปรเจกต์นี้ใช้ Express.js และมีการตั้งค่าการเชื่อมต่อตัวแปรฐานข้อมูล Redis ไว้ที่ไฟล์ src/lib/redis.ts ครับ"
    ),
    "subagent_en": (
        "Task: Inspect login route framework and locate existing Redis client.\n"
        "Report: Express.js route at src/routes/auth.ts; exported Redis client at src/lib/redis.ts."
    ),

    # 4. Code Generated + Re-read on Turn 2 (Counted x2: once when written, once when re-read in next turn context!)
    "code_th_comments": (
        "// ฟังก์ชันตัวกลางสำหรับตรวจสอบและจำกัดจำนวนครั้งในการส่งคำขอเข้าสู่ระบบ\n"
        "// หากผู้ใช้งานส่งคำขอเกิน 5 ครั้งภายในเวลา 1 นาที ระบบจะทำการบล็อกและส่งรหัสข้อผิดพลาด 429 กลับไปทันที\n"
        "export async function loginRateLimiter(req, res, next) {\n"
        "  // ดึงเลขไอพีของผู้ใช้งานมาสร้างเป็นคีย์สำหรับเก็บในฐานข้อมูลเรดิส\n"
        "  const key = `login_limit:${req.ip}`;\n"
        "  const count = await redis.incr(key);\n"
        "  // ถ้าเป็นการกดครั้งแรก ให้ตั้งเวลาหมดอายุไว้ที่ 60 วินาที\n"
        "  if (count === 1) await redis.expire(key, 60);\n"
        "  // ตรวจสอบว่าเกินจำนวนครั้งที่กำหนดไว้หรือไม่\n"
        "  if (count > 5) return res.status(429).json({ error: 'คุณทำรายการเกินจำนวนครั้งที่กำหนด กรุณารอสักครู่' });\n"
        "  next();\n"
        "}"
    ),
    "code_en_comments": (
        "// Rate limit login requests to 5 per 60s window per IP\n"
        "export async function loginRateLimiter(req, res, next) {\n"
        "  const key = `login_limit:${req.ip}`;\n"
        "  const count = await redis.incr(key);\n"
        "  if (count === 1) await redis.expire(key, 60);\n"
        "  if (count > 5) return res.status(429).json({ error: 'คุณทำรายการเกินจำนวนครั้งที่กำหนด กรุณารอสักครู่' });\n"
        "  next();\n"
        "}"
    ),

    # 5. Persistent Memory / Scratchpad (Reloaded across turns)
    "memory_th": (
        "บันทึกสถานะงาน: สร้างไฟล์มิดเดิลแวร์สำหรับจำกัดจำนวนการล็อกอินด้วยเรดิสเรียบร้อยแล้ว "
        "กำหนดโควต้าไว้ที่ 5 ครั้งต่อ 60 วินาที เชื่อมต่อกับไฟล์เรดิสหลักและผูกเข้ากับหน้าล็อกอินเสร็จสมบูรณ์"
    ),
    "memory_en": (
        "State: Added loginRateLimiter middleware (5 req/60s via src/lib/redis.ts) and attached to /login route."
    ),

    # 6. Final User Output
    "output_legacy_th": (
        "สวัสดีครับ ผมได้ทำการตรวจสอบโครงสร้างโปรเจกต์และสร้างระบบจำกัดการยิง API หรือ Rate Limiter ด้วย Redis สำหรับหน้าล็อกอินให้เรียบร้อยแล้วนะครับ "
        "โดยระบบจะทำการนับจำนวนครั้งตามเลข IP ของผู้ใช้งาน หากมีการกดล็อกอินเกิน 5 ครั้งภายในเวลา 1 นาที ระบบจะทำการบล็อกและส่งรหัส 429 กลับไปทันทีครับ"
    ),
    "output_golden_th": (
        "สร้าง Middleware `loginRateLimiter` ผูกกับ `src/lib/redis.ts` เรียบร้อย:\n"
        "- นับจำนวนยิงตาม IP ด้วย `redis.incr` + ตั้งอายุคีย์ `expire(60)`\n"
        "- ถ้าเกิน **5 ครั้ง/นาที** จะตัดจบด้วย HTTP `429` ทันที"
    ),
    "output_en": (
        "Implemented `loginRateLimiter` middleware using `src/lib/redis.ts`:\n"
        "- Tracks requests per IP via `redis.incr` with a `60s` TTL.\n"
        "- Rejects requests exceeding **5/min** with HTTP `429`."
    )
}

models = ["Gemini 4 Argon", "Astar 6.0", "Claude Opus 5.5"]

print("=" * 118)
print(" BENCHMARK: LEGACY THAI vs v1.0 (BASIC GOLDEN RATIO) vs v2.0 (FULL LIFECYCLE) vs ENGLISH")
print("=" * 118)

for m in models:
    # Components
    in_th = count_tokens(workflow["input_th"], True, m)
    in_en = count_tokens(workflow["input_en"], False, m)

    thk_th = count_tokens(workflow["thinking_th"], True, m)
    thk_en = count_tokens(workflow["thinking_en"], False, m)

    sub_th = count_tokens(workflow["subagent_th"], True, m)
    sub_en = count_tokens(workflow["subagent_en"], False, m)

    # Code & Memory are written in Turn 1 and re-read in Turn 2 (x2 context impact)
    code_th = count_tokens(workflow["code_th_comments"], True, m) * 2
    code_en = count_tokens(workflow["code_en_comments"], False, m) * 2

    mem_th = count_tokens(workflow["memory_th"], True, m) * 2
    mem_en = count_tokens(workflow["memory_en"], False, m) * 2

    out_leg_th = count_tokens(workflow["output_legacy_th"], True, m)
    out_gold_th = count_tokens(workflow["output_golden_th"], True, m)
    out_en = count_tokens(workflow["output_en"], False, m)

    # Totals
    # 0. Legacy (All Thai)
    total_legacy = in_th + thk_th + sub_th + code_th + mem_th + out_leg_th
    # 1. v1.0 (Only optimizes Thinking & Output; leaves Code Comments, Subagents, and Memory in Thai)
    total_v1 = in_th + thk_en + sub_th + code_th + mem_th + out_gold_th
    # 2. v2.0 (Optimizes Thinking + Output + Code Comments + Subagents + Memory)
    total_v2 = in_th + thk_en + sub_en + code_en + mem_en + out_gold_th
    # 3. English Baseline
    total_eng = in_en + thk_en + sub_en + code_en + mem_en + out_en

    save_v1_pct = ((total_legacy - total_v1) / total_legacy) * 100
    save_v2_pct = ((total_legacy - total_v2) / total_legacy) * 100
    v2_vs_v1_pct = ((total_v1 - total_v2) / total_v1) * 100

    print(f"\n▶ Model: [ {m} ]")
    print("-" * 118)
    print(f"  0. ❌ ก่อนใช้สกิล (Thai เดิมล้วน) : {total_legacy:>4} tokens  (แพงกว่า Eng {total_legacy/total_eng:.2f}x)")
    print(f"  1. 🥈 สกิลรุ่น v1.0 (รุ่นเก่า)     : {total_v1:>4} tokens  (ลดจากเดิม -{save_v1_pct:.1f}% | ยังแพงกว่า Eng {total_v1/total_eng:.2f}x)")
    print(f"  2. 🏆 สกิลรุ่น v2.0 (รุ่นใหม่ล่าสุด): {total_v2:>4} tokens  (ลดจากเดิม -{save_v2_pct:.1f}% | ลดเพิ่มจาก v1 อีก -{v2_vs_v1_pct:.1f}% | {total_v2/total_eng:.2f}x ของ Eng)")
    print(f"  3. 🇬🇧 English ล้วน (Baseline)  : {total_eng:>4} tokens  (1.00x มาตรฐานฝรั่ง)")
    print(f"     ➔ เจาะลึกจุดที่ v2.0 ชนะ v1.0: ประหยัดเพิ่มอีก {total_v1 - total_v2} tokens (จาก Code Comments, Subagents และ Memory)")

print("\n" + "=" * 118)
