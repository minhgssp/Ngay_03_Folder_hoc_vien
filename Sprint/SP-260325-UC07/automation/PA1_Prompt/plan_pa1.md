# Kế Hoạch Triển Khai Phương Án 1 (PA1): Prompt Automation

**Mục tiêu:** Quản lý đối soát chấm công hoàn toàn bằng Prompt AI. Không sử dụng mã nguồn (code) hay cài đặt phần mềm ngoài nào.

---

## 1. Cấu trúc thư mục (Deliverables)
Phương án PA1 sẽ bao gồm:
- `PA1_Prompt_Template.md`: File chứa câu lệnh Prompt chuẩn để User tái sử dụng hàng tháng.
- `PA1_Data_Prep_Guide.md`: Hướng dẫn ngắn cách User chuẩn bị dữ liệu (gộp 2 file CSV vào 1 file Excel) trước khi ném cho AI.

## 2. Các bước triển khai (Implementation Steps)

### Bước 2.1: Soạn thảo Prompt Template
Sử dụng mô hình "Role-Task-Context-Constraint" (Vai trò - Nhiệm vụ - Bối cảnh - Ràng buộc).
- **Ngữ cảnh (Context):** Định nghĩa rõ các cột, ý nghĩa và quy tắc (ví dụ: in > 08:30 là đi trễ).
- **Nhiệm vụ (Task):** Yêu cầu AI đọc file, phân loại từng dòng ra 1 trong 5 trạng thái: `[OK]`, `[Late]`, `[Missing Punch]`, `[Paid Leave]`, `[Unpaid Leave]`.
- **Ràng buộc (Constraint):** Bắt buộc trả về đúng cấu trúc bảng Markdown/CSV 8 cột, không bỏ sót dòng nào.

### Bước 2.2: Soạn tài liệu Hướng dẫn Chuẩn bị Dữ liệu
Vì các LLM thường xử lý kém khi ném nhiều file CSV rời rạc, em sẽ viết một hướng dẫn đơn giản:
1. Mở Excel, copy `raw_attendance.csv` vào Sheet 1.
2. Copy `leave_requests.csv` vào Sheet 2.
3. Lưu thành 1 file Excel duy nhất rồi upload lên kèm Prompt.

### Bước 2.3: Kiểm thử
- Giả lập User tải 2 file demo hiện tại thành 1 file và áp dụng Prompt Template vào một session chat rỗng.
- Kiểm tra tính đúng đắn của output.

## 3. Quản lý Rủi Ro
- **Rủi ro:** Khi data lớn hàng nghìn dòng, Prompt có thể bị "ngộp", trả về đầu ra bị cắt xén (cut-off) hoặc bị ảo giác (chế data).
- **Giảm thiểu:** Ghi chú rõ Constraint trong Prompt yêu cầu AI chỉ xử lý N dòng mỗi lượt, hoặc báo ngay khi file vượt quá số lượng khuyên dùng (~500 dòng).
