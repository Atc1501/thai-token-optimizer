#!/usr/bin/env python3
"""
Thai Token Preprocessor Utility
Programmatic regex-based cleaner for compressing Thai queries and responses
before sending to LLMs or during stream processing.
"""

import re
from typing import Dict

# Particles and polite fluff (can be safely stripped without losing semantics)
POLITE_PARTICLES = [
    r"\bครับ\b", r"\bค่ะ\b", r"\bนะครับ\b", r"\bนะคะ\b", r"\bขอบคุณครับ\b",
    r"\bขอบคุณค่ะ\b", r"\bรบกวน\b", r"\bขออนุญาต\b", r"\bหน่อยครับ\b",
    r"\bหน่อยค่ะ\b", r"\bด้วยครับ\b", r"\bด้วยค่ะ\b", r"\bช่วย\b(?=ตรวจสอบ|ดู|เขียน|แก้)",
]

# Verbose connector mappings to high-density alternatives
CONNECTOR_MAP: Dict[str, str] = {
    "เพื่อที่จะทำการ": "เพื่อ",
    "เพื่อที่จะ": "เพื่อ",
    "ในการที่จะ": "ในการ",
    "ในกรณีที่": "หาก",
    "ในส่วนของ": "สำหรับ",
    "ยกตัวอย่างเช่น": "เช่น",
    "เป็นเพราะว่า": "เพราะ",
    "เนื่องจากว่า": "เพราะ",
    "มีความสามารถในการ": "สามารถ",
    "ทำหน้าที่ในการ": "ใช้",
    "คอนฟิกูเรชัน": "Config",
    "คอนฟิก": "Config",
    "ฐานข้อมูล": "Database",
    "สถาปัตยกรรม": "Architecture",
    "ฟังก์ชัน": "Function",
    "แอปพลิเคชัน": "App",
}

def compress_thai_text(text: str, keep_politeness: bool = False) -> str:
    """
    Compress verbose Thai text to minimize token count.
    
    Args:
        text: Input Thai text
        keep_politeness: If True, skips stripping polite particles (useful for formal bots)
        
    Returns:
        High-density compressed text
    """
    result = text

    if not keep_politeness:
        for pattern in POLITE_PARTICLES:
            result = re.sub(pattern, "", result)

    for verbose, dense in CONNECTOR_MAP.items():
        result = result.replace(verbose, dense)

    # Normalize excessive spaces created by deletions
    result = re.sub(r"[ \t]+", " ", result).strip()
    return result

if __name__ == "__main__":
    sample = "รบกวนช่วยตรวจสอบคอนฟิกูเรชันของฐานข้อมูลเพื่อที่จะทำการเชื่อมต่อให้หน่อยครับ"
    print("Original :", sample)
    print("Compressed:", compress_thai_text(sample))
