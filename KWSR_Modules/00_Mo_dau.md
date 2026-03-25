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
>
