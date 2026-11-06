import sys
import tiktoken

# Ensure UTF-8 output on Windows console
sys.stdout.reconfigure(encoding='utf-8')

# Initialize tokenizers: o200k_base (GPT-4o) and cl100k_base (GPT-4 / ChatGPT)
enc_o200k = tiktoken.get_encoding("o200k_base")
enc_cl100k = tiktoken.get_encoding("cl100k_base")

test_cases = [
    {
        "category": "1. Distributed System Architecture & Failure Recovery (วิศวกรรมระบบกระจายศูนย์)",
        "thai_verbose": (
            "ในกรณีที่ระบบเซิร์ฟเวอร์หลักเกิดความล้มเหลวในการเชื่อมต่อกับคลัสเตอร์ฐานข้อมูลแบบกระจายศูนย์ "
            "เนื่องจากมีปริมาณทราฟฟิกพุ่งสูงขึ้นอย่างกะทันหันจนเกินขีดความสามารถในการประมวลผลของโหลดบาลานเซอร์นั้น "
            "ระบบควรจะทำการตัดสลับการทำงานไปยังคลัสเตอร์สำรองโดยอัตโนมัติพร้อมทั้งส่งการแจ้งเตือนไปยังทีมผู้ดูแลระบบในทันที"
        ),
        "english": (
            "If the primary server fails to connect to the distributed database cluster due to a sudden traffic spike "
            "exceeding the load balancer's capacity, the system must automatically fail over to the replica cluster "
            "and immediately dispatch an incident alert to the DevOps team."
        ),
        "thai_optimized": (
            "หาก Primary Server หลุดการเชื่อมต่อกับ Distributed DB Cluster เพราะ Traffic พุ่งเกินพิกัด Load Balancer: "
            "ระบบต้อง Auto-failover ไป Replica Cluster ทันที พร้อมยิง Alert แจ้ง DevOps"
        )
    },
    {
        "category": "2. Financial Risk Management & Algorithmic Trading (ระบบการเงินและการซื้อขายอัลกอริทึม)",
        "thai_verbose": (
            "เพื่อที่จะทำการป้องกันความเสี่ยงจากการผันผวนของราคาคู่เงินในตลาดที่มีสภาพคล่องต่ำ "
            "ทางเราขอแนะนำให้ท่านกำหนดระดับจุดตัดขาดทุนและจุดทำกำไรที่มีความยืดหยุ่นตามค่าความผันผวนจริง "
            "และควรหลีกเลี่ยงการเปิดสถานะการซื้อขายที่มีขนาดใหญ่จนเกินไปในช่วงเวลาที่มีการประกาศตัวเลขดัชนีทางเศรษฐกิจที่สำคัญครับ"
        ),
        "english": (
            "To mitigate risk from FX price volatility in low-liquidity markets, we recommend setting dynamic stop-loss "
            "and take-profit levels pegged to real market volatility, while avoiding oversized positions during high-impact economic data releases."
        ),
        "thai_optimized": (
            "เพื่อคุม Risk ความผันผวนคู่เงินช่วงสภาพคล่องต่ำ: แนะนำตั้ง Dynamic Stop-Loss / Take-Profit ตามค่า Volatility จริง "
            "และเลี่ยงเปิด Position ขนาดใหญ่ช่วงประกาศตัวเลขเศรษฐกิจสำคัญ"
        )
    },
    {
        "category": "3. Software Development Pipeline & Quality Gate (ไปป์ไลน์การพัฒนาซอฟต์แวร์และการทดสอบ)",
        "thai_verbose": (
            "รบกวนช่วยตรวจสอบกระบวนการทำงานของการรวมโค้ดและการส่งมอบอัตโนมัติให้หน่อยครับว่า "
            "มีขั้นตอนไหนบ้างที่ทำให้การรันชุดแบบทดสอบแบบรวมหน่วยเกิดความล่าช้า "
            "และมีข้อผิดพลาดที่ไม่พึงประสงค์เกิดขึ้นบ่อยครั้งในระหว่างกระบวนการคอมไพล์โค้ดและการสร้างอิมเมจคอนเทนเนอร์หรือไม่ครับ"
        ),
        "english": (
            "Please review the CI/CD pipeline to identify stages causing integration test latency, "
            "and determine whether recurring compilation or container build errors are occurring."
        ),
        "thai_optimized": (
            "ตรวจ CI/CD Pipeline: หาจุดที่ทำให้ Integration Test ช้า + บั๊กซ้ำซ้อนระหว่าง Compile และ Build Container Image"
        )
    }
]

print("=" * 105)
print(f"{'CATEGORY & COMPARISON':<42} | {'GPT-4o (o200k)':<15} | {'GPT-4 (cl100k)':<15} | {'SAVINGS VS THAI'}")
print("=" * 105)

for case in test_cases:
    print(f"\n[ {case['category']} ]")
    
    t_v_o200k = len(enc_o200k.encode(case["thai_verbose"]))
    t_v_cl100k = len(enc_cl100k.encode(case["thai_verbose"]))
    
    eng_o200k = len(enc_o200k.encode(case["english"]))
    eng_cl100k = len(enc_cl100k.encode(case["english"]))
    
    t_opt_o200k = len(enc_o200k.encode(case["thai_optimized"]))
    t_opt_cl100k = len(enc_cl100k.encode(case["thai_optimized"]))
    
    saved_o200k = ((t_v_o200k - t_opt_o200k) / t_v_o200k) * 100
    saved_cl100k = ((t_v_cl100k - t_opt_cl100k) / t_v_cl100k) * 100
    
    print(f"  1. ไทยปกติ (Verbose Thai)    : {t_v_o200k:>3} tokens        | {t_v_cl100k:>3} tokens        | (Baseline)")
    print(f"  2. อังกฤษ (English)          : {eng_o200k:>3} tokens        | {eng_cl100k:>3} tokens        | {((t_v_o200k - eng_o200k)/t_v_o200k)*100:>5.1f}% less")
    print(f"  3. ไทยประหยัด (Optimized Thai): {t_opt_o200k:>3} tokens        | {t_opt_cl100k:>3} tokens        | {saved_o200k:>5.1f}% SAVED (-{t_v_o200k - t_opt_o200k} tok)")
    print(f"     => เปรียบเทียบกับ Eng: ไทยประหยัด {'น้อยกว่าหรือเท่ากับ' if t_opt_o200k <= eng_o200k else 'ใกล้เคียง'} อังกฤษ ({t_opt_o200k} vs {eng_o200k} tokens)")

print("\n" + "=" * 105)
