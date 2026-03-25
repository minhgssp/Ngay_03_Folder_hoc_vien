"""
merge_kwsr.py — Gộp các module KWSR thành một tài liệu hoàn chỉnh.

Sử dụng:
    python merge_kwsr.py

Output: Kien_truc_Agent_KWSR.md (cùng thư mục cha)
"""
import os
from pathlib import Path

# Thứ tự gộp file
MODULE_ORDER = [
    "00_Mo_dau.md",
    "01_Knowledge.md",
    "02_Workflow.md",
    "03_Skill.md",
    "04_Rule.md",
    "05_Mo_hinh_Tien_hoa.md",
]

SEPARATOR = "\n\n---\n\n"

def main():
    script_dir = Path(__file__).parent
    modules_dir = script_dir / "KWSR_Modules"
    output_file = script_dir / "Kien_truc_Agent_KWSR.md"

    if not modules_dir.exists():
        print(f"[ERROR] Không tìm thấy thư mục: {modules_dir}")
        return

    parts = []
    for filename in MODULE_ORDER:
        filepath = modules_dir / filename
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8").strip()
            parts.append(content)
            print(f"  [OK] Đã đọc: {filename} ({len(content):,} ký tự)")
        else:
            print(f"  [SKIP] Không tìm thấy: {filename}")

    merged = SEPARATOR.join(parts)

    # Ghi file output
    output_file.write_text(merged, encoding="utf-8")

    print(f"\n{'='*60}")
    print(f"  ✅ Đã gộp {len(parts)} modules → {output_file.name}")
    print(f"  📏 Tổng: {len(merged):,} ký tự / {merged.count(chr(10)):,} dòng")
    print(f"  📁 Output: {output_file}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
