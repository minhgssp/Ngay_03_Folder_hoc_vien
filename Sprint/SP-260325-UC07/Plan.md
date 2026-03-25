# Kế Hoạch Triển Khai & Khám Phá Dữ Liệu

---

## 🔍 PHẦN 1: KHÁM PHÁ DỮ LIỆU

### File 1: `raw_attendance.csv` — Dữ liệu máy chấm công

**Tổng quan:** 25 dòng dữ liệu = 5 nhân viên × 5 ngày (01–05/03/2026)

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| `EmpID` | Text | Mã nhân viên (EMP001–EMP005) — **khóa liên kết** |
| `EmpName` | Text | Họ tên |
| `Date` | Date | Ngày chấm công |
| `CheckIn_Time` | Time | Giờ vào (có thể trống) |
| `CheckOut_Time` | Time | Giờ ra (có thể trống) |
| `Machine_Location` | Text | Vị trí máy chấm |

**Bất thường phát hiện:**
- 5 trường hợp **vắng hoàn toàn** (trống cả In & Out): EMP004 ngày 02, EMP003 ngày 03, EMP004 ngày 03, EMP005 ngày 04, EMP001 ngày 05
- 2 trường hợp **quên quẹt thẻ** (thiếu 1 chiều): EMP004 ngày 01 (thiếu In), EMP005 ngày 01 (thiếu Out)
- 2 trường hợp **đi trễ** rõ rệt: EMP003 ngày 01 (08:45), EMP005 ngày 02 (10:00), EMP002 ngày 03 (08:50)

### File 2: `leave_requests.csv` — Đơn xin nghỉ

**Tổng quan:** 5 đơn nghỉ

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| `LeaveID` | Text | Mã đơn (L001–L005) |
| `EmpID` | Text | Mã nhân viên — **khóa liên kết** |
| `LeaveDate` | Date | Ngày xin nghỉ |
| `LeaveType` | Text | Loại phép (Annual / Sick / Unpaid) |
| `ApprovalStatus` | Text | Trạng thái duyệt (Approved / Pending) |
| `Reason` | Text | Lý do |

**Chi tiết:**
| Đơn | NV | Ngày nghỉ | Loại | Trạng thái |
|------|-----|-----------|------|-----------|
| L001 | EMP003 | 03/03 | Annual Leave | ✅ Approved |
| L002 | EMP004 | 02/03 | Sick Leave | ✅ Approved |
| L003 | EMP004 | 03/03 | Sick Leave | ✅ Approved |
| L004 | EMP005 | 04/03 | Unpaid Leave | ⏳ Pending |
| L005 | EMP001 | 05/03 | Annual Leave | ✅ Approved |

### File mẫu đầu ra: `Final_Attendance_Report.xlsx`

**Cấu trúc:** 8 cột — bổ sung 3 cột so với file chấm công gốc:

| Cột gốc | Cột bổ sung |
|---------|-------------|
| EmpID, EmpName, Date, CheckIn_Time, CheckOut_Time | **LeaveType**, **ApprovalStatus**, **Final_Status** |

**5 trạng thái Final_Status:**
| Tag | Ý nghĩa | Điều kiện |
|-----|---------|-----------|
| `[OK]` | Ngày công chuẩn | Có In ≤ 08:30 & có Out |
| `[Late]` | Đi trễ | In > 08:30 |
| `[Missing Punch]` | Thiếu dữ liệu thẻ | Thiếu In HOẶC Out (nhưng không thiếu cả 2) |
| `[Paid Leave]` | Nghỉ có phép | Vắng cả 2 + có đơn Approved |
| `[Unpaid Leave]` | Nghỉ không phép | Vắng cả 2 + đơn Pending hoặc không có đơn |

---

## 🧠 PHẦN 2: TƯ DUY LOGIC (THINK OUT LOUD)

### Nếu làm thủ công, tôi sẽ làm thế nào?

**Bước 1 — Lấy bảng chấm công làm xương sống:**
Bảng `raw_attendance.csv` có 25 dòng = 25 lượt chấm công. Mỗi dòng = 1 nhân viên × 1 ngày. Đây chính là "khung xương" của bảng kết quả — mỗi dòng input → đúng 1 dòng output.

**Bước 2 — Phân loại từng dòng theo 3 nhánh:**
Với mỗi dòng, tôi nhìn vào `CheckIn_Time` và `CheckOut_Time`:
- **Nhánh A**: Có đủ cả In lẫn Out → Kiểm tra In có > 08:30 không:
  - ≤ 08:30 → `[OK]`
  - > 08:30 → `[Late]`
- **Nhánh B**: Thiếu 1 trong 2 (In hoặc Out) → `[Missing Punch]`
- **Nhánh C**: Trống cả In lẫn Out → Nhân viên không quẹt thẻ → Sang Bước 3

**Bước 3 — Đối chiếu với bảng Đơn phép (chỉ cho Nhánh C):**
Lấy `EmpID` + `Date` của dòng đang xét, tra trong `leave_requests.csv`:
- Tìm thấy đơn **Approved** → Ghi `[Paid Leave]` + copy LeaveType
- Tìm thấy đơn **Pending** → Ghi `[Unpaid Leave]`
- Không tìm thấy đơn nào → Ghi `[Unpaid Leave]` (vắng không phép thuần túy)

**Bước 4 — Gộp thành bảng kết quả:**
Ghép thêm 3 cột (LeaveType, ApprovalStatus, Final_Status) vào bảng gốc → Xuất file.

### Tóm lại: Phép JOIN rất đơn giản

Bản chất toàn bộ bài toán là **LEFT JOIN** bảng chấm công với bảng đơn phép trên cặp khóa `(EmpID, Date)`, rồi áp dụng bộ quy tắc IF/ELSE lên kết quả join để sinh cột `Final_Status`.

---

## 📅 PHẦN 3: KẾ HOẠCH TRIỂN KHAI

### Phase 1: Phân tích & Xác nhận Logic
- [x] Đọc và mô tả cấu trúc 2 file CSV
- [x] Nghiên cứu file output mẫu `Final_Attendance_Report.xlsx`
- [x] Trình bày tư duy logic (Think Out Loud)
- [x] User xác nhận logic đúng → chuyển Phase 2

### Phase 2: Đối soát thủ công (Manual Testing)
- [x] Thực hiện đối soát "bằng tay" cho 25 dòng dữ liệu
- [x] Xuất bảng kết quả đối soát để User so sánh với file mẫu
- [x] Đối chiếu thủ công lại kết quả với file gốc (Pass 100%)

### Phase 3: Tự động hóa (Automation) ← **ĐANG Ở ĐÂY**
- [ ] Đề xuất 3 phương án tự động hóa
- [ ] Triển khai công cụ User chọn

### Phase 4: Tổng kết & Đóng gói
- [ ] Xuất báo cáo kết quả
- [ ] Đóng gói quy trình tái sử dụng

---

## ⚙️ PHẦN 4: ĐỀ XUẤT 3 PHƯƠNG ÁN TỰ ĐỘNG HÓA

Tháng sau số lượng nhân sự sẽ tăng lên rất nhiều, đối soát thủ công không còn khả thi. Dưới đây là 3 phương án tự động hóa quy trình này, từ cấp độ dễ (Agent-based) đến khó (Software-based).

### Phương án 1 (PA1): Prompt Automation (Dùng AI 100%)
- **Cách thức:** Đóng gói toàn bộ logic (4 bước ở Phần 2) thành một "System Prompt Template" chuẩn. Mỗi tháng, anh chỉ cần gom 2 file CSV vào một file Excel duy nhất rồi upload lên khung chat kèm câu Prompt này. AI sẽ tự đọc, tự phân tích và trả về kết quả ngay trên chat.
- **Ưu điểm:** Cực kỳ dễ làm, không cần biết dòng code nào. Rất linh hoạt nếu chính sách nhân sự (giờ làm, quy định trễ) thay đổi liên tục.
- **Nhược điểm:** Phụ thuộc vào giới hạn token của AI. Giới hạn khoảng ~500 dòng dữ liệu, nếu file quá lớn AI sẽ bị "ngộp" hoặc bỏ sót dữ liệu. Thay vì xử lý 5000 nhân viên, AI có thể bỏ sót.

### Phương án 2 (PA2): Hybrid (Code Python + AI Chat)
- **Cách thức:** Tách quy trình làm 2 chặng:
  - **Chặng 1 (Code):** Viết 1 script Python gọi là `attendance_matcher.py`. Script này "gánh" phần việc nặng nhọc nhất là Data Cleaning (làm sạch giờ) và VLOOKUP trộn 2 file CSV lại với nhau thành 1 bảng duy nhất (Merge Data).
  - **Chặng 2 (AI Chat Prompt):** Từ bảng đã gộp, anh sử dụng một Prompt chuẩn, đưa file lên AI để AI chỉ tập trung suy luận (Scoring) các ca vi phạm phức tạp.
- **Ưu điểm:** Khắc phục điểm yếu giới hạn dữ liệu, chạy mượt cho file 10.000 dòng. AI chỉ làm phần trí tuệ là đưa ra quyết định dựa trên bảng đã sạch, không phải làm phần chân tay là gom dữ liệu (giảm token tiêu thụ). Vẫn giữ được đặc tính linh hoạt của Prompt (rất hợp cho HR).
- **Nhược điểm:** Cần cài Python. Phải thực hiện quy trình chạy thành 2 bước rời rạc.

### Phương án 3 (PA3): Software UI (Phần mềm tự động 100%)
- **Cách thức:** Lập trình hẳn một phần mềm có giao diện người dùng (Desktop App dùng Python Tkinter hoặc PyQt) có tên `attendance_matcher_gui.py`. Giao diện có nút "Tải file Chấm Công", "Tải file Đơn Phép", và cái nút "Xử lý & Xuất Excel". Bấm 1 cái là AI nhúng sẵn trong code tự xử lý và nôn ra thẳng file Result. Cứng hóa 100% logic đã chốt ở Phần 2.
- **Ưu điểm:** Sang xịn mịn, "bấm nút là xong". Tiện dụng bảo mật. Giải phóng hoàn toàn sức người.
- **Nhược điểm:** Mất tính linh hoạt. Nếu tháng sau thay chính sách, anh phải nhờ AI sửa lại Mã nguồn (code), chứ không thể gõ chat thêm quy định như P1, P2. Dễ xảy ra lỗi môi trường khi máy tính nhân viên thay đổi.

### 💡 Gợi ý lựa chọn từ AI:
Trong tình huống của anh, nếu tháng sau có rất nhiều nhân sự đối soát lớn, **Phương án 2 (PA2 - Hybrid)** hoặc **Phương án 3 (PA3 - Software UI)** sẽ là lý tưởng nhất.

Tuy nhiên, nếu anh thích sự tiện dụng và thấy 2 file .py (`attendance_matcher_gui` và `attendance_matcher`) đã lưu trong Workspace, em cũng có thể kích hoạt PA3 cho anh test thử.

**Anh chọn phương án nào (1, 2 hay 3) để em "đóng gói" triển khai ạ?**
