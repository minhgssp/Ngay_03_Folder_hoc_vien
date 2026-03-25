# BỘ TIÊU CHÍ ĐÁNH GIÁ CHẤT LƯỢNG (QUALITY GATE)
*Nguyên lý: Cấu trúc Working Backward - Truy ngược từ Kết quả kỳ vọng*

Dưới đây là 4 trụ cột tiêu chí (Quality Gates) được định nghĩa dựa trên kết quả cuối cùng mà người dùng (End-User/Attendee) phải nhận được. Mọi task triển khai trong dự án phải thỏa mãn các tiêu chí này trước khi được duyệt (Release).

## 1. Tiêu chí 1: Khán giả đông, nhiều người biết tới (Reach & Viral)
- **Định nghĩa:** Thông điệp sự kiện phải phủ rộng, tác động mạnh vào "Pain-point" của tệp B2B để tạo sự tò mò và lan truyền.
- **Tiêu chuẩn nghiệm thu (Acceptance Criteria):**
  - [ ] Content PR không viết chung chung, phải có "Góc nhìn/Insight" gây tranh luận (Ví dụ: CEO đăng đàn bóc phốt sai lầm Sales).
  - [ ] Có ít nhất 3 điểm chạm (Touchpoints) qua kênh khác nhau (Email Teaser, LinkedIn Organic, Retargeting Ads).
  - [ ] Hình ảnh (Visual) phải hiển thị rõ Pain-point và Giá trị (Value) ngay trong 3 giây lướt feed.

## 2. Tiêu chí 2: Đăng ký dễ dàng (Frictionless UX)
- **Định nghĩa:** Trải nghiệm người dùng từ lúc click vào link đến lúc thấy chữ "Đăng ký thành công" phải trơn tru, không có ma sát.
- **Tiêu chuẩn nghiệm thu (Acceptance Criteria):**
  - [ ] Landing Page áp dụng cấu trúc thuyết phục (PAS/AIDA).
  - [ ] Form điền thông tin ngắn gọn (Tối đa 3-4 trường thông tin: Tên, Email, SĐT, Chức vụ).
  - [ ] Landing view chuẩn SEO, load nhanh dưới 2s và hoàn hảo trên cả Mobile (70% traffic B2B lướt đt).

## 3. Tiêu chí 3: Thông tin được cập nhật kịp thời (Real-time Comms)
- **Định nghĩa:** Khách hàng không bao giờ bị rơi vào trạng thái "quên" lịch hoặc không biết link tham dự ở đâu.
- **Tiêu chuẩn nghiệm thu (Acceptance Criteria):**
  - [ ] Nhận ngay Email xác nhận (Trigger) trong vòng phút đầu tiên sau khi đăng ký thành công (Kèm link add to Calendar).
  - [ ] Có luồng nhắc nhở đa kênh được tự động hoá: T-3 (Email), Day-0 (Sáng sớm SMS/Email), Trực tiếp trước 1 tiếng (SMS link Zoom thẳng).

## 4. Tiêu chí 4: Sau sự kiện được nhận đủ tài liệu (Impeccable Fulfillment)
- **Định nghĩa:** Lời hứa về "Quà tặng" / "Record" / "Template" được thực thi chính xác theo hành vi xem của khách để điều hướng họ trở thành MQL.
- **Tiêu chuẩn nghiệm thu (Acceptance Criteria):**
  - [ ] Phải phân tách rõ 2 luồng Automation sau sự kiện chạy trong vòng 24h: 
        - Luồng Attendee (Người tham dự): Gửi tóm tắt Q&A, Quà tặng Master Template, và nút CTA Đặt lịch Tư vấn (Booking).
        - Luồng No-show (Người vắng mặt): Gửi thư tiếc nuối và bản thu VOD để níu kéo quan tâm.

---

## 5. Báo cáo Đối chiếu (Cross-check) với Master Checklist hiện tại
*Đánh giá xem 03_Master_Checklist.md có đáp ứng đủ 4 tiêu chí này chưa.*

- **Với Tiêu chí 1 (Reach):** Checklist ĐÃ ĐẢM BẢO. Cụ thể ở Mảng 2 đã có task lên Email 10k data, chạy Retargeting T-7 và viết bài CEO T-3.
- **Với Tiêu chí 2 (Đăng ký UX):** Checklist HƠI THIẾU. Có task tạo Landing Page nhưng CHƯA CÓ task "Test tối ưu UI/UX form điền cho Mobile" và "Setup quà mồi lúc đăng ký".
- **Với Tiêu chí 3 (Cập nhật):** Checklist ĐÃ ĐẢM BẢO. Có task cài SMS đếm ngược tự động và báo danh trực tiếp.
- **Với Tiêu chí 4 (Fulfillment):** Checklist ĐÃ ĐẢM BẢO. Ở mảng 4 phân luồng Email Attendee/No-show cực rõ.

👉 *Hành động khắc phục:* Em sẽ cập nhật bổ sung Task tối ưu Mobile UX và Test Trigger Form vào file Master Checklist để chặn lỗ hổng ở Tiêu chí 2.
