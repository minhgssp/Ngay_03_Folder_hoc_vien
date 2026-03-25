# Đề Xuất Nâng Cấp: Kiến Trúc Cốt Lõi Của AI Agent - Khung KWSR (Chuyên Sâu)

*Tài liệu này được nâng cấp với độ phân giải cao hơn, đi sâu vào cấu trúc vi mô của từng thành phần trong nền tảng Antigravity. Đây là tài liệu lõi dành cho **Ngày 3: Thiết Kế & Lắp Ráp Agent**, giúp học viên hiểu cách chuyển đổi AI từ một "trợ lý trả lời câu hỏi" thành một "chuyên gia tự chủ" cấp doanh nghiệp.*

---

## 1. 🧠 K - Knowledge (Kiến thức & Chiều sâu Context)

Không chỉ đơn thuần là "bộ nhớ", Knowledge trong Antigravity là **Hệ thống Ngữ cảnh Tích lũy (Cumulative Context)**. Nếu không có Knowledge vững chắc, Agent sẽ bị "mất trí nhớ tạm thời" hoặc rơi vào trạng thái ảo giác (Hallucination).

### Cấu trúc 3 Tầng Kiến Thức (The 3-Layer Context):

1. **Core Knowledge (Kiến thức lõi Doanh nghiệp):**
   - **Bao gồm:** Tầm nhìn, sứ mệnh, văn hóa công ty, quy định chung, danh mục sản phẩm (Ví dụ: Hồ sơ công ty YCOMPASS giả lập).
   - **Tác dụng:** Đảm bảo mọi câu trả lời của Agent luôn bám sát bản nguyên của doanh nghiệp.
2. **Role Knowledge (Kiến thức Đặc thù Vị trí):**
   - **Bao gồm:** Bộ luật lao động hiện hành, chính sách C&B, quy trình tuyển dụng chuẩn của phòng Nhân sự.
   - **Tác dụng:** Cung cấp "nền tảng chuyên môn" để Agent có thể đóng vai HR thay vì Marketing.
3. **Task/Session Knowledge (Kiến thức Phiên làm việc):**
   - **Bao gồm:** CV của ứng viên đang xét duyệt, chuỗi email thảo luận trước đó, dữ liệu bảng lương tháng này.
   - **Tác dụng:** Giới hạn vùng không gian suy nghĩ của Agent vào bài toán hiện tại.

### Cơ chế lưu trữ:

- **Knowledge Items (KIs):** Là các khối kiến thức đã được chắt lọc (distilled knowledge) từ các cuộc hội thoại cũ. Agent sẽ tự động đối chiếu các KIs này trước khi đưa ra quyết định mới.

---

## 2. ⚙️ W - Workflow (Thuật toán Thực thi - SOPs)

Workflow không phải là một Prompt dài. Workflow là một **Thuật toán Thực thi (Execution Algorithm)** ép Agent phải tư duy logic, bước qua bước, loại bỏ tính ngẫu hứng của AI.

### Giải phẫu một Workflow chuẩn:

- **Mục tiêu rõ ràng (Ideal State Criteria):** Định nghĩa cụ thể thành phẩm cuối cùng trông như thế nào.
- **Micro-steps định tuyến (Step-by-step Execution):** Chia nhỏ vấn đề. Thay vì "Hãy đánh giá CV này", Workflow sẽ yêu cầu:
  1. *Bước 1:* Trích xuất các kỹ năng cứng.
  2. *Bước 2:* So sánh kỹ năng cứng với Job Description.
  3. *Bước 3:* Đưa ra điểm số theo thang 1-10.
- **Cơ chế Checkpoint (Trạm kiểm duyệt):** Yêu cầu Agent phải báo cáo và nhận sự phê duyệt (Approval) của con người trước khi chuyển sang bước tiếp theo (Đặc biệt quan trọng khi Agent chuẩn bị gửi email hay thay đổi dữ liệu).

### Tại sao cần Workflow?

Workflow tạo ra **Sự Ổn Định (Consistency)**. Một Workflow tốt đảm bảo dù bạn chạy yêu cầu 100 lần, kết quả trả về từ AI vẫn có chất lượng đồng đều 100 lần.

---

## 3. 🛠️ S - Skill (Gói Năng lực Chuyên môn Sâu)

Nếu Workflow là "cách làm việc", thì Skill là "chất lượng công việc". Skill nâng cấp Agent từ cấp độ "Biết làm" lên cấp độ "Bậc thầy".

### Bản chất của Skill trong Antigravity:

Skill là một "chiếc hộp đen" (Package) có thể cắm-rút (Plug-and-play), chứa đựng các bí quyết tinh hoa của ngành nghề.

### Cấu trúc của một Skill HR điển hình:

- **Framework chuyên ngành:** Áp dụng mô hình phỏng vấn STAR (Situation, Task, Action, Result) thay vì hỏi đáp chung chung.
- **Tiêu chuẩn Đánh giá (Rubrics):** Định nghĩa thế nào là câu trả lời xuất sắc, thế nào là câu trả lời kém.
- **Công cụ vật lý (Tooling):** Ví dụ như một script Python tích hợp sẵn để xuất báo cáo đánh giá ứng viên ra file định dạng PDF/Word ngay lập tức.
- **Tone & Voice riêng:** Skill Viết Thông báo Sa thải (Offboarding) sẽ có tone giọng cực kì khác so với Skill Viết Thư Mời Nhận Việc (Offer Letter).

---

## 4. 🛡️ R - Rule (Hệ thống Rào Cản & Sự An Toàn)

Rule là ranh giới sống còn (Guardrails). Khi trao quyền cho AI làm các việc quan trọng (như tuyển dụng, lương thưởng), thiếu Rule sẽ gây ra rủi ro tàn khốc (Blast Radius).

### 3 Cấp Độ Rào Cản (Red Team Safeguards):

1. **Behavioral Rules (Quy tắc Kỷ luật Kế thừa):**
   - Bắt buộc giao tiếp bằng Tiếng Việt chuyên nghiệp, không dùng từ ngữ lóng/thiếu tôn trọng (Ví dụ: Đã gỡ bỏ các cụm từ "sáo rỗng", "viết rác" trong hệ thống).
   - Tuyệt đối không tự bịa đặt dữ liệu (Zero Hallucination Tolerance).
2. **Operational Rules (Quy tắc Vận hành):**
   - Chặn tác vụ lặp vô hạn (Circuit Breakers): Nếu tìm kiếm tài liệu không thấy sau 3 lần rà soát, Agent phải dừng lại và hỏi người dùng, không được tự ý tiếp tục.
   - Luôn sử dụng file cục bộ (Absolute Paths) thay vì URL ngoài nếu không được phép.
3. **Security Rules (Quy tắc Bảo mật Cao cấp):**
   - Không được phép (Forbidden) chia sẻ thông tin PII (Personally Identifiable Information - Dữ liệu cá nhân) cho các phòng ban không liên quan.
   - Thẩm quyền (Permissions): Phải xin phép con người (Human-in-the-loop) mỗi khi muốn xóa một file hay gửi đi một luồng email tự động.
