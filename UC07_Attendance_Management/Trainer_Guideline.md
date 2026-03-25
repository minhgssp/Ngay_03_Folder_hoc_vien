# Hướng dẫn thao tác (Trainer Guideline) - Trợ lý nhắc nhở

## Mục đích
Tạo Bot "đòi nợ" hồ sơ cho HR. Sự lặp lại "Em ơi nộp bằng" sẽ chấm dứt.

## Chuẩn bị
Sử dụng file `nhan_su_onboarding.csv`

## Câu lệnh Prompt mẫu (Hãy Copy / Dán vào Antigravity)
```
Đây là bảng 'nhan_su_onboarding.csv'.
Nhiệm vụ của bạn là:
1. Quét tìm tất cả các nhân sự có giá trị "Chưa nộp" ở cột "Bằng Cấp_Giấy Tờ".
2. Tự động viết 1 kịch bản tin nhắn Zalo hối thúc gửi đích danh cho từng người này (Xưng hô cho phù hợp, nhắc họ chuẩn bị luôn bản công chứng cứng nếu cần). Lưu tin nhắn nháp ra file 'Bot_Reminders.md'.
```

## Cách thực hiện
**Bước 1:** Gửi file theo dõi hồ sơ nhân sự thô.
**Bước 2:** Chạy yêu cầu hối thúc. 
**Bước 3:** (WOW MOMENT 💥) File `Bot_Reminders.md` được sinh ra tự động! Nó đã liệt kê lời nhắc hoàn chỉnh cho Nguyễn Văn A, Lê Huy B... cực kỳ dễ thương hoặc nghiêm khắc tùy AI. HR chỉ việc copy paste gửi luôn!
