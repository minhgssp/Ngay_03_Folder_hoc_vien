---
description: Khởi tạo, phân tích bối cảnh và thiết lập cấu trúc nền tảng cho dự án Webinar (Đa dụng)
---

# WORKFLOW: /webinar-start

**Mục tiêu:** 
Tự động hóa luồng khởi tạo dự án Webinar ở mọi chuẩn hình thức (B2B, Internal, Technical, Sales). Workflow này đóng gói tư duy "Working Backward": tự động đọc hiểu bối cảnh, thiết lập Master Checklist động, xác định Quality Gate từ kết quả kỳ vọng và tạo cấu trúc thư mục Sprint tùy chỉnh.

## CÁC BƯỚC THỰC THI (EXECUTION STEPS)

Khi người dùng gọi lệnh `/webinar-start`, AI Agent sẽ tuần tự thực thi:

**1. Khởi tạo Không gian & Thu thập Input:**
- Yêu cầu người dùng cung cấp vị trí thư mục Sprint và file tài liệu Bối cảnh (Business Context), kèm theo các mục tiêu/kết quả kỳ vọng cốt lõi của họ đối với Webinar này.
- Tạo file `02_Conversation_Log.md` để ghi chép lại mọi quyết định và trao đổi trong suốt phiên làm việc.
- Tạo hoặc cập nhật file `todo.md` để theo dõi tiến độ.

**2. Phân tích Bối cảnh (Context Evaluation):**
- Đọc file Bối cảnh, bóc tách cấu trúc: Pain points (Nỗi đau), Đối tượng mục tiêu (Audience), và Mục tiêu KPI (Objectives).
- Tạo file `01_Context_Evaluation.md`. Agent tự động suy luận để tìm ra các "Điểm mù thông tin" (Missing Info) tùy thuộc vào hình thái sự kiện (Ví dụ: Nền tảng livestream, Quà tặng phễu/Lead Magnet, Lịch trình, Ngân sách...).
- Tự động liệt kê các Options khả thi cho những phần khuyết thiếu để người dùng dễ dàng lựa chọn lấp đầy bối cảnh.

**3. Tạo Cấu trúc Thư mục Động (Dynamic Folder Matrix):**
Sử dụng AI tool `run_command` để tạo các thư mục dựa trên vòng đời sự kiện.
*(Cấu trúc sau là bộ khung tham khảo mặc định, Agent có thể thay đổi số lượng tuỳ bối cảnh)*
// turbo
```bash
mkdir 01_Strategy_And_Pillars
mkdir 02_Promo_Materials
mkdir 03_Tech_And_RunDown
mkdir 04_Post_Webinar_Assets
```

**4. Khởi tạo Quality Gate (Nguyên lý Working Backward):**
- Tổng hợp các kết quả mong đợi của người dùng ở Bước 1.
- Tạo file `04_Quality_Gate_Criteria.md`: Truy ngược từ các kỳ vọng đó thành những tiêu chuẩn đo lường chất lượng cụ thể (Acceptance Criteria). Mọi bản nháp sau này đều phải lọt qua rào cản duyệt (Gate) này.

**5. Lập Master Checklist Tùy Biến:**
- Dựa trên bối cảnh mở và hệ tiêu chuẩn Quality Gate, Agent phân rã công việc sinh ra file `03_Master_Checklist.md`.
- Checklist bắt buộc phải bao quát đủ các mảng công việc theo dạng Timeline. Thường sẽ quy hoạch thành 3-4 mảng cốt lõi (Mở, không fix cứng):
  - Nội dung & Chiến lược.
  - Vận hành & Kỹ thuật.
  - Marketing & Kéo số.
  - Khai thác hậu sự kiện (Repurposing).
- Cụ thể hóa từng đầu việc nhỏ để đảm bảo chặn được các rủi ro đã vạch ra ở Quality Gate.

**6. Đối chiếu Chéo & Báo cáo (Cross-check & Notify):**
- Soi chiếu lại: Đảm bảo Master Checklist thoả mãn tuyệt đối các tiêu chuẩn Quality Gate (Agent tự động bổ sung task nếu phát hiện điểm đứt gãy).
- Gọi `notify_user` để báo cáo hoàn thành quy trình Khởi tạo, đính kèm kết quả `03_Master_Checklist.md` và `04_Quality_Gate_Criteria.md` để người dùng xác nhận.
