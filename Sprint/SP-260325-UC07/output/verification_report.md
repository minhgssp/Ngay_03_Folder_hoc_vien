# BIÊN BẢN ĐỐI CHIẾU THỦ CÔNG — KẾT QUẢ VS. DỮ LIỆU GỐC

**Mục đích:** Kiểm tra từng dòng trong `final_attendance_report.csv` có khớp chính xác với dữ liệu gốc (`raw_attendance.csv` + `leave_requests.csv`) hay không.

**Phương pháp:** So sánh từng cặp giá trị (dòng output ↔ dòng gốc). Ghi PASS ✅ hoặc FAIL ❌.

---

## Kiểm tra #1: EmpID, EmpName, Date, CheckIn, CheckOut có khớp với raw_attendance.csv?

| Dòng | EmpID | Date | In (gốc) | In (kết quả) | Out (gốc) | Out (kết quả) | Khớp? |
|------|-------|------|-----------|---------------|------------|----------------|-------|
| 2 | EMP001 | 03-01 | 08:25 | 08:25 | 17:35 | 17:35 | ✅ |
| 3 | EMP002 | 03-01 | 08:30 | 08:30 | 17:40 | 17:40 | ✅ |
| 4 | EMP003 | 03-01 | 08:45 | 08:45 | 17:30 | 17:30 | ✅ |
| 5 | EMP004 | 03-01 | _(trống)_ | _(trống)_ | 17:30 | 17:30 | ✅ |
| 6 | EMP005 | 03-01 | 08:15 | 08:15 | _(trống)_ | _(trống)_ | ✅ |
| 7 | EMP001 | 03-02 | 08:20 | 08:20 | 17:45 | 17:45 | ✅ |
| 8 | EMP002 | 03-02 | 08:25 | 08:25 | 17:35 | 17:35 | ✅ |
| 9 | EMP003 | 03-02 | 08:30 | 08:30 | 17:30 | 17:30 | ✅ |
| 10 | EMP004 | 03-02 | _(trống)_ | _(trống)_ | _(trống)_ | _(trống)_ | ✅ |
| 11 | EMP005 | 03-02 | 10:00 | 10:00 | 17:30 | 17:30 | ✅ |
| 12 | EMP001 | 03-03 | 08:10 | 08:10 | 18:00 | 18:00 | ✅ |
| 13 | EMP002 | 03-03 | 08:50 | 08:50 | 17:30 | 17:30 | ✅ |
| 14 | EMP003 | 03-03 | _(trống)_ | _(trống)_ | _(trống)_ | _(trống)_ | ✅ |
| 15 | EMP004 | 03-03 | _(trống)_ | _(trống)_ | _(trống)_ | _(trống)_ | ✅ |
| 16 | EMP005 | 03-03 | 08:25 | 08:25 | 17:35 | 17:35 | ✅ |
| 17 | EMP001 | 03-04 | 08:22 | 08:22 | 17:33 | 17:33 | ✅ |
| 18 | EMP002 | 03-04 | 08:15 | 08:15 | 17:40 | 17:40 | ✅ |
| 19 | EMP003 | 03-04 | 08:20 | 08:20 | 17:30 | 17:30 | ✅ |
| 20 | EMP004 | 03-04 | 08:25 | 08:25 | 17:45 | 17:45 | ✅ |
| 21 | EMP005 | 03-04 | _(trống)_ | _(trống)_ | _(trống)_ | _(trống)_ | ✅ |
| 22 | EMP001 | 03-05 | _(trống)_ | _(trống)_ | _(trống)_ | _(trống)_ | ✅ |
| 23 | EMP002 | 03-05 | 08:10 | 08:10 | 17:30 | 17:30 | ✅ |
| 24 | EMP003 | 03-05 | 08:25 | 08:25 | 17:35 | 17:35 | ✅ |
| 25 | EMP004 | 03-05 | 08:20 | 08:20 | 17:40 | 17:40 | ✅ |
| 26 | EMP005 | 03-05 | 08:15 | 08:15 | 17:30 | 17:30 | ✅ |

**Kết quả: 25/25 dòng KHỚP ✅**

---

## Kiểm tra #2: Các trường hợp vắng có đúng đơn phép trong leave_requests.csv?

Có 5 dòng vắng hoàn toàn (trống cả In & Out). Đối chiếu lần lượt:

| Dòng | EmpID | Date | LeaveType (kết quả) | Tra leave_requests.csv | Khớp? |
|------|-------|------|---------------------|------------------------|-------|
| 10 | EMP004 | 03-02 | Sick Leave, Approved | L002: EMP004, 2026-03-02, Sick Leave, Approved | ✅ |
| 14 | EMP003 | 03-03 | Annual Leave, Approved | L001: EMP003, 2026-03-03, Annual Leave, Approved | ✅ |
| 15 | EMP004 | 03-03 | Sick Leave, Approved | L003: EMP004, 2026-03-03, Sick Leave, Approved | ✅ |
| 21 | EMP005 | 03-04 | Unpaid Leave, Pending | L004: EMP005, 2026-03-04, Unpaid Leave, Pending | ✅ |
| 22 | EMP001 | 03-05 | Annual Leave, Approved | L005: EMP001, 2026-03-05, Annual Leave, Approved | ✅ |

**Kết quả: 5/5 đơn phép KHỚP ✅**

---

## Kiểm tra #3: Logic phân loại Final_Status có đúng quy tắc?

| Quy tắc | Các dòng áp dụng | Kiểm tra | Kết quả |
|---------|-------------------|----------|---------|
| Có đủ In ≤ 08:30 & Out → `[OK]` | 2,3,7,8,9,12,16,17,18,19,20,23,24,25,26 (15 dòng) | In đều ≤ 08:30, Out có giá trị | ✅ 15/15 |
| In > 08:30 & có Out → `[Late]` | 4 (08:45), 11 (10:00), 13 (08:50) | In > 08:30 đúng cả 3 | ✅ 3/3 |
| Thiếu 1 chiều In hoặc Out → `[Missing Punch]` | 5 (thiếu In), 6 (thiếu Out) | Đúng cả 2 trường hợp | ✅ 2/2 |
| Trống cả 2 + đơn Approved → `[Paid Leave]` | 10, 14, 15, 22 | Cả 4 có đơn Approved | ✅ 4/4 |
| Trống cả 2 + đơn Pending → `[Unpaid Leave]` | 21 | L004 đúng Pending | ✅ 1/1 |

**Kết quả: 25/25 dòng phân loại ĐÚNG ✅**

---

## KẾT LUẬN ĐỐI CHIẾU

| Hạng mục | Kết quả |
|---------|---------|
| Dữ liệu chấm công (In/Out) khớp file gốc | ✅ 25/25 |
| Đơn phép khớp file gốc | ✅ 5/5 |
| Logic phân loại Final_Status đúng quy tắc | ✅ 25/25 |
| **TỔNG KẾT** | **✅ PASS — Không có sai lệch** |
