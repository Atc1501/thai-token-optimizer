import sys
import tiktoken

sys.stdout.reconfigure(encoding='utf-8')
enc = tiktoken.get_encoding("o200k_base")

# Base code (identical logic)
core_code = ("<div class='shop-container'>\n  <header class='navbar'><h1>Shop</h1><button id='cart-btn'>Cart (0)</button></header>\n" * 35) + \
            ("function addToCart(id) { const item = products.find(p => p.id === id); cart.push(item); renderCart(); }\n" * 35)

# Mock data (Thai vs English - 15 items vs 3 items)
mock_th_15 = """const products = [
  { id: 1, name: "หูฟังไร้สายตัดเสียงรบกวนระดับพรีเมียม รุ่น Pro Max", desc: "หูฟังคุณภาพสูงที่มาพร้อมระบบตัดเสียงรบกวนอัจฉริยะ แบตเตอรี่ใช้งานได้ยาวนานต่อเนื่องถึง 30 ชั่วโมงเต็ม", price: 4590 },
  { id: 2, name: "คีย์บอร์ดเมคานิคอลไฟ RGB สำหรับสายเกมมิ่งมืออาชีพ", desc: "สวิตช์แท้ตอบสนองไวแม่นยำทุกการใช้งาน สามารถปรับแต่งโหมดไฟได้มากกว่า 16 ล้านสีตามต้องการ", price: 2890 },
  { id: 3, name: "เมาส์ไร้สายน้ำหนักเบาพิเศษสำหรับทำงานและเล่นเกม", desc: "เซ็นเซอร์ความละเอียดสูงระดับเรือธง ออกแบบตามหลักสรีรศาสตร์ช่วยลดอาการปวดข้อมือเมื่อใช้งานนานๆ", price: 1990 },
""" * 5 + "];\n"

mock_en_15 = """const products = [
  { id: 1, name: "Premium Wireless Noise-Canceling Headphones Pro Max", desc: "High-quality headphones featuring smart active noise cancellation and up to 30 hours of battery life", price: 129 },
  { id: 2, name: "Professional RGB Mechanical Gaming Keyboard", desc: "Authentic mechanical switches with fast response and customizable 16.8M RGB lighting effects", price: 89 },
  { id: 3, name: "Ultra-Lightweight Wireless Ergonomic Gaming Mouse", desc: "Flagship high-precision optical sensor with ergonomic shape to reduce wrist fatigue during long sessions", price: 59 },
""" * 5 + "];\n"

mock_th_3 = """const products = [
  { id: 1, name: "หูฟังไร้สาย Pro", desc: "ตัดเสียงรบกวน แบต 30 ชม.", price: 4590 },
  { id: 2, name: "Mechanical Keyboard RGB", desc: "Hot-swappable switch", price: 2890 },
  { id: 3, name: "Wireless Gaming Mouse", desc: "26K DPI น้ำหนักเบา", price: 1990 },
];\n"""

mock_en_3 = """const products = [
  { id: 1, name: "Wireless Headphones Pro", desc: "ANC, 30h battery", price: 129 },
  { id: 2, name: "Mechanical Keyboard RGB", desc: "Hot-swappable switch", price: 89 },
  { id: 3, name: "Wireless Gaming Mouse", desc: "26K DPI lightweight", price: 59 },
];\n"""

surgical_diff = """// ... existing code ...
#cart-btn { background-color: #10b981; color: #ffffff; }
// ... existing code ...
function applyCoupon(code, total) { return code === 'SAVE10' ? total * 0.9 : total; }
"""

fix_snippet = "function applyCoupon(code = '', total = 0) {\n  return code.trim().toUpperCase() === 'SAVE10' ? total * 0.9 : total;\n}"

raw_err = (
    "Uncaught TypeError: Cannot read properties of undefined (reading 'toUpperCase')\n"
    "    at applyCoupon (app.js:142:23)\n"
    "    at HTMLButtonElement.<anonymous> (app.js:89:12)\n" * 3
)

# Code token counts
c_th_full = len(enc.encode(core_code + mock_th_15))
c_en_full = len(enc.encode(core_code + mock_en_15))
c_th_comp = len(enc.encode(core_code + mock_th_3))
c_en_comp = len(enc.encode(core_code + mock_en_3))
c_diff    = len(enc.encode(surgical_diff))
c_fix     = len(enc.encode(fix_snippet))
c_err     = len(enc.encode(raw_err))

# Turn 1: Prompt + CoT + Text + Code
t1 = {
    "th_legacy": 1712 + c_th_full,
    "en_normal": 300  + c_en_full,
    "th_v21":    419  + c_th_full,
    "th_v22":    419  + c_th_comp,
    "en_opt":    300  + c_en_comp,
}

# Turn 2: Follow-up Edit (Change button color + add coupon)
t2 = {
    "th_legacy": 980 + (c_th_full + 85),
    "en_normal": 190 + (c_en_full + 85),
    "th_v21":    265 + (c_th_full + 85),
    "th_v22":    265 + c_diff,
    "en_opt":    190 + c_diff,
}

# Turn 3: Fix TypeError bug
t3 = {
    "th_legacy": 1150 + c_err + c_th_full,
    "en_normal": 210  + c_err + c_fix,
    "th_v21":    290  + c_err + c_fix,
    "th_v22":    210  + c_fix,
    "en_opt":    145  + c_fix,
}

totals = {k: t1[k] + t2[k] + t3[k] for k in t1}

print("=" * 120)
print(" UNBIASED HEAD-TO-HEAD: THAI LEGACY vs NORMAL ENG vs THAI v2.1 vs THAI v2.2 vs OPTIMIZED ENG")
print("=" * 120)
print(f"{'Turn':<28} | {'1.ไทยเดิม':<10} | {'2.Eng ปกติ':<11} | {'3.ไทย v2.1':<11} | {'4.ไทย v2.2':<11} | {'5.Eng+กฎv2.2'}")
print("-" * 120)
print(f"{'Turn 1 (สร้างเว็บใหม่)':<28} | {t1['th_legacy']:>8}   | {t1['en_normal']:>9}   | {t1['th_v21']:>9}   | {t1['th_v22']:>9}   | {t1['en_opt']:>9}")
print(f"{'Turn 2 (สั่งแก้สี+เพิ่มคูปอง)':<28} | {t2['th_legacy']:>8}   | {t2['en_normal']:>9}   | {t2['th_v21']:>9}   | {t2['th_v22']:>9}   | {t2['en_opt']:>9}")
print(f"{'Turn 3 (ส่ง Error ไปแก้บั๊ก)':<28} | {t3['th_legacy']:>8}   | {t3['en_normal']:>9}   | {t3['th_v21']:>9}   | {t3['th_v22']:>9}   | {t3['en_opt']:>9}")
print("-" * 120)
print(f"{'รวม 3 Turns ทั้งโปรเจกต์':<28} | {totals['th_legacy']:>8}   | {totals['en_normal']:>9}   | {totals['th_v21']:>9}   | {totals['th_v22']:>9}   | {totals['en_opt']:>9}")
print("=" * 120)
