# 📘 Hướng dẫn sử dụng `merge_kwsr.py`

## Mục đích

Script này **gộp 6 module Markdown** trong thư mục `KWSR_Modules/` thành **một tài liệu hoàn chỉnh** tên `Kien_truc_Agent_KWSR.md`, phục vụ cho việc phân phối tài liệu kiến trúc Agent KWSR dưới dạng file duy nhất.

## Yêu cầu

- **Python 3.6+** (không cần cài thêm thư viện nào)

## Cấu trúc thư mục cần có

```
Ngay_03_Folder_hoc_vien/
├── merge_kwsr.py              ← Script gộp file
├── KWSR_Modules/              ← Thư mục chứa các module nguồn
│   ├── 00_Mo_dau.md
│   ├── 01_Knowledge.md
│   ├── 02_Workflow.md
│   ├── 03_Skill.md
│   ├── 04_Rule.md
│   └── 05_Mo_hinh_Tien_hoa.md
└── Kien_truc_Agent_KWSR.md    ← File output (tự động tạo/ghi đè)
```

## Cách sử dụng

Mở terminal tại thư mục chứa script, chạy lệnh:

```bash
python merge_kwsr.py
```

## Kết quả mong đợi

Script sẽ in ra log cho từng module đã đọc:

```
  [OK] Đã đọc: 00_Mo_dau.md (5,209 ký tự)
  [OK] Đã đọc: 01_Knowledge.md (4,778 ký tự)
  [OK] Đã đọc: 02_Workflow.md (5,806 ký tự)
  [OK] Đã đọc: 03_Skill.md (5,972 ký tự)
  [OK] Đã đọc: 04_Rule.md (4,960 ký tự)
  [OK] Đã đọc: 05_Mo_hinh_Tien_hoa.md (5,131 ký tự)

============================================================
  ✅ Đã gộp 6 modules → Kien_truc_Agent_KWSR.md
  📏 Tổng: ~35,000 ký tự
  📁 Output: .../Kien_truc_Agent_KWSR.md
============================================================
```

## Khi nào cần chạy lại?

- Khi **chỉnh sửa nội dung** bất kỳ file nào trong `KWSR_Modules/`
- Khi **thêm/xóa module** (cần cập nhật danh sách `MODULE_ORDER` trong script)

## Lưu ý

| Tình huống | Xử lý |
|---|---|
| Thiếu thư mục `KWSR_Modules/` | Script báo lỗi và dừng |
| Thiếu 1 file module | Script bỏ qua file đó (hiện `[SKIP]`) và gộp các file còn lại |
| File output đã tồn tại | Tự động **ghi đè** không cảnh báo |

## Tùy chỉnh nâng cao

Nếu muốn thêm module mới, mở `merge_kwsr.py` và thêm tên file vào danh sách `MODULE_ORDER`:

```python
MODULE_ORDER = [
    "00_Mo_dau.md",
    "01_Knowledge.md",
    "02_Workflow.md",
    "03_Skill.md",
    "04_Rule.md",
    "05_Mo_hinh_Tien_hoa.md",
    "06_Ten_Module_Moi.md",  # ← Thêm dòng này
]
```
