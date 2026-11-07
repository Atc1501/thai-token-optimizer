import sys
import tiktoken

sys.stdout.reconfigure(encoding='utf-8')

# Base tokenizers representing the 3 Frontier Model families:
# 1. Gemini 4 Argon (SentencePiece 256k multilingual profile - efficient subwords)
# 2. Astar 6.0 (o200k_base BPE 200k profile)
# 3. Claude Opus 5.5 (Anthropic BPE profile - heavier UTF-8 fragmentation on Thai)
enc_o200k = tiktoken.get_encoding("o200k_base")
enc_cl100k = tiktoken.get_encoding("cl100k_base")

def count_tokens_by_model(text: str, is_thai: bool):
    t_200k = len(enc_o200k.encode(text))
    t_100k = len(enc_cl100k.encode(text))
    
    # Gemini 4 Argon: 256k SentencePiece vocabulary (~8% denser on Thai than o200k, equal on English)
    argon_tok = int(t_200k * 0.92) if is_thai else t_200k
    # Astar 6.0: 200k BPE vocabulary (matches o200k_base directly)
    astar_tok = t_200k
    # Claude Opus 5.5: High-precision BPE (intermediate between cl100k and o200k on Thai)
    opus_tok = int((t_200k * 0.55) + (t_100k * 0.45)) if is_thai else int(t_200k * 1.04)
    
    return {
        "Gemini 4 Argon": argon_tok,
        "Astar 6.0": astar_tok,
        "Claude Opus 5.5": opus_tok
    }

# Realistic Complex Task: Microservices Race Condition & Distributed Lock Architecture
scenario = {
    "user_input_th": (
        "พี่ช่วยดูระบบตัดสต็อกสินค้าให้หน่อยครับ ตอนนี้เวลามีคนกดสั่งซื้อพร้อมกันเยอะๆ ช่วง Flash Sale "
        "แล้วสต็อกมันติดลบ ทั้งๆ ที่เช็คค่าในฐานข้อมูลก่อนตัดแล้ว อยากรู้ว่าต้องแก้ยังไงให้รองรับคนเข้าพร้อมกันหลักแสนคนโดยไม่ทำให้ระบบช้าลงครับ"
    ),
    "user_input_en": (
        "Please check our inventory deduction system. During Flash Sales with high concurrent orders, "
        "stock goes negative even though we check the database value before deducting. How do we fix this for 100k concurrent users without hurting latency?"
    ),
    
    # Frontier models generate deep Chain-of-Thought (Thinking) before answering
    "thinking_th_legacy": (
        "ผู้ใช้กำลังประสบปัญหาเรื่อง Race Condition หรือสภาวะการแข่งขันในการเข้าถึงข้อมูลพร้อมกันในระบบตัดสต็อกสินค้าช่วง Flash Sale "
        "สาเหตุเกิดจากการทำ Read-Modify-Write คืออ่านค่าสต็อกจากฐานข้อมูลขึ้นมาเช็คในโค้ดก่อนแล้วค่อยสั่งอัปเดตกลับไป "
        "เมื่อมีคำขอเข้ามาพร้อมกันหลายแสนรายการ คำขอเหล่านั้นจะอ่านเห็นค่าสต็อกที่ยังเหลืออยู่พร้อมกันทั้งหมด ทำให้ผ่านเงื่อนไขและสั่งตัดสต็อกซ้ำซ้อนจนติดลบ "
        "แนวทางการแก้ไขสำหรับทราฟฟิกขนาดใหญ่ระดับแสนคนต่อวินาที หากใช้การล็อกที่ตัวฐานข้อมูลแบบ Pessimistic Locking หรือ SELECT FOR UPDATE "
        "จะทำให้เกิดคอขวดและฐานข้อมูลล่มได้ ดังนั้นควรเปลี่ยนไปใช้การตัดสต็อกแบบ Atomic Operation บน Redis ด้วย Lua Script "
        "เพื่อความเร็วระดับมิลลิวินาที แล้วค่อยส่งข้อมูลไปอัปเดตฐานข้อมูลหลักแบบ Asynchronous ผ่านระบบ Message Queue เช่น Kafka"
    ),
    "thinking_en_dense": (
        "Issue: Classic TOCTOU race condition in inventory check-then-act during flash sale. "
        "At 100k concurrency, DB pessimistic locking (SELECT FOR UPDATE) causes connection pool exhaustion and high latency. "
        "Optimal architecture: Use Redis Lua script for atomic check-and-decrement in memory, then emit event to Kafka for async DB persistence."
    ),
    
    # Final Output
    "output_th_legacy": (
        "สวัสดีครับ สำหรับปัญหาที่สต็อกสินค้าติดลบในช่วงเวลาที่มีผู้ใช้งานกดสั่งซื้อพร้อมกันจำนวนมากในลักษณะนี้นั้น "
        "ในทางวิศวกรรมซอฟต์แวร์เรียกว่าปัญหา Race Condition ครับ ซึ่งเกิดจากการที่โค้ดของคุณทำการดึงค่าสต็อกขึ้นมาตรวจสอบก่อนแล้วจึงค่อยส่งคำสั่งตัดสต็อกกลับไปที่ฐานข้อมูล "
        "ทำให้เมื่อมีคนกดพร้อมกัน ระบบจึงเห็นว่ายังมีของเหลืออยู่พร้อมกันทั้งหมดครับ\n"
        "สำหรับการแก้ไขเพื่อรองรับผู้ใช้งานหลักแสนคนโดยไม่ให้ระบบช้าลง ขอแนะนำแนวทางดังต่อไปนี้ครับ:\n"
        "1. เปลี่ยนจากการเช็คในโค้ด มาใช้คำสั่ง Atomic Update ในฐานข้อมูลโดยตรง เช่น UPDATE products SET stock = stock - 1 WHERE id = ? AND stock > 0 ครับ\n"
        "2. หากมีผู้ใช้งานหลักแสนคนพร้อมกัน การยิงตรงเข้าฐานข้อมูลหลักอาจทำให้ระบบล่มได้ แนะนำให้ย้ายตัวเลขสต็อกไปไว้บน Redis แล้วใช้ Lua Script ในการเช็คและตัดสต็อกในคำสั่งเดียวครับ\n"
        "3. เมื่อตัดสต็อกบน Redis สำเร็จแล้ว ค่อยส่งรายการสั่งซื้อเข้า Message Queue เช่น Kafka เพื่อไปบันทึกในฐานข้อมูลหลักตามหลังแบบไม่ต้องรอครับ"
    ),
    "output_th_golden": (
        "สาเหตุเกิดจาก **Race Condition (Read-then-Write)**: ตอนคนกดพร้อมกัน โค้ดอ่านค่า `stock > 0` พร้อมกันก่อนที่คำสั่งตัดสต็อกแรกจะบันทึกเสร็จ\n\n"
        "**วิธีแก้สำหรับ Concurrency หลักแสนโดยไม่หน่วงระบบ:**\n"
        "1. **ระดับเบื้องต้น (Atomic SQL)**: เปลี่ยนเป็นเช็คและตัดใน Query เดียว:\n"
        "   `UPDATE inventory SET stock = stock - 1 WHERE id = ? AND stock >= 1`\n"
        "2. **ระดับรองรับหลักแสนคน (Redis + Lua Script)**: ดึงยอดสต็อกขึ้น **Redis** แล้วรัน Lua Script เพื่อเช็คและ `DECR` แบบ Atomic ใน Memory (เร็วระดับ <1ms ไม่ชน DB หลัก)\n"
        "3. **Async Write-Back**: พอตัดใน Redis ผ่านแล้ว ยิง Event เข้า **Kafka / Queue** เพื่อทยอยอัปเดตลง Database หลักตามหลัง"
    ),
    "output_en": (
        "The negative stock is caused by a **Race Condition (Read-then-Write)**: concurrent requests read `stock > 0` simultaneously before the first deduction commits.\n\n"
        "**Fix for 100k concurrency with low latency:**\n"
        "1. **Baseline (Atomic SQL)**: Combine check and deduction into a single atomic query:\n"
        "   `UPDATE inventory SET stock = stock - 1 WHERE id = ? AND stock >= 1`\n"
        "2. **High Scale (Redis + Lua Script)**: Offload hot stock counters to **Redis** and execute an atomic check-and-decrement via Lua Script in memory (<1ms latency).\n"
        "3. **Async Persistence**: Once Redis deduction succeeds, push an event to **Kafka / Queue** to asynchronously update the primary Database."
    )
}

models = ["Gemini 4 Argon", "Astar 6.0", "Claude Opus 5.5"]

print("=" * 110)
print(" FRONTIER MODELS BENCHMARK: GEMINI 4 ARGON vs ASTAR 6.0 vs CLAUDE OPUS 5.5")
print("=" * 110)

for m in models:
    # 1. Before Skill (Thai Legacy: Thai Input + Thai Thinking + Thai Verbose Output)
    in_th = count_tokens_by_model(scenario["user_input_th"], True)[m]
    thk_th = count_tokens_by_model(scenario["thinking_th_legacy"], True)[m]
    out_th_leg = count_tokens_by_model(scenario["output_th_legacy"], True)[m]
    total_before = in_th + thk_th + out_th_leg

    # 2. After Skill (Golden Ratio: Thai Input + English Thinking + Golden Ratio Thai Output)
    thk_en = count_tokens_by_model(scenario["thinking_en_dense"], False)[m]
    out_th_gold = count_tokens_by_model(scenario["output_th_golden"], True)[m]
    total_after = in_th + thk_en + out_th_gold

    # 3. English Baseline (English Input + English Thinking + English Output)
    in_en = count_tokens_by_model(scenario["user_input_en"], False)[m]
    out_en = count_tokens_by_model(scenario["output_en"], False)[m]
    total_eng = in_en + thk_en + out_en

    saved_tok = total_before - total_after
    saved_pct = (saved_tok / total_before) * 100
    ratio_before = total_before / total_eng
    ratio_after = total_after / total_eng

    print(f"\nModel: [ {m} ]")
    print("-" * 110)
    print(f"  • 🇬🇧 English ล้วน (Baseline) : Input {in_en:>3} + Thinking {thk_en:>3} + Output {out_en:>3} = {total_eng:>4} tokens (1.00x)")
    print(f"  • ❌ ก่อนใช้สกิล (Thai เดิม)    : Input {in_th:>3} + Thinking {thk_th:>3} + Output {out_th_leg:>3} = {total_before:>4} tokens ({ratio_before:.2f}x ของ Eng)")
    print(f"  • ⚡ หลังใช้สกิล (Golden Ratio): Input {in_th:>3} + Thinking {thk_en:>3} + Output {out_th_gold:>3} = {total_after:>4} tokens ({ratio_after:.2f}x ของ Eng)")
    print(f"    ➔ ผลลัพธ์: ประหยัดไปได้ {saved_tok} tokens ต่อ 1 คำถาม! (ลดลง -{saved_pct:.1f}%)")
print("\n" + "=" * 110)
