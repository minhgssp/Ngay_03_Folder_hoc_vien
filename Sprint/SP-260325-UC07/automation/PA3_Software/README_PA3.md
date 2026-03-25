# Hướng Dẫn Sử Dụng Nhận Sự: Công Cụ Chấm Công Tự Động (PA3)

Đây là Phần mềm **Hệ Thống Đối Soát Tự Động 1-Click** (Software UI) đã được đóng rắn theo logic đối soát hiện tại của Công ty. Phần mềm lấy sự ổn định, tiện lợi bảo mật làm gốc, do Python và Pandas đảm nhiệm sức mạnh xử lý 10,000 dòng trong tích tắc.

## I. Yêu Cầu Cài Đặt (Chỉ làm 1 lần trên máy mới)
Nếu máy bạn chưa có thư viện hỗ trợ xử lý Data (Pandas), hãy mở Terminal (PowerShell/CMD) trỏ tới thư mục này và gõ:
```bash
pip install -r requirements.txt
```

## II. Cách Chạy Phần Mềm
1. Click đúp vào file `attendance_gui.py` hoặc bật command line: `python attendance_gui.py`
2. Màn hình phần mềm sẽ hiện ra y hệt trong quá trình thực hành đối soát.

## III. Các Bước Sử Dụng (Dành cho HR hàng tháng)
1. Bấm nút **Browse** dòng số 1: Chọn file chấm công xuất từ máy quẹt thẻ (*.csv hoặc *.xlsx).
2. Bấm nút **Browse** dòng số 2: Chọn file Đơn xin phép xuất ra từ hệ thống nghỉ (*.csv hoặc *.xlsx).
3. Bấm **🚀 XỬ LÝ & XUẤT BÁO CÁO**.
4. Check kết quả: Phần mềm sẽ tự động bật popup và xuất ra file chứa toàn bộ trạng thái cuối theo tên mã mới nhất: `Final_Report_yyyymmdd_hhmmss.csv`, nằm ngạy cạnh chỗ lưu file gốc thẻ từ.

---
**Chú ý bảo trì (Maintainance):**
Toàn bộ logic chấm: Giờ tính muộn là **08:31**, Logic nghỉ phép (Unpaid, Paid Leave)... đã được **cứng hóa (Hardcode)** trong Python. Nếu công ty thay quy định, cần nhờ Coder mở file `.py` và chỉnh sửa tham số `t_limit`.
