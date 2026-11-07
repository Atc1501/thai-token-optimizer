import sys
import tiktoken

sys.stdout.reconfigure(encoding='utf-8')
enc = tiktoken.get_encoding("o200k_base")

head_to_head_cases = [
    {
        "case_name": "Case 1: Dev / System (DB Connection Timeout)",
        "eng": {
            "thought": "Diagnosed DB timeout. Root cause: connection pool exhausted. Action: bump pool size in config, restart service.",
            "output": "Cause: DB Connection Pool is too low in config.\nFix: Increase pool_size in config -> restart service."
        },
        "thai_legacy": {
            "thought": "วิเคราะห์สาเหตุและขั้นตอน: เซิร์ฟเวอร์ฐานข้อมูลหมดเวลาเชื่อมต่อเพราะขนาดของพูลในคอนฟิกต่ำไป ต้องแก้คอนฟิกและรีสตาร์ต",
            "output": "สวัสดีครับ จากการตรวจสอบพบว่าขนาดของคอนเนกชันพูลในไฟล์คอนฟิกูเรชันถูกตั้งไว้ต่ำเกินไปครับ รบกวนช่วยเข้าไปทำการปรับเพิ่มขนาดพูลในไฟล์และทำการรีสตาร์ตเซอร์วิสใหม่อีกครั้งหนึ่งด้วยนะครับ ขอบคุณครับ"
        },
        "thai_unified": {
            "thought": "Diagnosed DB timeout. Root cause: connection pool exhausted. Action: bump pool size in config, restart service.",
            "output": "สาเหตุ DB Timeout: Connection Pool ใน config ต่ำเกินไป\nวิธีแก้: ปรับเพิ่ม pool_size ใน config -> restart service"
        }
    },
    {
        "case_name": "Case 2: Customer Support (Payment Delay Investigation)",
        "eng": {
            "thought": "Customer query on payment delay. Bank network maintenance confirmed. Inform politely with estimated resolution.",
            "output": "Dear customer, we checked with our partner bank and confirmed that payments are delayed due to scheduled maintenance. Funds will credit automatically once completed. We apologize for the inconvenience."
        },
        "thai_legacy": {
            "thought": "วิเคราะห์และเตรียมตอบลูกค้า: ลูกค้าสอบถามเรื่องเงินล่าช้า ตรวจสอบกับธนาคารแล้วพบว่าปิดปรับปรุง ต้องแจ้งลูกค้าอย่างสุภาพและขออภัย",
            "output": "กราบเรียนคุณลูกค้าที่เคารพ ทางทีมงานขออนุญาตเรียนชี้แจงให้ทราบว่า ทางเราได้ตรวจสอบกับทางธนาคารคู่ค้าแล้วและพบว่าขณะนี้ระบบของธนาคารกำลังปิดปรับปรุงระบบครับ ยอดเงินจะเข้าอัตโนมัติเมื่อเสร็จสิ้น ทางเราต้องกราบขออภัยในความไม่สะดวกเป็นอย่างยิ่งครับ"
        },
        "thai_unified": {
            "thought": "Customer query on payment delay. Bank network maintenance confirmed. Inform politely with estimated resolution.",
            "output": "สวัสดีครับคุณลูกค้า ทางเราตรวจสอบกับธนาคารคู่ค้าแล้ว พบว่าระบบตัดเงินล่าช้าเนื่องจากธนาคารกำลังปิดปรับปรุงระบบชั่วคราวครับ ยอดเงินจะเข้าบัญชีอัตโนมัติทันทีที่เสร็จสิ้น ขออภัยในความไม่สะดวกด้วยครับ"
        }
    },
    {
        "case_name": "Case 3: Creative / Dystopian Cyberpunk Rain Scene",
        "eng": {
            "thought": "Cyberpunk dystopian rain scene: acid rain, neon reflections, surveillance drones, desolate atmosphere.",
            "output": "Heavy acid rain corroded the crumbling skyscrapers under the gloom of a hopeless metropolis. Beneath the dull red glow of neon lights reflecting in oily puddles on cracked asphalt, people hurried with lowered heads, dodging the gaze of surveillance drones humming silently above."
        },
        "thai_legacy": {
            "thought": "วางโครงเรื่องและบรรยายฉากไซเบอร์พังก์ดิสโทเปีย ฝนกรด แสงไฟนีออน แอ่งน้ำน้ำมัน โดรนสอดแนมในอากาศ ความสิ้นหวังของผู้คน",
            "output": "สายฝนกรดที่ตกลงมาอย่างหนักหน่วงได้กัดกร่อนซากตึกระฟ้าเก่าแก่ในเงามืดของเมืองใหญ่ที่ไร้ซึ่งแสงสว่างแห่งความหวัง ท่ามกลางแสงไฟนีออนสีแดงหม่นที่ส่องสะท้อนกับแอ่งน้ำคราบน้ํามันบนถนนลาดยางอันแตกร้าว ทุกคนต่างเร่งสาวเท้าก้มหน้าหลบสายตาจากโดรนสอดแนมที่ลอยตรวจตราอย่างเงียบเชียบในอากาศ"
        },
        "thai_unified": {
            "thought": "Cyberpunk dystopian rain scene: acid rain, neon reflections, surveillance drones, desolate atmosphere.",
            "output": "สายฝนกรดที่ตกลงมาอย่างหนักหน่วงได้กัดกร่อนซากตึกระฟ้าเก่าแก่ในเงามืดของเมืองใหญ่ที่ไร้ซึ่งแสงสว่างแห่งความหวัง ท่ามกลางแสงไฟนีออนสีแดงหม่นที่ส่องสะท้อนกับแอ่งน้ำคราบน้ํามันบนถนนลาดยางอันแตกร้าว ทุกคนต่างเร่งสาวเท้าก้มหน้าหลบสายตาจากโดรนสอดแนมที่ลอยตรวจตราอย่างเงียบเชียบในอากาศ"
        }
    }
]

print("=" * 105)
print(" HEAD-TO-HEAD BATTLE: ENGLISH vs THAI LEGACY vs THAI OPTIMIZED (GPT-4o o200k_base)")
print("=" * 105)

for c in head_to_head_cases:
    print(f"\n▶ [{c['case_name']}]")
    
    # English tokens
    e_th = len(enc.encode(c["eng"]["thought"]))
    e_out = len(enc.encode(c["eng"]["output"]))
    e_total = e_th + e_out
    
    # Thai legacy tokens
    tl_th = len(enc.encode(c["thai_legacy"]["thought"]))
    tl_out = len(enc.encode(c["thai_legacy"]["output"]))
    tl_total = tl_th + tl_out
    
    # Thai unified tokens
    tu_th = len(enc.encode(c["thai_unified"]["thought"]))
    tu_out = len(enc.encode(c["thai_unified"]["output"]))
    tu_total = tu_th + tu_out
    
    print(f"  1. 🇬🇧 English ล้วน           : คิด {e_th:>2} + ตอบ {e_out:>3}  =  {e_total:>3} tokens  (มาตรฐานฝรั่ง)")
    print(f"  2. 🇹🇭 ไทยปกติ (Legacy)       : คิด {tl_th:>2} + ตอบ {tl_out:>3}  =  {tl_total:>3} tokens  (กินบวม x{tl_total/e_total:.1f})")
    print(f"  3. ⚡ ไทยประหยัด (Unified)   : คิด {tu_th:>2} + ตอบ {tu_out:>3}  =  {tu_total:>3} tokens  (ลดจากไทยเดิม {((tl_total - tu_total)/tl_total)*100:.1f}%)")
    
    ratio_to_eng = tu_total / e_total
    if tu_total <= e_total:
        verdict = f"🎉 น้อยกว่าหรือเท่ากับอังกฤษ! ({tu_total} <= {e_total} tokens)"
    else:
        verdict = f"✨ ใกล้เคียงอังกฤษมาก (ต่างกันแค่ {tu_total - e_total} tokens, Ratio: {ratio_to_eng:.2f}x จากเดิม {tl_total/e_total:.2f}x)"
    print(f"     ➔ สรุปเทียบกับ English : {verdict}")

print("\n" + "=" * 105)
