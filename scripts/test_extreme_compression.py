import sys
import tiktoken

sys.stdout.reconfigure(encoding='utf-8')
enc = tiktoken.get_encoding("o200k_base")

tests = [
    ("1. English Full Prose (ต้นฉบับอังกฤษร้อยแก้ว)", "If the database connection times out, increase the connection pool size in the configuration file and then restart the service."),
    ("2. Thai Full Prose (ต้นฉบับไทยร้อยแก้ว)", "หากระบบฐานข้อมูลเกิดการหมดเวลาในการเชื่อมต่อ ให้ทำการเพิ่มขนาดของคอนเนกชันพูลในไฟล์คอนฟิกูเรชันแล้วทำการรีสตาร์ตเซอร์วิสครับ"),
    ("3. Level 1: Optimized Thai (โหมดปัจจุบัน)", "สาเหตุ DB Timeout: Connection Pool ใน config ต่ำเกินไป วิธีแก้: ปรับเพิ่ม pool_size ใน config -> restart service"),
    ("4. Level 2: Micro-Syntax (สัญกรณ์ตรรกะ)", "DB Timeout: เพิ่ม cfg.pool_size => restart service"),
    ("5. Level 3: Extreme Nanocode (ขีดสุด)", "DB Timeout: cfg.pool++ => restart svc")
]

print("=" * 95)
print(" EXTREME TOKEN COMPRESSION: ไปได้ต่ำสุดแค่ไหน?")
print("=" * 95)
for name, text in tests:
    tokens = len(enc.encode(text))
    print(f"{name:<45} : {tokens:>2} tokens | \"{text}\"")
print("=" * 95)
