## 4. 🛡️ R — Rule (Hệ Thống Rào Cản & Sự An Toàn)

### 4.1 Định nghĩa

Rule là tập hợp các giới hạn và quy định bắt buộc mà Agent phải tuân thủ trong mọi tình huống. Nó trả lời hai câu hỏi:
- **"Những điều gì KHÔNG ĐƯỢC PHÉP làm?"**
- **"Những nguyên tắc nào PHẢI tuân thủ tuyệt đối?"**

Rule là ranh giới sống còn (Guardrails). Khi trao quyền cho AI làm các việc quan trọng (như tuyển dụng, lương thưởng), thiếu Rule sẽ gây ra rủi ro tàn khốc (**Blast Radius** — vùng ảnh hưởng khi sai sót xảy ra).

**Ví dụ rủi ro thực tế:** Một Agent "quá nhiệt tình" có thể tự động gửi email từ chối 50 ứng viên mà chưa qua duyệt của Manager. Hậu quả: mất ứng viên tiềm năng, tổn hại thương hiệu tuyển dụng, vi phạm quy trình nội bộ.

---

### 4.2 Ba cấp độ Rào cản

#### Cấp 1: Behavioral Rules (Quy tắc Hành vi)
Quy định cách Agent giao tiếp và ứng xử.

- Bắt buộc giao tiếp bằng tiếng Việt chuyên nghiệp, không dùng từ ngữ lóng hoặc thiếu tôn trọng.
- Tuyệt đối không tự bịa đặt dữ liệu (**Zero Hallucination Tolerance**).
- Giữ đúng tone/voice của thương hiệu nhà tuyển dụng.

#### Cấp 2: Operational Rules (Quy tắc Vận hành)
Quy định cách Agent thao tác với hệ thống.

- **Circuit Breakers:** Nếu tìm kiếm tài liệu không thấy sau 3 lần, Agent phải dừng lại và hỏi, không được tự ý tiếp tục vô tận.
- **Read-Only Input:** Tuyệt đối không sửa file trong thư mục `01_Inputs/`.
- **Backup trước khi sửa:** Luôn tạo bản sao trước khi chỉnh sửa file quan trọng.

#### Cấp 3: Security Rules (Quy tắc Bảo mật)
Quy định về bảo vệ dữ liệu và quyền hạn.

- **Cấm** chia sẻ thông tin PII (Personally Identifiable Information) cho phòng ban không liên quan.
- **Human-in-the-loop:** Phải xin phép con người mỗi khi muốn xóa file hoặc gửi email tự động.
- **Không tiết lộ** lương, đánh giá cá nhân của ứng viên A cho ứng viên B.

---

### 4.3 Global Rule vs. Workspace Rule

Rule được phân thành hai cấp lưu trữ, với **quy tắc ưu tiên rõ ràng: Workspace luôn thắng Global**.

| Cấp | Vị trí | Đặc điểm |
|---|---|---|
| **Global Rule** | `~/.gemini/GEMINI.md` (một file duy nhất) | "Hiến pháp" — áp dụng mọi nơi, là sàn an toàn |
| **Workspace Rule** | `.agent/rules/` (nhiều file theo chủ đề) | "Luật dự án" — tùy chỉnh cho từng ngữ cảnh |

**Mẫu Global Rule (`GEMINI.md`):**
```
- Luôn trả lời bằng tiếng Việt.
- TUYỆT ĐỐI KHÔNG xóa dữ liệu gốc (Input).
- TUYỆT ĐỐI KHÔNG chia sẻ PII ra ngoài workspace.
- Luôn hỏi trước khi thực hiện thao tác xóa.
```

**Mẫu Workspace Rule (`ke_toan.md`):**
```
- Định dạng số: Phân cách hàng nghìn bằng dấu chấm (.)
- Format ngày: DD/MM/YYYY
- Bắt buộc đối chiếu tổng phát sinh Nợ/Có
- Không xuất file kế toán ra ngoài thư mục dự án
```

**Nguyên tắc vàng:** Global Rule thiết lập "sàn an toàn"; Workspace **nên nâng cao** tiêu chuẩn, **không hạ thấp**.

---

### 4.4 Bốn chế độ Kích hoạt Rule

Không phải mọi Rule đều luôn cần bật. Antigravity hỗ trợ 4 chế độ:

| Chế độ | Mô tả | Ví dụ |
|---|---|---|
| **Luôn bật** (Always On) | Áp dụng mọi lúc, mọi nơi | Quy ước đặt tên file, mã hóa UTF-8 |
| **Thủ công** (Manual) | Chỉ bật khi người dùng gọi `@mention` | `@bao_mat` — chỉ nạp khi cần xử lý dữ liệu nhạy cảm |
| **Tự động theo file** (Glob) | Bật khi Agent mở file nhất định | Mở `.xlsx` → Kích hoạt Rule format kế toán |
| **AI Tự quyết** (Model Decision) | Agent tự đánh giá ngữ cảnh và bật | Rule "ứng xử khủng hoảng" bật khi phát hiện giọng điệu gay gắt |

---

### 4.5 Rule trong Quản trị Niềm tin

Trong giai đoạn đầu triển khai AI, tâm lý chung của quản lý là lo ngại. Rule chính là giải pháp kỹ thuật để chuyển từ trạng thái **"tin tưởng mù quáng"** sang **"tin tưởng có kiểm soát"**:

| Lo ngại | Giải pháp Rule |
|---|---|
| Mất dữ liệu | Rule cấm xóa (Permissions) |
| Sai lệch thông tin | Rule về nguồn dữ liệu (Grounding) |
| Văn phong máy móc | Rule về giọng văn (Persona) |
| Rò rỉ thông tin | Rule về PII và phạm vi chia sẻ |

> 💡 **Hãy bắt đầu việc xây dựng Agent bằng việc soạn thảo file `GEMINI.md`**. Đó là nền móng vững chắc nhất cho một hệ thống AI phục vụ doanh nghiệp an toàn.
