---
name: Webinar Automation (Meta-Workflow)
description: "Sử dụng Skill này khi người dùng yêu cầu 'tổ chức webinar', 'làm webinar', 'kế hoạch webinar', 'khởi tạo dự án sự kiện online'. Skill này áp dụng nguyên lý Working Backward để tự động thiết lập Master Checklist, Quality Gate và cấu trúc thư mục."
---

# 🎭 Webinar Automation (Working Backward Framework)

> **Mục tiêu:** Tự động hóa toàn bộ quy trình phân tích bối cảnh kinh doanh, lập Master Checklist, xác định Quality Gate và tạo cấu trúc thư mục nền tảng cho một dự án Webinar ở bất kỳ định dạng nào.

## 1. Context Evaluation & Feedback (Phân tích Bối cảnh)
Khi kích hoạt Skill, Agent ngay lập tức:
- Đọc file Bối cảnh (nếu có) hoặc yêu cầu user cung cấp: KPIs, Pain-point, Hành vi Target Audience.
- **Cực kỳ Quan trọng:** Suy luận và tự động phân tích "Điểm mù thông tin" tuỳ thuộc vào hình thái sự kiện (Ví dụ cụt lủn: Nền tảng livestream, Quà tặng phễu, Budget MKT, Thời gian lên sóng...).
- Tự động liệt kê các Options (Lựa chọn) khả thi cho những phần khuyết thiếu để user dễ dàng gật đầu lấp đầy bối cảnh.
- Tạo file `01_Context_Evaluation.md` và `02_Conversation_Log.md` (để ghi chép lại mọi quyết định của luồng hội thoại).

## 2. Dynamic Folder Matrix (Tạo Cấu trúc Thư mục Động)
Sử dụng công cụ hệ thống để tạo các thư mục gốc, phân nhánh theo vòng đời sự kiện. Cấu trúc mặc định thường là:
```bash
mkdir 01_Strategy_And_Pillars
mkdir 02_Promo_Materials
mkdir 03_Tech_And_RunDown
mkdir 04_Post_Webinar_Assets
```

## 3. Khởi tạo Quality Gate (Nguyên lý Working Backward)
- Đọc các kết quả/thành quả mong đợi của người dùng từ Bối cảnh.
- Tạo file `04_Quality_Gate_Criteria.md`: Truy ngược từ các kỳ vọng đó thành các tiêu chuẩn đo lường (Acceptance Criteria) cứng rắn. Ví dụ: (Reach / Mức độ lan toả -> UX Landing Page -> Real-time Comms -> Nurturing Fulfillment). Mọi kế hoạch sau này phải vượt qua Gate này.

## 4. Master Checklist Tùy Biến (Dynamic Plan)
- Từ Quality Gate, Agent đẻ ra file `03_Master_Checklist.md`.
- **Luật Cấm Hardcode:** Tuyệt đối KHÔNG fix cứng đầu việc. Phải tuỳ biến, nhưng nên bao quát tối thiểu 4 mảng: Nội dung cốt lõi, Kỹ thuật (Tech & Backstage), Marketing Kéo số, và Sales Repurposing.
- Cụ thể hóa từng task con (VD: Mobile UX Mobile Form, Auto SMS T-0) để chặn đứng mọi rủi ro nảy sinh ở Quality Gate.

## 5. Báo cáo Chéo (Cross-check & Closure)
- Gọi tool để bàn giao cho người dùng 2 file Master Checklist và Quality Gate.
- Đưa ra báo cáo phân tích xem Checklist đã đủ bít lỗ hổng của Gate hay chưa. Xin lệnh duyệt tiếp theo.
