import sys
import tiktoken

sys.stdout.reconfigure(encoding='utf-8')
enc = tiktoken.get_encoding("o200k_base")

test_modes = [
    {
        "mode_name": "Mode 1: Ultra-Dense (งาน Dev & System)",
        "scenario": "ผู้ใช้แจ้งปัญหา Database Connection Timeout ในช่วงโหลดหนัก",
        "verbose_thai_output": (
            "สวัสดีครับคุณลูกค้า ทางเราได้รับทราบปัญหาเรื่องที่เซิร์ฟเวอร์ฐานข้อมูลเกิดอาการหมดเวลาในการเชื่อมต่อแล้วนะครับ "
            "จากการตรวจสอบเบื้องต้นเป็นเพราะว่าขนาดของคอนเนกชันพูลในไฟล์คอนฟิกูเรชันถูกตั้งไว้ต่ำเกินไปครับ "
            "รบกวนช่วยเข้าไปทำการปรับเพิ่มขนาดพูลในไฟล์และทำการรีสตาร์ตเซอร์วิสใหม่อีกครั้งหนึ่งด้วยนะครับผม ขอบคุณครับ"
        ),
        "unified_internal_thought_en": (
            "Diagnosed DB timeout. Root cause: connection pool exhausted. Action: bump pool size in config, restart service."
        ),
        "unified_thai_output": (
            "สาเหตุ DB Timeout: Connection Pool ใน config ต่ำเกินไป\n"
            "วิธีแก้: ปรับเพิ่ม pool_size ใน config -> restart service"
        )
    },
    {
        "mode_name": "Mode 2: Polite-Hybrid (งานตอบลูกค้า / องค์กร)",
        "scenario": "ลูกค้าสอบถามเรื่องระบบตัดเงินล่าช้าและขอตรวจสอบสถานะ",
        "verbose_thai_output": (
            "กราบเรียนคุณลูกค้าที่เคารพ ทางทีมงานขออนุญาตเรียนชี้แจงให้ทราบเกี่ยวกับกรณีที่ท่านได้สอบถามเรื่องการตัดยอดเงินล่าช้าเข้ามานั้น "
            "ทางเราได้ทำการตรวจสอบกับทางธนาคารคู่ค้าเรียบร้อยแล้วนะครับ และพบว่าขณะนี้ระบบเครือข่ายของธนาคารกำลังอยู่ในระหว่างการปรับปรุงระบบครับ "
            "ทางเราต้องกราบขออภัยในความไม่สะดวกเป็นอย่างยิ่งครับผม"
        ),
        "unified_internal_thought_en": (
            "Customer query on payment delay. Bank network maintenance confirmed. Inform politely with estimated resolution."
        ),
        "unified_thai_output": (
            "สวัสดีครับคุณลูกค้า ทางเราตรวจสอบกับธนาคารคู่ค้าแล้ว พบว่าระบบตัดเงินล่าช้าเนื่องจากธนาคารกำลังปิดปรับปรุงระบบชั่วคราวครับ "
            "ยอดเงินจะเข้าบัญชีโดยอัตโนมัติทันทีที่ธนาคารเสร็จสิ้นการปรับปรุง ทางทีมงานขออภัยในความไม่สะดวกด้วยครับ"
        )
    },
    {
        "mode_name": "Mode 3: Creative-Bypass (งานแต่งเรื่อง / นิยาย)",
        "scenario": "ผู้ใช้สั่ง: แต่งบรรยายฉากเมืองหลวงยุคดิสโทเปียตอนฝนตก",
        "verbose_thai_output": (
            "สายฝนกรดที่ตกลงมาอย่างหนักหน่วงได้กัดกร่อนซากตึกระฟ้าเก่าแก่ในเงามืดของเมืองใหญ่ที่ไร้ซึ่งแสงสว่างแห่งความหวัง "
            "ท่ามกลางแสงไฟนีออนสีแดงหม่นที่ส่องสะท้อนกับแอ่งน้ำคราบน้ํามันบนถนนลาดยางอันแตกร้าว "
            "ทุกคนต่างเร่งสาวเท้าก้มหน้าหลบสายตาจากโดรนสอดแนมที่ลอยตรวจตราอย่างเงียบเชียบในอากาศ"
        ),
        "unified_internal_thought_en": (
            "Cyberpunk dystopian rain scene: acid rain, neon reflections, surveillance drones, desolate atmosphere."
        ),
        "unified_thai_output": (
            "สายฝนกรดที่ตกลงมาอย่างหนักหน่วงได้กัดกร่อนซากตึกระฟ้าเก่าแก่ในเงามืดของเมืองใหญ่ที่ไร้ซึ่งแสงสว่างแห่งความหวัง "
            "ท่ามกลางแสงไฟนีออนสีแดงหม่นที่ส่องสะท้อนกับแอ่งน้ำคราบน้ํามันบนถนนลาดยางอันแตกร้าว "
            "ทุกคนต่างเร่งสาวเท้าก้มหน้าหลบสายตาจากโดรนสอดแนมที่ลอยตรวจตราอย่างเงียบเชียบในอากาศ"
        )
    }
]

print("=" * 95)
print(" LIVE TEST: UNIFIED TRI-PILLAR ARCHITECTURE (วัดผลจริงด้วย Tokenizer GPT-4o)")
print("=" * 95)

for t in test_modes:
    print(f"\n▶ [{t['mode_name']}]")
    print(f"  สถานการณ์: {t['scenario']}")
    
    # 1. Output Tokens comparison
    tok_verbose_out = len(enc.encode(t["verbose_thai_output"]))
    tok_unified_out = len(enc.encode(t["unified_thai_output"]))
    
    # 2. Internal Thinking comparison (If thinking was Thai verbose vs English dense)
    # Simulate thinking in Thai vs Thinking in English
    tok_thought_th = len(enc.encode("วิเคราะห์สาเหตุและขั้นตอน: " + t["verbose_thai_output"]))
    tok_thought_en = len(enc.encode(t["unified_internal_thought_en"]))
    
    # Total Turn Tokens = Internal Thinking + User Output
    total_legacy = tok_thought_th + tok_verbose_out
    total_unified = tok_thought_en + tok_unified_out
    savings_pct = ((total_legacy - total_unified) / total_legacy) * 100
    
    print("-" * 95)
    print(f"  [Output เดิมแบบไทยเวิ่นเว้อ] : {tok_verbose_out:>3} tokens")
    print(f"  [Output ระบบ Unified ใหม่]   : {tok_unified_out:>3} tokens")
    print(f"  [Thinking ในหัว (ไทย vs Eng)]: {tok_thought_th:>3} tok (TH) ➔ {tok_thought_en:>3} tok (ENG) [ลดหลังบ้าน -{tok_thought_th - tok_thought_en} tok]")
    print(f"  ---------------------------------------------------------------------------------")
    print(f"  ★ รวมทั้ง Turn (คิด + ตอบ)   : เดิม {total_legacy} tokens ➔ เหลือ {total_unified} tokens (ประหยัดสุทธิ {savings_pct:.1f}%)")
    print(f"  ข้อความที่แสดงผลให้ผู้ใช้:\n  \"{t['unified_thai_output'].replace(chr(10), ' ')}\"")

print("\n" + "=" * 95)
