# USE CASE 07: KỸ THUẬT ĐỐI SOÁT CHẤM CÔNG VÀ XIN PHÉP
**Dành cho:** Kế toán (C&B, Payroll), Hành chính (Admin) - Level: Cơ bản (Non-tech)

## 🎯 Bối Cảnh Thực Tế Doanh Nghiệp
Mỗi tháng, chuyên viên C&B phải trích xuất dữ liệu máy chấm công vân tay của hàng trăm nhân sự. Sau đó, đối chiếu với danh sách Đăng ký nghỉ phép / Công tác (HRIS) nhằm phân loại trạng thái: **"Vắng hợp lệ"** hay **"Vắng không phép"**, **"Đi trễ"**, hay **"Về sớm"**. 
Quá trình này tốn từ 2-3 ngày, phụ thuộc nhiều vào hàm VLOOKUP trên Excel và tỷ lệ sai sót rất cao do dữ liệu đầu vào "nhiễu" (thiếu giờ In/Out).

Mục tiêu của Use Case này: Hướng dẫn học viên lộ trình khám phá và kiểm soát AI. Bạn sẽ không nhận một câu lệnh (Prompt) có sẵn. Thay vào đó, bạn sẽ yêu cầu AI: (1) Trình bày cách làm, (2) Khớp tay nháp 5 trường hợp, (3) Đề xuất phương án tự động hóa, (4) Thực thi thử từng phương án để bạn tự do chọn lựa điều phù hợp nhất.

---

## 🚀 HƯỚNG DẪN "TƯ DUY LÀM CHỦ AI" - XÂY DỰNG TỪ CON SỐ 0

### Bước 1: Gửi tài liệu thô & Hỏi AI đề xuất giải pháp (Exploration Phase)
1. Tải lên 2 file: `raw_attendance.csv` (Dữ liệu máy vân tay) và `leave_requests.csv` (Đơn xin nghỉ).
2. Sử dụng Prompt mồi: 
   > "Chào bạn, tôi là chuyên viên Nhân sự và không biết lập trình. Tôi có 2 file dữ liệu đính kèm. Khó khăn của tôi là mỗi cuối tháng phải kiểm tra xem nhân viên có đi làm đủ không, nếu vắng thì phải xem họ có đơn trên hệ thống hay không rồi tổng hợp lại thành 1 bảng mới.
   > Bạn có khả năng giúp tôi giải quyết bài toán này không? Nếu có, bạn sẽ làm theo các bước nào để đảm bảo tính chính xác? (Tuyệt đối chưa xử lý dữ liệu vội, chỉ trình bày tư duy logic của bạn)."
3. **Kết quả kỳ vọng:** AI sẽ phân tích cột `EmpID` để liên kết 2 file và tự vạch ra luồng suy nghĩ gồm 4 bước: Quét giờ In/Out -> Tìm nhân viên thiếu giờ -> Tra cứu bảng phép để lấy lý do Approved -> Gộp bảng.

### Bước 2: Yêu cầu AI đối chiếu thủ công để kiểm chứng (Manual Testing)
Khẳng định quyền lực của bạn: Bắt AI làm nháp để chứng minh năng lực trước khi tự động hóa.
1. Sử dụng Prompt:
   > "Tư duy của bạn rất chính xác với nguyên tắc C&B. Bây giờ, hãy làm thử nghiệm thủ công trên 5 nhân sự đầu tiên ngay trong khung chat này. 
   > Nguyên tắc: Kiểm tra chấm công -> Nếu thiếu giờ/vắng mặt thì đối chiếu file đơn phép -> Gộp lại bảng mới và tạo ra cột Trạng thái cuối cùng.
   > Xuất kết quả đối chiếu thành một bảng Markdown để tôi kiểm tra tính đúng đắn."
2. **Kết quả kỳ vọng:** AI xuất ra một bảng Markdown thể hiện đúng 4 tình huống chấm công (vắng có phép, quên quẹt, đi trễ, bình thường). Bạn kiểm tra bằng mắt, nếu thấy sai, hãy chỉnh ngay lập tức (Ví dụ: "Bạn làm sai trường hợp EMP004. Người này nghỉ có phép, sao bạn ghi là vắng không phép? Hãy làm lại.")

### Bước 3: Đòi hỏi AI đề xuất 3 mức độ Tự động hóa
Khi bài test thủ công hoàn hảo, đây là lúc bạn muốn tự động hóa việc này cho hàng ngàn nhân sự tháng sau mà không phải đánh máy lại từ đầu.
1. Sử dụng Prompt:
   > "Kết quả đối soát thủ công hoàn toàn xuất sắc! Tháng sau tôi sẽ có dữ liệu của 5000 nhân sự và không rảnh để copy đoạn chat này lặp lại. 
   > Bạn hãy đề xuất cho tôi 3 phương án tối ưu để tự động hóa quy trình này. Yêu cầu:
   > 1. Phương án Tự động hóa 100% bằng Prompt (Build Workflow hoặc Prompt Template).
   > 2. Phương án Code cấu trúc lai (Hybrid): Vừa dùng Script ngầm vạn năng, vừa phối hợp ra lệnh bằng ô chat.
   > 3. Phương án Tự động hóa qua Phần mềm: Code 1 phần mềm có giao diện người dùng (UI) trực quan.
   > Ở cả 3 phương án, bạn phải đảm bảo hệ thống tham chiếu học hỏi từ 'dữ liệu chuẩn' tôi vừa xác nhận ở lần chạy thủ công trên (Few-shot learning)."

### Bước 4: Chạy thử Phương án 1 (Prompt Template / Workflow)
1. Sử dụng Prompt:
   > "Tôi muốn thử Phương án 1 trước. Hãy đóng gói đoạn hội thoại trên thành một System Prompt Template (Biểu mẫu vạn năng). Từ nay tôi chỉ cần thả 2 file CSV vào và chèn dòng Template này là bạn tự xử lý đúng logic thủ công trên."
2. **Trải nghiệm học viên:** Phương án này dễ nhất, không cần đụng đến code, phù hợp cho file data nhỏ dưới 500 dòng. AI xử lý trực tiếp trên khung chat cực kỳ nhanh.

### Bước 5: Chạy thử Phương án 2 (Hybrid Code & Chat)
1. Sử dụng Prompt:
   > "Bây giờ chuyển qua Phương án 2. Hãy viết một tập lệnh Python nền tảng (attendance_matcher.py). Code này chỉ làm phần nặng nhọc nhất là Gộp Dữ Liệu (Merge) bằng EmpID, xuất ra file tạm. Sau đó, viết một đoạn Prompt để tôi nạp file tạm đó vào đây và nhờ bạn chat cùng tôi để xử lý các 'ca khó' bằng ngôn ngữ tự nhiên."
2. **Trải nghiệm học viên:** Phương án này phù hợp cho data khổng lồ (vài chục ngàn dòng hoặc nặng). Python gánh phần Data Prep, còn khâu quyết định (Scoring) do AI trên chat đảm nhiệm. Ở môi trường linh hoạt cao, chuyên viên C&B làm chủ 100% logic linh hoạt từng tháng.

### Bước 6: Chạy thử Phương án 3 (Phần mềm tự động 100% có Giao diện UI)
1. Sử dụng Prompt:
   > "Tuyệt vời. Cuối cùng hãy đến với Phương án 3. Tôi là sếp và tôi lười, nên tôi muốn 'bấm nút là xong'. Hãy lập trình cho tôi công cụ phần mềm Giao diện UI với Tkinter (hoặc PyQt). Yêu cầu thiết kế 1 cửa sổ có 2 nút [Tải file Chấm công, Tải file Nghỉ phép] và 1 nút [Xử lý & Xuất Excel]. Tích hợp luôn logic chấm công thành công ở lần làm thủ công vào trong code. Viết toàn bộ mã nguồn ra đây."
2. **Trải nghiệm học viên:** AI sẽ nôn ra mã nguồn `attendance_matcher_gui.py`. Học viên chạy thử, màn hình phần mềm hiện lên! Mọi thứ được giải quyết trong 1 cái click. Phương pháp này "chống rác dữ liệu lên ô chat", nhưng buộc phải nhờ AI sửa code nếu chính sách lương thay đổi.

### Bước 7: Đối chiếu & Lựa chọn Workflow doanh nghiệp
Sau khi thử nghiệm cả 3 phương án do chính AI "đẻ" ra, học viên sẽ phải tự rút ra kết luận dựa vào tình hình hệ thống của công ty mình:
- Mới bắt đầu, ít công cụ -> Dùng **PA1 (Prompt Automation)**.
- Data quá lớn, hay đổi quy chế mỗi tháng -> Dùng **PA2 (Hybrid)**.
- Quy trình đã chốt cứng, muốn phát cho nhiều kế toán viên tự dập máy móc -> Dùng **PA3 (Software UI)**.

Đây chính là đỉnh cao của năng lực quản trị Agent: "Không xin cá, mà tự ép AI đóng thuyền".
