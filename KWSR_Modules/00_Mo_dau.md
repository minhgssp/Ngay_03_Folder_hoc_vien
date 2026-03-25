# Kiến Trúc Cốt Lõi Của AI Agent — Khung KWSR

*Tài liệu chuyên sâu dành cho Ngày 3: Thiết Kế & Lắp Ráp Agent — Khóa Masterclass HR-AI.*
*Nguồn: SGK Antigravity Full v2, Chương 2.4 & Chương 3.*

---

## Tổng quan

Trong hệ sinh thái **Antigravity**, một AI Agent không chỉ là một chatbot trả lời câu hỏi đơn thuần. Nó được thiết kế và vận hành dựa trên một kiến trúc "não bộ" có cấu trúc, cho phép Agent có khả năng tự chủ, ghi nhớ, tuân thủ quy trình và đảm bảo an toàn.

Kiến trúc này được gọi là **Khung KWSR** — bốn trụ cột tạo nên năng lực hoàn chỉnh của một Agent:

| Ký hiệu | Tên | Vai trò cốt lõi | Câu hỏi trả lời |
|:---:|---|---|---|
| **K** | Knowledge | Bộ nhớ & Ngữ cảnh | Agent **biết gì** về doanh nghiệp? |
| **W** | Workflow | Thuật toán Thực thi | Agent phải **làm theo thứ tự** nào? |
| **S** | Skill | Gói Năng lực Chuyên môn | Làm sao để Agent **làm tốt nhất**? |
| **R** | Rule | Rào cản & An toàn | Agent **KHÔNG ĐƯỢC** làm gì? |

Bốn trụ cột này không hoạt động riêng lẻ mà được kết nối theo một **Mô hình Tiến hóa** — lộ trình phát triển từ Agent "biết ít" đến Agent "chuyên gia đáng tin cậy".

Trong các phần tiếp theo, chúng ta sẽ đi sâu vào từng trụ cột.
