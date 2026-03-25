# Kế Hoạch Triển Khai Phương Án 2 (PA2): Hybrid (Python + AI)

**Mục tiêu:** Chia tách quy trình đối soát để tối ưu chi phí token và năng lực xử lý: Python lo phần "chân tay" (gộp data), AI lo phần "trí tuệ" (suy luận logic phân loại).

---

## 1. Cấu trúc thư mục (Deliverables)
Phương án PA2 sẽ bao gồm:
- `attendance_merger.py`: Script Python để đọc 2 file CSV và ghép lại thành một bảng dữ liệu sạch.
- `PA2_Scoring_Prompt.md`: Câu lệnh AI để phân loại 5 trạng thái dựa trên file dữ liệu đã làm sạch.
- `README_PA2.md`: Hướng dẫn sử dụng phương án Hybrid này.

## 2. Các bước triển khai (Implementation Steps)

### Bước 2.1: Viết Script Data Merger (Python)
Script sẽ làm các tác vụ sau:
1. Đọc `raw_attendance.csv` và `leave_requests.csv`.
2. Trích xuất thời điểm In/Out.
3. LEFT JOIN thông tin đơn phép dựa trên `EmpID` và `Date`.
4. Xuất ra tệp `merged_attendance.csv` (Đã gộp nhưng CHƯA có cột Final_Status). Cột này chứa đầy đủ thông tin In/Out/LeaveType/ApprovalStatus.

### Bước 2.2: Soạn PA2 Scoring Prompt
Prompt này sẽ nhận đầu vào là file `merged_attendance.csv` ở trên.
- **Nhiệm vụ:** AI chỉ cần thực hiện đánh giá logic cuối cùng (suy luận 5 trạng thái) dựa trên bảng "đã có sẵn cả In/Out lẫn đơn phép ở cùng 1 dòng".
- **Lợi ích:** Bot không phải nhớ thông tin từ 2 bảng khác nhau, độ tập trung logic tăng vọt, đỡ tốn token.

### Bước 2.3: Viết Document
Viết hướng dẫn cho User: Cách chạy lệnh Python `python attendance_merger.py` → kéo file kết quả lên AI cùng Prompt.

## 3. Lý do lựa chọn & Tính linh hoạt
Đây là phương án lý tưởng nhất cho HR. Nó xử lý được cả vạn dòng dữ liệu (gộp bằng Python cực kỳ nhanh), đồng thời việc điều chỉnh quy trình đánh giá kết quả (ví dụ trễ 5 phút có bị trừ lương hay không) vẫn nằm trên text Prompt, HR có thể tự sửa mà không cần nhờ Coder.
