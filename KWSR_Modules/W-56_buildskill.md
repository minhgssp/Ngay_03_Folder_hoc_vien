---
description: "🛠️ Skill Packaging & Evaluation Workflow — Quy trình tạo, đánh giá và cấu hình chuẩn 1 Skill mới."
---

<!-- doc_id: DOC-WFL-BUILDSKILL | version: 1.0.0 | last_modified: 2026-03-24 | owner: @AI_RM | tier: Tier-2 Task Workflow -->

# `/buildskill` — Quy trình Tạo & Tối ưu Skill

> **Owner:** AI_RM (A-01) hoặc các Agent thiết kế hệ thống.
> **Mục đích:** Hướng dẫn từng bước cách khởi tạo một Skill chuẩn Antigravity (Specification), tối ưu hóa luồng kích hoạt (Trigger rate), và đánh giá đầu ra (Eval-driven) liên tục.
> **Kiến thức lõi:** Vận dụng `Skill_Packaging_Master.md` tại `SP-260324-01-Skill-Packaging`.

---

## Boot Sequence

Khi lệnh `/buildskill [mode]` được gọi, Agent thực thi:
1. Xác nhận mode (BUILD, OPTIMIZE_TRIGGER, EVALUATE, OPTIMIZE_INSTRUCTION).
2. Tải ngữ cảnh phù hợp.
3. Chạy các bước tương ứng dưới đây.

---

## 🏗️ MODE: BUILD — Khởi tạo Skill Framework

**Hoàn cảnh:** Khi có một chuyên môn mới (Domain knowledge) cần đóng gói thành công cụ cho Agent.

### Quy trình:
1. **Khởi tạo thư mục:**
   - Tạo thư mục `c:\commandcenter\.agents\skills\[skill-name]`.
   - Các file cơ bản: `SKILL.md` (Bắt buộc).
   - Thư mục tùy chọn: `scripts/`, `references/`, `assets/`, `evals/`.
2. **Khởi tạo Frontmatter (`SKILL.md`):**
   - Đảm bảo có YAML metadata gồm: `name`, `description` (cực kỳ rõ ràng về "khi nào cần gọi").
3. **Draft Phần Thân (Body Content):**
   - **Start from real expertise:** Sử dụng quy trình đã được User kiểm chứng thay vì tự sáng tác ngẫu nhiên.
   - **Spend context wisely:** Cắt bỏ lý thuyết phổ thông. Đi thẳng vào vấn đề chứa gotchas.
   - **Mức độ kiểm soát:** 
     + *Linh hoạt (Freedom):* Dùng bullet point cho các task mở.
     + *Nghiêm ngặt (Prescriptive):* Dùng Code block và yêu cầu copy y hệt cho những lệnh rủi ro.
4. **Validation Bước Đầu:** Đảm bảo `SKILL.md` dưới 500 dòng. Kiến thức rườm rà → `references/`.

---

## ⚡ MODE: OPTIMIZE_TRIGGER — Tối ưu Mô tả Kích hoạt

**Hoàn cảnh:** Skill đã được Build xong (Draft), nhưng cần đảm bảo Agent sẽ nhận diện và triệu hồi nó ĐÚNG LÚC TRƯỚC khi mang đi Evaluate kết quả đầu ra.
*Một skill dù tốt đến đâu cũng vô dụng nếu không bao giờ được gọi kích hoạt.*

### Quy trình:
1. **Thiết kế Queries (`evals/eval_queries.json`):**
   - Viết ~20 prompt thực tế: 10 cái "Should-trigger" (Nên gọi skill này) và 10 cái "Near-misses" (Giống keyword nhưng KHÔNG nên gọi).
   - **Lưu ý:** Thử nghiệm với các prompt ẩn ý/khó (Ví dụ: "clean my customer files" thay vì lộ liễu "analyze CSV").
2. **Train/Validation Split:**
   - Chia ngẫu nhiên 60% dữ liệu làm tập *Train* (dùng để sửa mô tả), và 40% làm *Validation* (giữ kín chỉ để test chéo nhằm tránh Overfitting).
3. **Thử nghiệm Gọi Skill (Đo Lường Trigger Rate):**
   - Ném prompt cho Agent. Kiểm tra log xem Agent có load `SKILL.md` không.
   - Do tính phi tuyến (nondeterministic), mỗi query chạy 3 lần để lấy tỷ lệ % `trigger_rate`.
4. **Cập nhật `description` trong Frontmatter:**
   - **Imperative phrasing:** Đổi sang giọng ra lệnh: "Use this skill when..." thay vì "This skill does...". Nhấn mạnh Intent.
   - Giữ dưới mức 1024 ký tự.
   - Lặp lại bước 3 với tập Train cho đến khi Trigger Rate đạt kỳ vọng (>50%), sau đó test đối xứng bằng tập Validation set. Qua bài test mới chuyển sang khâu Eval Output.

---

## 🧪 MODE: EVALUATE — Đánh giá Đầu Ra Thực Tế (Eval-Driven)

**Hoàn cảnh:** Skill đã Trigger chính xác và đáng tin cậy. Nay cần kiểm định xem nội dung dạy việc của Skill có giúp Agent xử lý tốt hơn LLM tự thân không.

### Quy trình:
1. **Thiết kế Test Cases (`evals/evals.json`):**
   - Tạo 2-3 Test cases. `{ "id", "prompt", "expected_output", "files": [] }`.
2. **Khởi chạy Baseline (Without Skill):**
   - Mở Session mới (Không load skill). Gửi prompt → Lưu `without_skill/outputs/` và `timing.json`.
3. **Khởi chạy Thực nghiệm (With Skill):**
   - Mở Session truyền `SKILL.md` vào. Gửi cùng prompt → Lưu `with_skill/outputs/` và `timing.json`.
4. **Viết Assertions (Điều kiện chuẩn):**
   - Sau khi xem kết quả lần đầu, bổ sung các điều kiện định lượng vào `assertions`. (VD: "Có 3 gạch đầu dòng", "Valid JSON").
5. **Grading & Benchmark:**
   - Chấm điểm PASS/FAIL cho từng Assertion → `grading.json`.
   - Tổng hợp `benchmark.json` so sánh Delta (Tăng bao nhiêu Pass Rate? Tốn thêm bao nhiêu Token/Time?).

---

## 🛠️ MODE: OPTIMIZE_INSTRUCTION — Phân tích & Tối ưu Nội Dung Dạy Việc

**Hoàn cảnh:** Đã có Benchmark và Transcripts từ bước EVALUATE để thấy rõ lỗ hổng trong bản Draft nội dung.

### Quy trình:
1. **Đọc Feedback & Transcripts:**
   - Xóa `assertions` luôn pass bất kể có skill hay không (Skill không cấp thêm giá trị thực tiễn).
   - Phân tích Assertion liên tục FAIL để tìm ngõ cụt.
   - Đọc Human Feedback (`feedback.json`) để cải thiện định dạng, UX, Tone-of-Voice.
2. **Cập nhật `SKILL.md` Body:**
   - **Bundle Scripts:** Cứ thấy Agent tự sinh helper code thủ công (VD: data parser) ở nhiều run → Đóng gói code sẵn vào `scripts/helper.py` và chỉ cho Agent cách gọi.
   - **Explain the Why:** Nếu Agent vi phạm các luật cấm, hãy giải thích nguyên do "Tại sao cấm" thay vì chỉ in đậm.
   - **Generalize:** Khái quát hóa rule để áp dụng toàn cục, không patch lỗi tủn mủn cho 1 test case.
3. **Iteration mới:**
   - Chạy lại vòng EVALUATE ở thư mục `iteration-2/`. Dừng khi User hoàn toàn vừa ý.

---

## 🗂 Cấu Trúc Workspace Mẫu Toàn Diện

```text
[skill-name]/
├── SKILL.md
└── evals/
    ├── eval_queries.json       # Phục vụ OPTIMIZE_TRIGGER 
    └── evals.json              # Phục vụ EVALUATE Output

[skill-name]-workspace/
└── iteration-1/
    ├── eval-test-case-1/
    │   ├── with_skill/     (outputs/, timing.json, grading.json)
    │   └── without_skill/  (outputs/, timing.json, grading.json)
    ├── feedback.json
    └── benchmark.json
```
