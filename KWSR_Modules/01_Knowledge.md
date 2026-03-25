## 1. 🧠 K — Knowledge (Kiến Thức & Chiều Sâu Context)

### 1.1 Định nghĩa

Knowledge là toàn bộ dữ liệu, thông tin ngữ cảnh, tài liệu, và lịch sử tương tác mà Agent có quyền truy cập. Không chỉ đơn thuần là "bộ nhớ", Knowledge trong Antigravity là **Hệ thống Ngữ cảnh Tích lũy** (Cumulative Context).

Nếu không có Knowledge vững chắc, Agent sẽ bị "mất trí nhớ tạm thời" hoặc rơi vào trạng thái **ảo giác** (Hallucination) — tức là bịa đặt thông tin nghe có vẻ đúng nhưng thực tế hoàn toàn sai.

---

### 1.2 Mô hình Ba Tầng Tri Thức

Tương tự bộ não con người có trí nhớ ngắn hạn và dài hạn, Agent trong Antigravity quản lý thông tin qua **ba cơ chế riêng biệt**:

| Tầng | Quản lý bởi | Thời hạn | Mục đích | Vị trí trên máy |
|---|---|---|---|---|
| **Brain** | 🤖 Hệ thống (Tự động) | Ngắn hạn | Lưu vết lịch sử tương tác (log thô) | `~/.gemini/antigravity/brain/` |
| **Knowledge** | 🤖 Hệ thống (Tự động) | Dài hạn | Tái sử dụng kinh nghiệm đã chắt lọc | `~/.gemini/antigravity/knowledge/` |
| **Database** | ✋ Người dùng (Thủ công) | Dài hạn | Tổ chức dữ liệu nguồn & sản phẩm | Thư mục dự án do bạn tạo |

**Brain** ghi lại *mọi thứ* — từng câu hỏi, câu trả lời, thao tác file — nhưng dữ liệu còn thô, chưa cấu trúc. Hãy hình dung Brain như cuốn sổ ghi chép bừa bộn của nhân viên.

**Knowledge** là kết quả của quá trình **phân tích chủ động**. Một sub-agent chuyên trách (Knowledge Subagent) liên tục rà soát các cuộc hội thoại, chắt lọc tri thức hữu ích, và lưu thành các **Knowledge Items (KIs)**. Mỗi KI gồm:
- **Metadata:** Chủ đề, thời gian tạo, nguồn gốc.
- **Artifacts:** Quy trình mẫu (Markdown), đoạn mã xử lý (Code snippets), file cấu hình.

**Database (Workspace)** là "bàn làm việc" vật lý — nơi bạn tổ chức file Input, file trung gian, và Output theo cấu trúc IPO.

---

### 1.3 Cấu trúc 3 Tầng Dữ Liệu (The 3-Layer Context)

Ngoài cách tổ chức theo cơ chế lưu trữ (Brain/Knowledge/Database), dữ liệu đầu vào cho Agent cũng cần được phân tầng theo **phạm vi ảnh hưởng**:

1. **Core Knowledge (Kiến thức lõi Doanh nghiệp):**
   - **Bao gồm:** Tầm nhìn, sứ mệnh, văn hóa công ty, quy định chung, danh mục sản phẩm.
   - **Ví dụ HR:** Hồ sơ công ty YCOMPASS, cơ cấu tổ chức, giá trị cốt lõi.
   - **Tác dụng:** Đảm bảo mọi câu trả lời bám sát bản nguyên của doanh nghiệp.

2. **Role Knowledge (Kiến thức Đặc thù Vị trí):**
   - **Bao gồm:** Bộ luật lao động, chính sách C&B, quy trình tuyển dụng chuẩn.
   - **Ví dụ HR:** Bộ luật Lao động 2019, Quy chế lương thưởng nội bộ.
   - **Tác dụng:** Giúp Agent đóng vai HR chuyên nghiệp thay vì trả lời chung chung.

3. **Task/Session Knowledge (Kiến thức Phiên làm việc):**
   - **Bao gồm:** CV đang xét duyệt, email trao đổi, dữ liệu bảng lương tháng này.
   - **Ví dụ HR:** 50 CV ứng viên cho vị trí Marketing Manager.
   - **Tác dụng:** Giới hạn vùng suy nghĩ của Agent vào bài toán hiện tại.

---

### 1.4 Tự động vs. Thủ công

| Hành động | Cách thức |
|---|---|
| Agent tự ghi nhớ sau mỗi phiên | ✅ **Tự động** — Knowledge Subagent chạy ngầm |
| Bạn yêu cầu Agent lưu kiến thức cụ thể | ✅ **Thủ công** — Nói: *"Hãy lưu quy trình này vào Knowledge để dùng lại sau."* |
| Cập nhật Knowledge cũ không còn phù hợp | ✅ **Thủ công** — Hướng dẫn lại để Agent tạo phiên bản mới |

---

### 1.5 Ưu và Nhược điểm

**Thế mạnh:** Linh hoạt. Không cần chuẩn bị tài liệu phức tạp ngay từ đầu — chỉ cần bắt đầu làm việc và hệ thống tự học. Rất phù hợp giai đoạn đầu dự án khi mọi thứ chưa định hình.

**Hạn chế:** Thiếu tính nhất quán. Vì dựa trên kinh nghiệm cá nhân và ngữ cảnh cụ thể, tri thức này khó nhân bản cho người khác. Một Agent "hiểu ý" bạn chưa chắc làm việc tốt với đồng nghiệp của bạn.

> 💡 **Dấu hiệu cần tiến lên Workflow:** Khi bạn nhận thấy mình đang phải hướng dẫn Agent cùng một chuỗi hành động lặp đi lặp lại (trên 3 lần), đó là lúc Knowledge không đủ.
