# Hướng Dẫn Chuẩn Bị Dữ Liệu (Data Prep Guide) - Phương Án 1

Vì AI làm theo Phương án 1 (Prompt Automation) sẽ đảm nhận 100% công sức phân tích dữ liệu, nên đôi khi ném vào 2 file CSV cùng lúc có thể khiến AI bối rối không biết gọi file nào nếu logic không thật sự tường minh.

Để xử lý việc đọc dữ liệu chuẩn 100%, bạn (HR) nên chuẩn bị dữ liệu gộp vào một file Excel duy nhất (*hoặc ít nhất nhắc AI rõ ràng là nó ở 2 file riêng*).

## Các bước chuẩn bị dữ liệu cực nhanh:

**Bước 1:** Tạo 1 file Excel mới đặt tên là `Data_ChamCong_Thang.xlsx`

**Bước 2:** Mở file `raw_attendance.csv` (Dữ liệu thẻ từ trên máy tải về).
- Bấm Ctrl+A, Ctrl+C (Copy tất cả).
- Paste vào **Sheet 1** của file Excel mới.
- Đổi tên phía dưới góc trải Sheet 1 thành: `Raw_Attendance`

**Bước 3:** Mở file `leave_requests.csv` (Dữ liệu xin phép trên phần mềm tải về).
- Bấm Ctrl+A, Ctrl+C (Copy tất cả).
- Paste vào **Sheet 2** của file Excel mới.
- Đổi tên Sheet 2 thành: `Leave_Requests`

**Bước 4:** Xong! Lưu file lại.
Mỗi cuối tháng, bạn chỉ mất chưa tới 30 giây để có file mẫu chẩn.
Kéo thả file `Data_ChamCong_Thang.xlsx` này vào khung chat AI. Sau đó dán câu lệnh ở file `PA1_Prompt_Template.md` đi kèm. AI sẽ đọc qua 2 Sheet và đối soát tuyệt đối độ chính xác.

---
*Lưu ý: PA1 Prompt chỉ khuyên dùng tối đa 300 - 500 dòng nhân viên/tháng. Nếu nhiều hơn, AI dễ bỏ sót dữ liệu do tràn độ dài Output window.*
