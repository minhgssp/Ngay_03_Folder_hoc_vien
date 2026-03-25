# Kế Hoạch Triển Khai Phương Án 3 (PA3): Software UI

**Mục tiêu:** Tạo ra một ứng dụng độc lập, có giao diện trực quan. Người dùng (nhân viên HR) không cần biết code, không cần truy cập AI, chỉ việc Import file và Export file.

---

## 1. Cấu trúc thư mục (Deliverables)
Phương án PA3 sẽ bao gồm:
- `attendance_gui.py`: Script Python chứa toàn bộ mã nguồn GUI và Logic đối soát.
- `requirements.txt`: Các thư viện cần thiết (ví dụ: `pandas`, `tkinter`).
- `README_PA3.md`: Hướng dẫn cài đặt và sử dụng (thậm chí hướng dẫn build file `.exe` bằng `pyinstaller`).

## 2. Các bước triển khai (Implementation Steps)

### Bước 2.1: Lập trình Logic "Cứng" (Core Engine)
Sử dụng thư viện `pandas` để xử lý bảng logic.
1. Đọc DataFrames từ 2 file CSV.
2. Join trên khóa `[EmpID, Date]`.
3. Áp dụng Rule Engine (Hàm phân loại IF/ELSE cứng):
   - Tính toán khoảng cách In/Out.
   - Trễ > 08:30 -> Late.
   - Thiếu 1 trong 2 -> Missing Punch...
   - Có Leave -> Trả về Paid hoặc Unpaid.

### Bước 2.2: Lập trình Giao diện Người Dùng (GUI)
Thiết kế giao diện tối giản (ví dụ dùng `tkinter` hoặc `customtkinter`):
- 2 Nút Browse: (1) Chọn file chấm công thô, (2) Chọn file duyệt phép.
- Khu vực trạng thái: Hiển thị file đã chọn.
- 1 Nút bấm to: "Chạy Đối Soát & Xuất Báo Cáo".
- Popup báo thành công và mở thư mục chứa file.

### Bước 2.3: Test Toàn diện
- Chạy thử app chọn 2 file CSV trong thư mục `data` của Sprint.
- So sánh `final_attendance_report.csv` sinh ra từ code so với bản thủ công ở Phase 2. Đảm bảo cấu trúc 8 cột y chang.

## 3. Đặc điểm & Hạn chế
Tính "Đóng gói" của ứng dụng là 100%. Anh có thể quăng phần mềm cho 1 thực tập sinh làm mà không cần training dài dòng. Tuy nhiên nếu chính sách Công ty đổi (vd: đổi giờ làm), anh bắt buộc phải mở file `attendance_gui.py` lên để sửa `08:30` thành `09:00` thay vì chỉnh tham số trên màn hình hoặc qua Prompt.
