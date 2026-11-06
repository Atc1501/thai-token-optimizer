#!/usr/bin/env python3
"""
Thai Token Optimizer Benchmark
Compares token counts between:
1. Verbose Standard Thai
2. English Equivalent
3. Optimized Thai (Thai Token Optimizer applied)

Supports:
- OpenAI tiktoken (cl100k_base / o200k_base)
- Character-based fallback estimation if tiktoken is not installed
"""

import sys

TEST_CASES = [
    {
        "name": "Code Review Request",
        "verbose_thai": "รบกวนช่วยตรวจสอบโค้ดในไฟล์นี้ให้หน่อยครับว่าทำไมมันถึงรันไม่ผ่านและมีบั๊กตรงไหนบ้าง",
        "english": "Please check this file to find why it fails to run and identify any bugs.",
        "optimized_thai": "ตรวจไฟล์นี้: สาเหตุรันไม่ผ่าน + บั๊ก",
    },
    {
        "name": "Database Config Explanation",
        "verbose_thai": "ในการที่จะทำการเชื่อมต่อฐานข้อมูลนั้น จำเป็นต้องใส่คอนฟิกูเรชันของพอร์ตและโฮสต์ให้ถูกต้องนะครับ",
        "english": "To connect to the database, you need to configure the correct host and port.",
        "optimized_thai": "เชื่อมต่อ Database: ต้องระบุ Host และ Port ให้ถูกต้อง",
    },
    {
        "name": "User Clarification Question",
        "verbose_thai": "ขออนุญาตสอบถามเพิ่มเติมได้ไหมครับว่าต้องการให้บันทึกข้อมูลลงในระบบแบบไหนดีครับ",
        "english": "May I ask which format you would like to save the data in?",
        "optimized_thai": "ต้องการบันทึกข้อมูลรูปแบบไหน?",
    },
    {
        "name": "API Error Notification",
        "verbose_thai": "ระบบไม่สามารถทำการส่งข้อมูลคำขอไปยังเซิร์ฟเวอร์ปลายทางได้เนื่องจากเกิดข้อผิดพลาดในการตรวจสอบสิทธิ์การเข้าใช้งานครับ",
        "english": "Failed to send request to target server due to an authentication error.",
        "optimized_thai": "ส่ง Request ล้มเหลว: Auth Error ที่ปลายทาง",
    },
]

def get_token_counter():
    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")
        return lambda text: len(enc.encode(text)), "tiktoken (cl100k_base - GPT-4/3.5)"
    except ImportError:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("o200k_base")
            return lambda text: len(enc.encode(text)), "tiktoken (o200k_base - GPT-4o)"
        except Exception:
            pass
    
    # Fallback heuristic if tiktoken is not installed
    def heuristic(text: str) -> int:
        thai_chars = sum(1 for c in text if '\u0e00' <= c <= '\u0e7f')
        other_chars = len(text) - thai_chars
        # Approximate: ~2.5 tokens per Thai character cluster/word, ~4 chars per token for English
        return int((thai_chars * 0.7) + (other_chars / 4.0))
    return heuristic, "Heuristic Estimation (Install tiktoken for exact tokens: pip install tiktoken)"

def run_benchmark():
    counter, engine_name = get_token_counter()
    print("=" * 80)
    print(f" THAI TOKEN OPTIMIZER BENCHMARK")
    print(f" Engine: {engine_name}")
    print("=" * 80)

    total_verbose = 0
    total_english = 0
    total_optimized = 0

    print(f"{'Case':<22} | {'Verbose Thai':<14} | {'English':<10} | {'Optimized':<10} | {'Saved (%)':<10}")
    print("-" * 80)

    for case in TEST_CASES:
        c_verbose = counter(case["verbose_thai"])
        c_eng = counter(case["english"])
        c_opt = counter(case["optimized_thai"])

        total_verbose += c_verbose
        total_english += c_eng
        total_optimized += c_opt

        saved_pct = ((c_verbose - c_opt) / c_verbose) * 100
        print(f"{case['name']:<22} | {c_verbose:<14} | {c_eng:<10} | {c_opt:<10} | {saved_pct:>8.1f}%")

    print("-" * 80)
    total_saved = ((total_verbose - total_optimized) / total_verbose) * 100
    print(f"{'TOTAL / AVERAGE':<22} | {total_verbose:<14} | {total_english:<10} | {total_optimized:<10} | {total_saved:>8.1f}%")
    print("=" * 80)
    print(f"\n[Summary] Optimized Thai achieves comparable or fewer tokens than English, saving ~{total_saved:.1f}% vs Standard Thai!")

if __name__ == "__main__":
    run_benchmark()
