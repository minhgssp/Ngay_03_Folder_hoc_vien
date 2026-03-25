## 5. 🔄 Mô Hình Tiến Hóa Năng Lực Agent

### 5.1 Nghịch lý về sự trưởng thành

AI Agent rất thông minh trong việc trả lời câu hỏi, nhưng lại "non nớt" trong việc vận hành hệ thống. Tuần đầu bạn hướng dẫn chi tiết, Agent làm tốt. Tuần sau bạn nói "Làm báo cáo như cũ", Agent lại hỏi như người mới.

Vấn đề không nằm ở trí tuệ của AI, mà nằm ở **cơ chế kết tinh tri thức**. Agent cần một lộ trình để chuyển hóa từ xử lý rời rạc thành kinh nghiệm tái sử dụng.

---

### 5.2 Bốn giai đoạn Tiến hóa

Quá trình phát triển Agent tương ứng với bốn trụ cột KWSR:

| Giai đoạn | Tầng | Trọng tâm | Hành động HR |
|---|---|---|---|
| **1. Discovery** | Knowledge | Học hỏi, nạp dữ liệu | Upload quy chế nhân sự, danh sách nhân viên |
| **2. Standardization** | Workflow | Chuẩn hóa quy trình | Tạo Workflow "6 bước sàng lọc CV" |
| **3. Specialization** | Skill | Nâng tầm chất lượng | Đóng gói Skill "Phỏng vấn hành vi STAR" |
| **4. Control** | Rule | Bảo vệ & Kiểm soát | Thiết lập Rule "Không tiết lộ lương ứng viên A cho B" |

---

### 5.3 Mô hình Tiến hóa Hai Chiều

KWSR thoạt nhìn là đường thẳng tuyến tính. Nhưng trong thực tế, môi trường kinh doanh **luôn biến động**. Một quy trình hoàn hảo hôm nay có thể lỗi thời vào ngày mai.

Hệ thống cho phép chuyển đổi **hai chiều**:

```
← Thích nghi (Adaptation) ←

     Knowledge ←→ Workflow ←→ Skill ←→ Rule

→ Tiến hóa (Evolution) →
```

- **Tiến hóa (→):** Biến kinh nghiệm rời rạc thành quy trình chuẩn.
- **Thích nghi (←):** Khi Rule/Skill cũ không còn phù hợp → phá vỡ → quay về Knowledge để học cách làm mới.

**Ví dụ HR:** Công ty chuyển từ "Tuyển dụng qua Email" sang "Tuyển dụng qua ATS (Applicant Tracking System)":
1. Hủy bỏ Workflow và Rule cũ về email.
2. Quay về Knowledge — Agent học cách sử dụng ATS mới.
3. Khi đã thạo → Thiết lập Workflow mới cho ATS.
4. Đóng gói Skill mới về sàng lọc ứng viên trên ATS.

---

### 5.4 Đo lường mức độ trưởng thành

**Công thức:**
```
Độ trưởng thành (%) = 100% - (Số lần phải can thiệp sửa lỗi / Tổng số tác vụ giao)
```

**Phân tích nguyên nhân can thiệp → Biết cần bổ sung tầng nào:**

| Loại can thiệp | Biểu hiện | Cần bổ sung |
|---|---|---|
| **Về ngữ cảnh** | Agent không hiểu thuật ngữ, không tìm thấy file | → Knowledge |
| **Về quy trình** | Agent làm sai thứ tự, bỏ sót bước | → Workflow |
| **Về chất lượng** | Agent làm đúng nhưng kết quả xấu, sai format | → Skill |
| **Về an toàn** | Agent làm việc nguy hiểm, rủi ro | → Rule |

**Thang đo đánh giá:**

| Mức | Giai đoạn | Cách quản lý |
|---|---|---|
| **< 70%** | Học việc | Giám sát chặt, hướng dẫn từng bước. Tập trung xây Knowledge. |
| **70–90%** | Thạo việc | Giao việc theo quy trình, kiểm tra kết quả cuối. Tối ưu Workflow & Skill. |
| **> 90%** | Chuyên gia | Giao quyền tự chủ cao. Quản trị bằng Rule, giám sát ngoại lệ. |

---

### 5.5 Thứ tự ưu tiên KWSR theo ngành

Không phải ngành nào cũng bắt đầu từ Knowledge. Ngành có rủi ro cao cần xây **Rule trước**:

| Ngành | Thứ tự ưu tiên | Lý do |
|---|---|---|
| **HR** | K → W → S → R | Cần nạp context trước, rủi ro ở mức trung bình |
| **Marketing** | K → W → S → R | Sáng tạo cần context, quy trình đến sau |
| **Tài chính - Kế toán** | **R → W → S** → K | Sai số = hậu quả tài chính, Rule phải có trước |
| **Ngân hàng - Bảo hiểm** | **R → S → W** → K | Tuân thủ KYC/AML là bắt buộc, Skill chuyên môn cao |
| **Pháp lý** | **S → R** → K → W | Chất lượng phân tích pháp lý là yếu tố quyết định |

---

### 5.6 Vai trò kiến tạo của Người vận hành

Sự trưởng thành của Agent **phản chiếu sự rõ ràng trong tư duy quản lý** của bạn:

- Bạn làm việc tùy hứng → Agent dừng ở mức Knowledge rời rạc.
- Bạn có tư duy quy trình → Agent thành cỗ máy vận hành (Workflow).
- Bạn chú trọng chất lượng → Agent thành chuyên gia (Skill).
- Bạn có tư duy quản trị rủi ro → Agent thành trợ lý đáng tin cậy (Rule).

> 💡 Đừng kỳ vọng phép màu xảy ra ngay lập tức. Hãy kiên nhẫn dẫn dắt Agent đi qua từng giai đoạn. Đó là cách bền vững nhất để xây dựng một Song Sinh Số thực sự đắc lực.

---

*Tài liệu này được trích xuất và biên soạn dựa trên cuốn SGK Antigravity Full v2, Chương 2.4 & Chương 3, phục vụ cho khóa Masterclass HR-AI.*
