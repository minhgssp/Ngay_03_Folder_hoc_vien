## 3. 🛠️ S — Skill (Gói Năng Lực Chuyên Môn Sâu)

### 3.1 Định nghĩa

Nếu Workflow trả lời câu hỏi "Làm bước nào trước, bước nào sau?", thì Skill trả lời câu hỏi **"Làm như thế nào mới là TỐT?"**.

Skill là các gói năng lực chuyên sâu, được đóng gói sẵn để Agent sử dụng khi cần giải quyết các bài toán phức tạp đòi hỏi chất lượng cao. Skill nâng cấp Agent từ cấp độ "Biết làm" lên cấp độ **"Bậc thầy"**.

---

### 3.2 Workflow vs. Skill — Bảng so sánh

| Khía cạnh | Workflow | Skill |
|---|---|---|
| **Câu hỏi** | "Làm gì để hoàn thành?" | "Làm sao để hoàn thành **xuất sắc**?" |
| **Tập trung** | Trình tự các bước (Procedure) | Chất lượng thực hiện (Craftsmanship) |
| **Mục tiêu** | Ra được sản phẩm đúng yêu cầu | Ra sản phẩm với chất lượng cao nhất |
| **Bản chất** | Quy trình chuẩn hóa | Tinh hoa được **chắt lọc** từ quy trình |
| **Kích hoạt** | Thủ công (gõ `/ten_workflow`) | **Tự động** — Agent nhận diện và áp dụng |

**Ví dụ minh họa — Viết Email từ chối ứng viên:**

- **Giai đoạn Workflow (làm được):** Xác định người nhận → Viết tiêu đề → Viết nội dung → Kiểm tra → Gửi. Kết quả: email được gửi đi với đầy đủ thông tin.
- **Giai đoạn Skill (làm tốt nhất):** Tiêu đề dạng "Cập nhật về đơn ứng tuyển [Vị trí]" thay vì "Thông báo kết quả". Cấu trúc: cảm ơn → lý do ngắn gọn → khuyến khích → giữ kết nối. Tone giọng: tôn trọng, ấm áp, không máy móc.

---

### 3.3 Cấu trúc thư mục chuẩn của một Skill

Một Skill không phải chỉ là một file prompt. Nó là một **gói tài nguyên hoàn chỉnh**, lưu trong `.agent/skills/` hoặc `~/.gemini/antigravity/skills/`:

```
.agent/skills/
  phong-van-hanh-vi/          ← Tên thư mục Skill
    SKILL.md                  ← Hướng dẫn cốt lõi (BẮT BUỘC)
    scripts/                  ← Đoạn mã tự động hóa (tùy chọn)
      generate_report.py
    examples/                 ← Mẫu tham chiếu (tùy chọn)
      sample_interview.md
    resources/                ← Tài liệu bổ trợ (tùy chọn)
      star_framework.md
```

---

### 3.4 Mẫu file SKILL.md thực tế

File `SKILL.md` là thành phần quan trọng nhất — định nghĩa năng lực của Skill. File này được viết ở **ngôi thứ ba**, mô tả khách quan chức năng và cách sử dụng:

```markdown
---
name: phong-van-hanh-vi
description: Chuyên gia thiết kế và đánh giá phỏng vấn hành vi theo mô hình STAR.
---

# Kỹ năng Phỏng vấn Hành vi (STAR)

## Mục đích
Hỗ trợ tạo bộ câu hỏi phỏng vấn hành vi theo mô hình STAR
(Situation - Task - Action - Result) và đánh giá câu trả lời
của ứng viên theo tiêu chuẩn chất lượng.

## Phạm vi Ứng dụng
- Tạo câu hỏi phỏng vấn theo vị trí và năng lực cần đánh giá.
- Đánh giá câu trả lời có đủ 4 yếu tố STAR hay không.
- Cho điểm và nhận xét mức độ phù hợp.

## Bộ Nguyên tắc Cốt lõi
1. **Luôn bám sát STAR:** Mỗi câu hỏi phải khai thác đủ 4 yếu tố.
2. **Đánh giá hành vi, không phải ý kiến:** Hỏi "Bạn đã làm gì?"
   thay vì "Bạn nghĩ gì?".
3. **Rubrics rõ ràng:** Điểm 1-3 (yếu), 4-6 (trung bình),
   7-9 (tốt), 10 (xuất sắc).

## Quy trình Thực hiện Chuẩn
1. **Phân tích JD:** Xác định 3-5 năng lực trọng yếu cần đánh giá.
2. **Thiết kế câu hỏi:** Mỗi năng lực → 2 câu hỏi STAR.
3. **Đánh giá:** Áp dụng Rubrics cho từng câu trả lời.
4. **Tổng hợp:** Xuất báo cáo đánh giá tổng thể.
```

---

### 3.5 Cơ chế Kích hoạt Thông minh (Progressive Disclosure)

Agent không nạp toàn bộ hàng trăm Skill cùng lúc. Hệ thống sử dụng cơ chế **Tiết lộ Dần dần**:

1. **Nhận diện (Discovery):** Bình thường, Agent chỉ nắm danh sách tên Skill và mô tả ngắn (từ YAML header).
2. **Kích hoạt (Activation):** Khi bạn nói "Tạo câu hỏi phỏng vấn", Agent đối chiếu → thấy khớp với `phong-van-hanh-vi` → tự động nạp nội dung chi tiết.
3. **Thực thi (Execution):** Agent áp dụng các nguyên tắc trong `SKILL.md` để xử lý.

→ Bạn **không cần gõ lệnh** để kích hoạt Skill. Agent tự nhận diện.

---

### 3.6 Đóng gói Tri thức Chuyên gia

Skill là phương tiện hiệu quả nhất để **số hóa tri thức ngầm** (tacit knowledge) của doanh nghiệp.

**Ví dụ HR:** Trưởng phòng Nhân sự có 10 năm kinh nghiệm, biết rõ:
- *Ứng viên nào nói hay nhưng làm không tốt (dấu hiệu nhận biết).*
- *Câu hỏi nào khiến ứng viên bộc lộ bản chất thật.*
- *Cách đánh giá "culture fit" bằng trực giác.*

Thay vì phụ thuộc vào một người, doanh nghiệp yêu cầu chuyên gia mô tả phương pháp → đóng gói thành Skill → mọi Agent và nhân viên mới đều có thể sử dụng.

---

### 3.7 Khi nào nâng cấp Workflow → Skill?

Bạn nên nâng cấp khi:
- ✅ Quy trình đã **ổn định** và ít thay đổi các bước.
- ✅ Bạn có yêu cầu khắt khe về **chất lượng** đầu ra.
- ✅ Bạn muốn **tái sử dụng** năng lực này cho nhiều dự án hoặc chia sẻ cho đồng nghiệp.

> 💡 **Dấu hiệu cần bổ sung Rule:** Khi Agent đã "giỏi" (có Skill) và "nhanh" (có Workflow), bạn cần đặt câu hỏi: "Agent có thể gây hại gì nếu tự chủ hoàn toàn?" → Đó là lúc cần Rule.
