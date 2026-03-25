# KHUNG KẾ HOẠCH BỘ PHẬN: VẬN HÀNH & KỸ THUẬT (TECH & OPS)

## 1. Thông tin Chung (Overview)
- **Bộ phận phụ trách:** Ban Vận Hành (Ops) / IT / Điều phối kỹ thuật.
- **Mục tiêu:** Setup phần mềm trơn tru, bắn Automation chuẩn xác đúng giờ theo Quality Gate. Đạo diễn trơn tru Run-down của ngày Live.

## 2. Kế Hoạch Triển Khai (Action Plan)
### Đầu việc 2.1: Cài đặt và Tự Động Hóa (Automation Trigger Setup)
- Nền tảng Live: [Tên nền tảng (VD: Zoom Webinar)]. Các cài đặt cấu hình: Q&A feature, Chat on/off.
- CRM & Integration:
  - Trigger 1: Khách điền Form Landing -> Bắn API đẩy vào CRM.
  - Trigger 2: CRM -> Gửi Email xác nhận đăng ký ngay phút đầu tiên (Kèm link add-to-calendar).

### Đầu việc 2.2: Kịch bản Nhắc nhở (Real-time Comms)
- Lịch bắn Auto-SMS / Auto-Email cho list đã đăng ký:
  - T-3: Email đếm ngược "Chỉ còn 3 ngày".
  - Day 0 (Sáng 8AM): SMS nhắc nhở lịch Live rạng sáng nay.
  - Day 0 (Trước 1 giờ): SMS đính kèm thẳng link Zoom để user click vào là mở mạng trực tiếp.

### Đầu việc 2.3: Run-down Kỹ thuật Hậu trường (Backstage Matrix)
- [Bảng Kịch bản Đường dây (Minute-by-minute)]: Xác định nhân sự phụ trách:
  - Phút thứ x: Tắt nhạc đếm ngược -> Mở Mic MC.
  - Phút thứ y: Spotlight Camera diễn giả -> Bấm record trên đám mây.
- Setup Vật phẩm: Virtual Background đếm ngược, Nhạc chờ (No Copyright).

### Đầu việc 2.4: Rủi ro & Backup (Risk Management)
- Backup mạng: MC/Host có 2 thiết bị kết nối 4G phòng rớt Wifi.
- Seeding Q&A: Chuẩn bị 3 câu hỏi (chim mồi) gửi sẵn cho Mod phòng khi khán giả im lặng phần Q&A.

---
*Ghi chú Cập nhật: Lưu toàn bộ File MP3, hình ảnh Background, File Setup API vào thư mục `03_Tech_And_RunDown`.*
