# Sprint SP-260325-UC07: Đối Soát Chấm Công & Đóng Gói Tự Động Hóa

## 📝 Bối Cảnh
Chuyên viên Nhân sự (không biết lập trình) cần thực hiện đối soát dữ liệu chấm công hàng tháng. Công việc bao gồm kiểm tra sự hiện diện của nhân viên từ dữ liệu máy chấm công, đối chiếu với các đơn xin nghỉ phép trên hệ thống để xác định trạng thái đi làm (Vắng có phép, vắng không phép, đi trễ, về sớm).

## 🎯 Mục Tiêu
1. **Xử lý dữ liệu**: Hoàn thành việc đối soát cho 2 file dữ liệu demo (`raw_attendance.csv` và `leave_requests.csv`).
2. **Đóng gói tri thức**: Ghi chép toàn bộ quá trình thực hiện để xây dựng bộ công cụ tự động hóa (Prompt/Workflow/Script) cho tương lai.
3. **Minh bạch hóa quá trình**: Duy trì nhật ký trao đổi đầy đủ giữa User và AI Agent.

## ⚖️ Luật Lệ Sprint (BẮT BUỘC TUÂN THỦ)
1. **SSOT (Single Source of Truth)**: Luôn cập nhật và duy trì 3 file cốt lõi trong suốt quá trình làm việc:
   - `Readme.md`: Bối cảnh, mục tiêu và luật lệ.
   - `Plan.md`: Khám phá dữ liệu và kế hoạch triển khai.
   - `Log.md`: Toàn bộ diễn biến hội thoại giữa User và AI.
2. **Cô lập dữ liệu**: Mọi thao tác chỉ thực hiện trên dữ liệu copy trong thư mục `data/` của Sprint, không can thiệp file gốc.
3. **Cập nhật liên tục**: Sau mỗi bước ngoặt hoặc quyết định quan trọng, AI phải cập nhật ngay các file tài liệu này.

---
**Sprint ID:** SP-260325-UC07  
**Status:** Phase 0 - Khởi tạo hoàn tất.
