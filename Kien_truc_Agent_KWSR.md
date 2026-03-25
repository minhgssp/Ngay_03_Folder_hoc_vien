# Kiến Trúc Cốt Lõi Của AI Agent — Khung KWSR

*Tài liệu chuyên sâu dành cho Ngày 3: Thiết Kế & Lắp Ráp Agent — Khóa Masterclass HR-AI.*
*Nguồn: SGK Antigravity Full v2, Chương 2.4 & Chương 3.*

---

## Tổng quan

Trong hệ sinh thái **Antigravity**, một AI Agent không chỉ là một chatbot trả lời câu hỏi đơn thuần. Nó được thiết kế và vận hành dựa trên một kiến trúc "não bộ" có cấu trúc, cho phép Agent có khả năng tự chủ, ghi nhớ, tuân thủ quy trình và đảm bảo an toàn.

Kiến trúc này được gọi là **Khung KWSR** — bốn trụ cột tạo nên năng lực hoàn chỉnh của một Agent:

|  Ký hiệu  | Tên      | Vai trò cốt lõi           | Câu hỏi trả lời                           |
| :---------: | --------- | ---------------------------- | --------------------------------------------- |
| **K** | Knowledge | Bộ nhớ & Ngữ cảnh        | Agent**biết gì** về doanh nghiệp?   |
| **W** | Workflow  | Thuật toán Thực thi       | Agent phải**làm theo thứ tự** nào? |
| **S** | Skill     | Gói Năng lực Chuyên môn | Làm sao để Agent**làm tốt nhất**? |
| **R** | Rule      | Rào cản & An toàn         | Agent**KHÔNG ĐƯỢC** làm gì?       |

Bốn trụ cột này không hoạt động riêng lẻ mà được kết nối theo một **Mô hình Tiến hóa** — lộ trình phát triển từ Agent "biết ít" đến Agent "chuyên gia đáng tin cậy".

Trong các phần tiếp theo, chúng ta sẽ đi sâu vào từng trụ cột.

# Bóc Tách Khái Niệm Lõi: Workflow, Skill và Rule

Trong hệ sinh thái quản lý agentic của Antigravity, việc nhầm lẫn giữa **Workflow (Quy trình)** và **Skill (Kỹ năng)** là nguyên nhân số một gây ra sự cồng kềnh, thiếu hiệu quả và khó bảo trì cho các Agent. Theo chuẩn kiến trúc sư hệ thống (Architecture Principles), chúng ta phải tuân thủ sự phân tách rạch ròi.

## 1. Workflow (Quy Trình Làm Việc)

**Workflow lả gì?**
Workflow trả lời cho câu hỏi: *"Làm cái gì, theo thứ tự nào?"*. Đây là một chuỗi các bước (step-by-step) mang tính "Thực thi" (Execution).

**Đặc điểm nhận diện:**

- Được người dùng (User) gọi ra một cách chủ động thông qua lệnh gạch chéo `/workflow-name`.
- Có tính tuần tự và cấu trúc ở cấp độ tiến trình (**Trajectory level**).
- Cho phép lồng ghép: Một workflow có thể gọi các workflow khác.
- Agent có khả năng tự động tạo Workflow từ lịch sử chat sau khi user làm mẫu thủ công.
- **Vị trí lưu trữ chuẩn:**
  - Cấp độ dự án (Workspace): `<workspace-root>/.agents/workflows/` (hoặc `.agent/workflows/`)
  - Cấp độ toàn cục (Global): `~/.gemini/antigravity/global_workflows/`

## 2. Skill (Kỹ Năng & Kiến Thức)

**Skill là gì?**
Skill trả lời cho câu hỏi: *"Làm như thế nào, chi tiết ra sao?"*. Đây là bộ nhớ học thuật, bao gồm định nghĩa, công thức, khuôn mẫu (templates), và các nguyên tắc chuyên sâu.

**Đặc điểm nhận diện:**

- Không chứa các bước quy trình từ 1 đến N.
- Được Agent (AI) tự động tải vào bộ nhớ (Implicit Trigger) dựa vào việc quét danh sách mô tả (description) trong YAML frontmatter để chọn Skill phù hợp.
- Một Skill có thể được tái sử dụng (reusability) bởi hàng chục Workflow hay Rule khác nhau.
- **Vị trí lưu trữ chuẩn:**
  - Cấp độ dự án (Workspace-specific): `<workspace-root>/.agent/skills/<skill-folder>/SKILL.md`
  - Cấp độ toàn cục (Global - all workspaces): `~/.gemini/antigravity/skills/<skill-folder>/SKILL.md`

## 3. Rules (Quy Tắc Ràng Buộc)

**Rule là gì?**
Trong khi Skill cung cấp kiến thức rộng và công cụ thực thi, **Rule** là các ràng buộc (Constraints) được định nghĩa thủ công để Agent phải tuân theo ở cấp độ **Prompt**. Khác biệt với Workflow (hoạt động ở cấp Trajectory), Rule thiết lập một bối cảnh bền vững (persistent context) cho hành vi của Agent.

**Đặc điểm nhận diện:**

- Giới hạn hệ thống: Tối đa 12.000 ký tự mỗi tệp.
- Cơ chế kích hoạt đa dạng:
  - Thủ công qua lệnh `@ten-file`
  - Always On (Luôn bật)
  - Áp dụng tự động theo định dạng file (`.js`, `src/**/*.ts`)
  - AI tự quyết định dựa theo mô tả (Model decision).
- **Vị trí lưu trữ chuẩn:**
  - Cấp độ dự án (Workspace rules): `<workspace-root>/.agent/rules/`
  - Cấp độ toàn cục (Global rules): `~/.gemini/GEMINI.md` (Áp dụng cho mọi workspaces)

---

> **Tóm lược Antigravity:** Người dùng gọi một Workflow. Workflow sẽ chỉ định tuần tự các hành động. Tại mỗi hành động, Agent sẽ tra cứu các Skill liên quan để biết cách làm, và tuân thủ các Rules bên trong Skill đó để không đi chệch đường ray.

---

## 1. 🧠 K — Knowledge (Kiến Thức & Chiều Sâu Context)

### 1.1 Định nghĩa

Knowledge là toàn bộ dữ liệu, thông tin ngữ cảnh, tài liệu, và lịch sử tương tác mà Agent có quyền truy cập. Không chỉ đơn thuần là "bộ nhớ", Knowledge trong Antigravity là **Hệ thống Ngữ cảnh Tích lũy** (Cumulative Context).

Nếu không có Knowledge vững chắc, Agent sẽ bị "mất trí nhớ tạm thời" hoặc rơi vào trạng thái **ảo giác** (Hallucination) — tức là bịa đặt thông tin nghe có vẻ đúng nhưng thực tế hoàn toàn sai.

---

### 1.2 Mô hình Ba Tầng Tri Thức

Tương tự bộ não con người có trí nhớ ngắn hạn và dài hạn, Agent trong Antigravity quản lý thông tin qua **ba cơ chế riêng biệt**:

| Tầng               | Quản lý bởi                | Thời hạn | Mục đích                                 | Vị trí trên máy                  |
| ------------------- | ----------------------------- | ---------- | ------------------------------------------- | ------------------------------------ |
| **Brain**     | 🤖 Hệ thống (Tự động)    | Ngắn hạn | Lưu vết lịch sử tương tác (log thô) | `~/.gemini/antigravity/brain/`     |
| **Knowledge** | 🤖 Hệ thống (Tự động)    | Dài hạn  | Tái sử dụng kinh nghiệm đã chắt lọc | `~/.gemini/antigravity/knowledge/` |
| **Database**  | ✋ Người dùng (Thủ công) | Dài hạn  | Tổ chức dữ liệu nguồn & sản phẩm     | Thư mục dự án do bạn tạo       |

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

| Hành động                                   | Cách thức                                                                                         |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Agent tự ghi nhớ sau mỗi phiên             | ✅**Tự động** — Knowledge Subagent chạy ngầm                                            |
| Bạn yêu cầu Agent lưu kiến thức cụ thể | ✅**Thủ công** — Nói: *"Hãy lưu quy trình này vào Knowledge để dùng lại sau."* |
| Cập nhật Knowledge cũ không còn phù hợp | ✅**Thủ công** — Hướng dẫn lại để Agent tạo phiên bản mới                        |

---

### 1.5 Ưu và Nhược điểm

**Thế mạnh:** Linh hoạt. Không cần chuẩn bị tài liệu phức tạp ngay từ đầu — chỉ cần bắt đầu làm việc và hệ thống tự học. Rất phù hợp giai đoạn đầu dự án khi mọi thứ chưa định hình.

**Hạn chế:** Thiếu tính nhất quán. Vì dựa trên kinh nghiệm cá nhân và ngữ cảnh cụ thể, tri thức này khó nhân bản cho người khác. Một Agent "hiểu ý" bạn chưa chắc làm việc tốt với đồng nghiệp của bạn.

> 💡 **Dấu hiệu cần tiến lên Workflow:** Khi bạn nhận thấy mình đang phải hướng dẫn Agent cùng một chuỗi hành động lặp đi lặp lại (trên 3 lần), đó là lúc Knowledge không đủ.

---

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

| Phạm vi                                         | Vị trí                                    | Ví dụ                                   |
| ------------------------------------------------ | ------------------------------------------- | ----------------------------------------- |
| **Global Workflows** (mọi dự án)        | `~/.gemini/antigravity/global_workflows/` | `/dich_tai_lieu`, `/tom_tat_cuoc_hop` |
| **Workspace Workflows** (dự án cụ thể) | `Project/.agent/workflows/`               | `/sang_loc_cv`, `/bao_cao_tuyen_dung` |

---

### 2.7 Đặc tính quan trọng

Workflow là quy trình **thủ công** — không tự chạy. Người dùng phải chủ động kích hoạt bằng lệnh slash (`/ten_workflow`). Điều này được thiết kế có chủ đích: cho phép người dùng kiểm soát và điều chỉnh trước khi Agent bắt đầu.

Workflow cũng **linh hoạt** — nó là "sườn bài", không phải "khuôn đúc". Bạn có thể yêu cầu Agent chạy Workflow nhưng bỏ qua bước 2, hoặc thay đổi nguồn dữ liệu đầu vào.

> 💡 **Dấu hiệu cần tiến lên Skill:** Workflow giải quyết bài toán hiệu suất (không cần giải thích lại quy trình). Nhưng khi bạn cần Agent **làm TỐT** chứ không chỉ "làm ĐÚNG thứ tự", đó là lúc cần Skill.

---

## 3. 🛠️ S — Skill (Gói Năng Lực Chuyên Môn Sâu)

### 3.1 Định nghĩa

Nếu Workflow trả lời câu hỏi "Làm bước nào trước, bước nào sau?", thì Skill trả lời câu hỏi **"Làm như thế nào mới là TỐT?"**.

Skill là các gói năng lực chuyên sâu, được đóng gói sẵn để Agent sử dụng khi cần giải quyết các bài toán phức tạp đòi hỏi chất lượng cao. Skill nâng cấp Agent từ cấp độ "Biết làm" lên cấp độ **"Bậc thầy"**.

---

### 3.2 Workflow vs. Skill — Bảng so sánh

| Khía cạnh           | Workflow                               | Skill                                                   |
| --------------------- | -------------------------------------- | ------------------------------------------------------- |
| **Câu hỏi**   | "Làm gì để hoàn thành?"          | "Làm sao để hoàn thành**xuất sắc**?"       |
| **Tập trung**  | Trình tự các bước (Procedure)     | Chất lượng thực hiện (Craftsmanship)               |
| **Mục tiêu**  | Ra được sản phẩm đúng yêu cầu | Ra sản phẩm với chất lượng cao nhất              |
| **Bản chất**  | Quy trình chuẩn hóa                 | Tinh hoa được**chắt lọc** từ quy trình     |
| **Kích hoạt** | Thủ công (gõ `/ten_workflow`)     | **Tự động** — Agent nhận diện và áp dụng |

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

---

## 4. 🛡️ R — Rule (Hệ Thống Rào Cản & Sự An Toàn)

### 4.1 Định nghĩa

Rule là tập hợp các giới hạn và quy định bắt buộc mà Agent phải tuân thủ trong mọi tình huống. Nó trả lời hai câu hỏi:

- **"Những điều gì KHÔNG ĐƯỢC PHÉP làm?"**
- **"Những nguyên tắc nào PHẢI tuân thủ tuyệt đối?"**

Rule là ranh giới sống còn (Guardrails). Khi trao quyền cho AI làm các việc quan trọng (như tuyển dụng, lương thưởng), thiếu Rule sẽ gây ra rủi ro tàn khốc (**Blast Radius** — vùng ảnh hưởng khi sai sót xảy ra).

**Ví dụ rủi ro thực tế:** Một Agent "quá nhiệt tình" có thể tự động gửi email từ chối 50 ứng viên mà chưa qua duyệt của Manager. Hậu quả: mất ứng viên tiềm năng, tổn hại thương hiệu tuyển dụng, vi phạm quy trình nội bộ.

---

### 4.2 Ba cấp độ Rào cản

#### Cấp 1: Behavioral Rules (Quy tắc Hành vi)

Quy định cách Agent giao tiếp và ứng xử.

- Bắt buộc giao tiếp bằng tiếng Việt chuyên nghiệp, không dùng từ ngữ lóng hoặc thiếu tôn trọng.
- Tuyệt đối không tự bịa đặt dữ liệu (**Zero Hallucination Tolerance**).
- Giữ đúng tone/voice của thương hiệu nhà tuyển dụng.

#### Cấp 2: Operational Rules (Quy tắc Vận hành)

Quy định cách Agent thao tác với hệ thống.

- **Circuit Breakers:** Nếu tìm kiếm tài liệu không thấy sau 3 lần, Agent phải dừng lại và hỏi, không được tự ý tiếp tục vô tận.
- **Read-Only Input:** Tuyệt đối không sửa file trong thư mục `01_Inputs/`.
- **Backup trước khi sửa:** Luôn tạo bản sao trước khi chỉnh sửa file quan trọng.

#### Cấp 3: Security Rules (Quy tắc Bảo mật)

Quy định về bảo vệ dữ liệu và quyền hạn.

- **Cấm** chia sẻ thông tin PII (Personally Identifiable Information) cho phòng ban không liên quan.
- **Human-in-the-loop:** Phải xin phép con người mỗi khi muốn xóa file hoặc gửi email tự động.
- **Không tiết lộ** lương, đánh giá cá nhân của ứng viên A cho ứng viên B.

---

### 4.3 Global Rule vs. Workspace Rule

Rule được phân thành hai cấp lưu trữ, với **quy tắc ưu tiên rõ ràng: Workspace luôn thắng Global**.

| Cấp                     | Vị trí                                       | Đặc điểm                                            |
| ------------------------ | ---------------------------------------------- | ------------------------------------------------------- |
| **Global Rule**    | `~/.gemini/GEMINI.md` (một file duy nhất)  | "Hiến pháp" — áp dụng mọi nơi, là sàn an toàn |
| **Workspace Rule** | `.agent/rules/` (nhiều file theo chủ đề) | "Luật dự án" — tùy chỉnh cho từng ngữ cảnh     |

**Mẫu Global Rule (`GEMINI.md`):**

```
- Luôn trả lời bằng tiếng Việt.
- TUYỆT ĐỐI KHÔNG xóa dữ liệu gốc (Input).
- TUYỆT ĐỐI KHÔNG chia sẻ PII ra ngoài workspace.
- Luôn hỏi trước khi thực hiện thao tác xóa.
```

**Mẫu Workspace Rule (`ke_toan.md`):**

```
- Định dạng số: Phân cách hàng nghìn bằng dấu chấm (.)
- Format ngày: DD/MM/YYYY
- Bắt buộc đối chiếu tổng phát sinh Nợ/Có
- Không xuất file kế toán ra ngoài thư mục dự án
```

**Nguyên tắc vàng:** Global Rule thiết lập "sàn an toàn"; Workspace **nên nâng cao** tiêu chuẩn, **không hạ thấp**.

---

### 4.4 Bốn chế độ Kích hoạt Rule

Không phải mọi Rule đều luôn cần bật. Antigravity hỗ trợ 4 chế độ:

| Chế độ                                | Mô tả                                       | Ví dụ                                                                   |
| ---------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------- |
| **Luôn bật** (Always On)         | Áp dụng mọi lúc, mọi nơi                | Quy ước đặt tên file, mã hóa UTF-8                                 |
| **Thủ công** (Manual)            | Chỉ bật khi người dùng gọi `@mention` | `@bao_mat` — chỉ nạp khi cần xử lý dữ liệu nhạy cảm           |
| **Tự động theo file** (Glob)    | Bật khi Agent mở file nhất định          | Mở `.xlsx` → Kích hoạt Rule format kế toán                        |
| **AI Tự quyết** (Model Decision) | Agent tự đánh giá ngữ cảnh và bật     | Rule "ứng xử khủng hoảng" bật khi phát hiện giọng điệu gay gắt |

---

### 4.5 Rule trong Quản trị Niềm tin

Trong giai đoạn đầu triển khai AI, tâm lý chung của quản lý là lo ngại. Rule chính là giải pháp kỹ thuật để chuyển từ trạng thái **"tin tưởng mù quáng"** sang **"tin tưởng có kiểm soát"**:

| Lo ngại             | Giải pháp Rule                      |
| -------------------- | ------------------------------------- |
| Mất dữ liệu       | Rule cấm xóa (Permissions)          |
| Sai lệch thông tin | Rule về nguồn dữ liệu (Grounding) |
| Văn phong máy móc | Rule về giọng văn (Persona)        |
| Rò rỉ thông tin   | Rule về PII và phạm vi chia sẻ    |

> 💡 **Hãy bắt đầu việc xây dựng Agent bằng việc soạn thảo file `GEMINI.md`**. Đó là nền móng vững chắc nhất cho một hệ thống AI phục vụ doanh nghiệp an toàn.

---

## 5. 🔄 Mô Hình Tiến Hóa Năng Lực Agent

### 5.1 Nghịch lý về sự trưởng thành

AI Agent rất thông minh trong việc trả lời câu hỏi, nhưng lại "non nớt" trong việc vận hành hệ thống. Tuần đầu bạn hướng dẫn chi tiết, Agent làm tốt. Tuần sau bạn nói "Làm báo cáo như cũ", Agent lại hỏi như người mới.

Vấn đề không nằm ở trí tuệ của AI, mà nằm ở **cơ chế kết tinh tri thức**. Agent cần một lộ trình để chuyển hóa từ xử lý rời rạc thành kinh nghiệm tái sử dụng.

---

### 5.2 Bốn giai đoạn Tiến hóa

Quá trình phát triển Agent tương ứng với bốn trụ cột KWSR:

| Giai đoạn                  | Tầng     | Trọng tâm               | Hành động HR                                                |
| ---------------------------- | --------- | ------------------------- | -------------------------------------------------------------- |
| **1. Discovery**       | Knowledge | Học hỏi, nạp dữ liệu | Upload quy chế nhân sự, danh sách nhân viên              |
| **2. Standardization** | Workflow  | Chuẩn hóa quy trình    | Tạo Workflow "6 bước sàng lọc CV"                         |
| **3. Specialization**  | Skill     | Nâng tầm chất lượng  | Đóng gói Skill "Phỏng vấn hành vi STAR"                  |
| **4. Control**         | Rule      | Bảo vệ & Kiểm soát    | Thiết lập Rule "Không tiết lộ lương ứng viên A cho B" |

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

| Loại can thiệp            | Biểu hiện                                            | Cần bổ sung |
| --------------------------- | ------------------------------------------------------ | ------------- |
| **Về ngữ cảnh**    | Agent không hiểu thuật ngữ, không tìm thấy file | → Knowledge  |
| **Về quy trình**    | Agent làm sai thứ tự, bỏ sót bước               | → Workflow   |
| **Về chất lượng** | Agent làm đúng nhưng kết quả xấu, sai format    | → Skill      |
| **Về an toàn**      | Agent làm việc nguy hiểm, rủi ro                   | → Rule       |

**Thang đo đánh giá:**

| Mức              | Giai đoạn | Cách quản lý                                                                   |
| ----------------- | ----------- | --------------------------------------------------------------------------------- |
| **< 70%**   | Học việc  | Giám sát chặt, hướng dẫn từng bước. Tập trung xây Knowledge.           |
| **70–90%** | Thạo việc | Giao việc theo quy trình, kiểm tra kết quả cuối. Tối ưu Workflow & Skill. |
| **> 90%**   | Chuyên gia | Giao quyền tự chủ cao. Quản trị bằng Rule, giám sát ngoại lệ.           |

---

### 5.5 Thứ tự ưu tiên KWSR theo ngành

Không phải ngành nào cũng bắt đầu từ Knowledge. Ngành có rủi ro cao cần xây **Rule trước**:

| Ngành                             | Thứ tự ưu tiên         | Lý do                                                         |
| ---------------------------------- | -------------------------- | -------------------------------------------------------------- |
| **HR**                       | K → W → S → R           | Cần nạp context trước, rủi ro ở mức trung bình         |
| **Marketing**                | K → W → S → R           | Sáng tạo cần context, quy trình đến sau                  |
| **Tài chính - Kế toán**  | **R → W → S** → K | Sai số = hậu quả tài chính, Rule phải có trước        |
| **Ngân hàng - Bảo hiểm** | **R → S → W** → K | Tuân thủ KYC/AML là bắt buộc, Skill chuyên môn cao      |
| **Pháp lý**                | **S → R** → K → W | Chất lượng phân tích pháp lý là yếu tố quyết định |

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
