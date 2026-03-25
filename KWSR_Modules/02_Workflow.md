## 2. ⚙️ W — Workflow (Thuật Toán Thực Thi)

### 2.1 Định nghĩa

Workflow là chuỗi các bước hướng dẫn cụ thể (SOP — Standard Operating Procedure) mà Agent cần tuân theo để hoàn thành một tác vụ. Workflow **không phải** là một Prompt dài. Workflow là một **Thuật toán Thực thi** (Execution Algorithm) — ép Agent phải tư duy logic, bước qua bước, loại bỏ tính ngẫu hứng.

**Tại sao cần Workflow?** Workflow tạo ra **Sự Ổn Định** (Consistency). Một Workflow tốt đảm bảo dù bạn chạy yêu cầu 100 lần, kết quả trả về từ AI vẫn có chất lượng đồng đều 100 lần.

---

### 2.2 Dấu hiệu nhận biết cần tạo Workflow

Khi bạn nhận thấy mình đang phải hướng dẫn Agent cùng một chuỗi hành động **lặp đi lặp lại trên 3 lần**, đó là tín hiệu để chuyển từ Knowledge sang Workflow.

Thay vì dựa vào trí nhớ của Agent ("Làm giống lần trước nhé"), bạn cần một bản hướng dẫn cụ thể và rõ ràng hơn.

---

### 2.3 Bốn mô hình Workflow cơ bản

Hầu hết các quy trình phức tạp đều có thể được xây dựng từ bốn mô hình cơ bản:

#### a. Mô hình Tuyến tính (Linear Flow)
Bước A → Bước B → Bước C → Output. Không có ngã rẽ.

**Ví dụ HR:** Quy trình Onboarding nhân viên mới:
1. Tạo email công ty
2. Cấp thẻ ra vào
3. Ký hợp đồng

#### b. Mô hình Song song (Parallel Flow)
Nhiều tác vụ thực hiện cùng lúc → Tổng hợp kết quả.

**Ví dụ HR:** Tổng hợp thông tin ứng viên:
- Luồng 1: Xác minh bằng cấp
- Luồng 2: Kiểm tra lý lịch
- Luồng 3: Liên hệ người tham chiếu
→ Gộp lại thành Hồ sơ đánh giá tổng hợp.

#### c. Mô hình Có điều kiện (Conditional Flow)
Agent tự ra quyết định xử lý dựa trên tính chất đầu vào (If-Else).

**Ví dụ HR:** Phân loại CV đến:
- Nếu kinh nghiệm ≥ 5 năm → Shortlist ưu tiên
- Nếu kinh nghiệm 2–5 năm → Đánh giá kỹ năng bổ sung
- Nếu kinh nghiệm < 2 năm → Từ chối lịch sự

#### d. Mô hình Lặp (Loop Flow)
Có cơ chế tự kiểm tra và sửa lỗi trước khi hoàn tất.

**Ví dụ HR:** Soạn thảo Job Description:
1. Viết bản nháp JD
2. Kiểm tra theo checklist (đủ yêu cầu, đúng tone)
3. Nếu thiếu → Bổ sung → Quay lại bước 2
4. Nếu đạt → Xuất bản cuối cùng

---

### 2.4 Giải phẫu một Workflow chuẩn

Một Workflow chuẩn gồm ba thành phần:

- **Mục tiêu rõ ràng (Ideal State Criteria):** Định nghĩa cụ thể thành phẩm cuối cùng trông như thế nào.
- **Micro-steps định tuyến:** Chia nhỏ vấn đề thành các bước tuần tự. Thay vì "Hãy đánh giá CV này", Workflow yêu cầu:
  1. Trích xuất các kỹ năng cứng.
  2. So sánh với Job Description.
  3. Cho điểm theo thang 1-10.
- **Cơ chế Checkpoint (Trạm kiểm duyệt):** Agent phải báo cáo và nhận sự phê duyệt (Approval) của con người trước khi chuyển sang bước tiếp theo. Đặc biệt quan trọng khi Agent chuẩn bị gửi email hay thay đổi dữ liệu.

---

### 2.5 Mẫu file Workflow thực tế

Trong Antigravity, Workflow là file Markdown với YAML frontmatter, lưu trong thư mục `.agent/workflows/`. Dưới đây là ví dụ đơn giản hóa:

```markdown
---
description: Quy trình sàng lọc CV ứng viên theo JD
---

# Workflow: Sàng lọc CV

## Bước 1: Thu thập dữ liệu
**Input:** Đọc file CV trong thư mục `01_Inputs/CVs/`
**Xử lý:**
- Trích xuất họ tên, số năm kinh nghiệm, kỹ năng chính
- Lưu kết quả tạm vào `02_Process/cv_extracted.csv`

## Bước 2: So sánh với JD
**Input:** File `01_Inputs/JD_MarketingManager.md` + kết quả Bước 1
**Xử lý:**
- Đối chiếu từng kỹ năng ứng viên với yêu cầu JD
- Cho điểm phù hợp trên thang 1-10

## Bước 3: Phân loại & Xuất kết quả
**Output:** Lưu file `03_Outputs/CV_Shortlist.csv`
- Điểm ≥ 7: Shortlist phỏng vấn
- Điểm 4-6: Chờ xét thêm
- Điểm < 4: Từ chối

## Checklist Kiểm tra
- [ ] Đã xử lý đủ tất cả CV chưa?
- [ ] Điểm số có khớp khi kiểm tra ngẫu nhiên 3 CV?
- [ ] File output đúng định dạng CSV?
```

Khi file này được lưu, người dùng chỉ cần gõ `/sang_loc_cv`, Agent sẽ thực hiện chính xác từng bước.

---

### 2.6 Vị trí lưu trữ

| Phạm vi | Vị trí | Ví dụ |
|---|---|---|
| **Global Workflows** (mọi dự án) | `~/.gemini/antigravity/global_workflows/` | `/dich_tai_lieu`, `/tom_tat_cuoc_hop` |
| **Workspace Workflows** (dự án cụ thể) | `Project/.agent/workflows/` | `/sang_loc_cv`, `/bao_cao_tuyen_dung` |

---

### 2.7 Đặc tính quan trọng

Workflow là quy trình **thủ công** — không tự chạy. Người dùng phải chủ động kích hoạt bằng lệnh slash (`/ten_workflow`). Điều này được thiết kế có chủ đích: cho phép người dùng kiểm soát và điều chỉnh trước khi Agent bắt đầu.

Workflow cũng **linh hoạt** — nó là "sườn bài", không phải "khuôn đúc". Bạn có thể yêu cầu Agent chạy Workflow nhưng bỏ qua bước 2, hoặc thay đổi nguồn dữ liệu đầu vào.

> 💡 **Dấu hiệu cần tiến lên Skill:** Workflow giải quyết bài toán hiệu suất (không cần giải thích lại quy trình). Nhưng khi bạn cần Agent **làm TỐT** chứ không chỉ "làm ĐÚNG thứ tự", đó là lúc cần Skill.
