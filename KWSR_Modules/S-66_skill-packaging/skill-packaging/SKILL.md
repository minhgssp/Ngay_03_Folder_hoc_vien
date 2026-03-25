---
name: skill-packaging
description: Chuyên dụng để đóng gói kiến thức, framework, hoặc các công cụ thành Skill chuẩn Antigravity. Sử dụng khi cần tạo skill mới, cập nhật cấu trúc skill hiện có, hoặc chuẩn hóa tài liệu theo Agent Skills Specification.
license: Proprietary
metadata:
  author: AI_RM (Antigravity)
  version: "1.0"
---

# 📦 Kỹ năng Đóng gói Skill (Skill Packaging)

Kỹ năng này cung cấp quy trình vận hành tiêu chuẩn (SOP) để biến các tài liệu rời rạc thành một "Gói Kỹ Năng" (Skill Package) mà các AI Agent khác có thể dễ dàng hiểu và vận hành.

## 1. Cấu trúc thư mục chuẩn (Directory Structure)

Mọi Skill phải nằm trong một thư mục riêng biệt với cấu trúc sau:

```
skill-name/
├── SKILL.md          # Bắt buộc: Chứa metadata (frontmatter) và hướng dẫn lõi
├── scripts/          # Tùy chọn: Chứa mã thực thi (Python, Bash, JS)
├── references/       # Tùy chọn: Chứa tài liệu tham khảo chi tiết
├── assets/           # Tùy chọn: Chứa templates, hình ảnh, tài nguyên tĩnh
└── ...               # Các file bổ trợ khác
```

## 2. Định dạng file `SKILL.md`

### 2.1. Frontmatter (Phần đầu file)
Bắt buộc phải có YAML frontmatter:

| Trường | Bắt buộc | Ràng buộc |
| :--- | :--- | :--- |
| `name` | Có | Chữ thường, số, dấu gạch ngang. Độ dài tối đa 64 ký tự. |
| `description` | Có | Mô tả rõ chức năng và **khi nào cần sử dụng**. Tối đa 1024 ký tự. |
| `license` | Không | Loại license (ví dụ: MIT, Apache-2.0, Proprietary). |
| `compatibility`| Không | Yêu cầu môi trường (ví dụ: Python 3.10+, Docker). |

**Ví dụ tối giản:**
```markdown
---
name: my-new-skill
description: Mô tả ngắn gọn về kỹ năng này.
---
```

### 2.2. Phần thân (Body content)
Đây là nơi chứa hướng dẫn vận hành cho Agent. Các mục nên có:
- **Hướng dẫn từng bước (Step-by-step instructions)**.
- **Ví dụ Input/Output**.
- **Các trường hợp ngoại lệ (Edge cases)**.

## 3. Quy tắc tối ưu Context (Progressive Disclosure)

Để tiết kiệm Token và tăng hiệu suất, Skill cần tuân thủ:
1. **Metadata (~100 tokens):** `name` và `description` được load khi khởi động. Hãy làm cho chúng cực kỳ rõ ràng để hệ thống biết khi nào cần kích hoạt.
2. **Hướng dẫn (< 5000 tokens):** Toàn bộ `SKILL.md` sẽ được load khi skill được kích hoạt. Hãy giữ file này dưới 500 dòng.
3. **Tài nguyên (Khi cần):** Các file trong `scripts/` hoặc `references/` chỉ được đọc khi Agent thực sự cần dùng đến thông qua các lệnh đọc file.

## 4. Thực hành tốt nhất (Best Practices)

Để tạo ra một Skill có độ chính xác cao và hữu dụng, hệ thống yêu cầu:
- **Khởi nguồn từ thực tế (Start from real expertise):** KHÔNG bao giờ dùng LLM để generate skill suông mà không có ngữ cảnh. Hãy extract pattern từ quá trình giải quyết task thực tế hoặc từ logs hệ thống của dự án.
- **Tiêu dùng Context tinh gọn (Spend context wisely):** Bỏ qua những kiến thức phổ thông mà LLM đã biết (VD: PDF là gì). Chỉ tập trung vào Gotchas, Edge Cases, và Quy ước nội bộ (Internal conventions) của dự án.
- **Thiết kế từng phần mạch lạc (Coherent Units):** Đảm bảo scope của skill hợp lý. Không quá hẹp, cũng không ôm đồm quá nhiều (VD: Đừng bao gồm "database administration" vào một skill "database query formatting").
- **Kiểm soát linh hoạt (Calibrating control):** Cho Agent khoảng trống với các thao tác linh hoạt. Ép buộc (Prescriptive) và đưa ra khuôn mẫu mặc định (Defaults) cho những thao tác dễ gây vỡ hệ thống.

> Chi tiết các ví dụ và kỹ thuật tối ưu hóa Context được ghi chép tại: `c:\commandcenter\02_AI_Hub\SPRINTS\SP-260324-01-Skill-Packaging\Skill_Packaging_Master.md`. Mọi Agent tạo skill BẮT BUỘC nên đọc/tham khảo guideline này.

## 5. Kiểm tra và Xác thực (Validation)

Sử dụng lệnh sau để kiểm tra tính hợp lệ của Skill (nếu có công cụ `skills-ref`):
```bash
skills-ref validate ./my-skill
```

---
*Lưu ý: Mọi Skill mới tạo ra phải được đăng ký vào hệ thống thông qua việc cập nhật TODO.md và INDEX.md của dự án tương ứng.*
