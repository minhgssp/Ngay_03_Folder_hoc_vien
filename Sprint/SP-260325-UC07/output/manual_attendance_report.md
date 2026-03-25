# BÁO CÁO ĐỐI SOÁT CHẤM CÔNG (THỦ CÔNG)
**Sprint:** SP-260325-UC07  
**Phương pháp:** Đối chiếu thủ công từng dòng  
**Dữ liệu:** 5 nhân viên × 5 ngày = 25 dòng  
**Quy tắc:** In ≤ 08:30 = OK | In > 08:30 = Late | Thiếu 1 chiều = Missing Punch | Trống cả 2 = Tra đơn phép

---

## Quá Trình Đối Soát Từng Dòng

### 🗓️ Ngày 01/03/2026

| # | EmpID | Tên | In | Out | Phân loại | Tra đơn? | Kết quả |
|---|-------|-----|-----|------|-----------|----------|---------|
| 1 | EMP001 | Nguyen Van Alpha | 08:25 | 17:35 | Đủ In/Out, In ≤ 08:30 | Không | ✅ `[OK]` |
| 2 | EMP002 | Tran Thi Beta | 08:30 | 17:40 | Đủ In/Out, In = 08:30 | Không | ✅ `[OK]` |
| 3 | EMP003 | Le Van Gamma | 08:45 | 17:30 | Đủ In/Out, In > 08:30 | Không | ⏰ `[Late]` — Check-in lúc 08:45 |
| 4 | EMP004 | Hoang Thi Delta | _(trống)_ | 17:30 | Thiếu In | Không | ⚠️ `[Missing Punch]` — Cần giải trình |
| 5 | EMP005 | Vu Van Epsilon | 08:15 | _(trống)_ | Thiếu Out | Không | ⚠️ `[Missing Punch]` — Cần giải trình |

### 🗓️ Ngày 02/03/2026

| # | EmpID | Tên | In | Out | Phân loại | Tra đơn? | Kết quả |
|---|-------|-----|-----|------|-----------|----------|---------|
| 6 | EMP001 | Nguyen Van Alpha | 08:20 | 17:45 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |
| 7 | EMP002 | Tran Thi Beta | 08:25 | 17:35 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |
| 8 | EMP003 | Le Van Gamma | 08:30 | 17:30 | Đủ, = 08:30 | Không | ✅ `[OK]` |
| 9 | EMP004 | Hoang Thi Delta | _(trống)_ | _(trống)_ | **Vắng hoàn toàn** | ✅ Có → L002: Sick Leave, **Approved** | 🟢 `[Paid Leave]` — Nghỉ ốm có phép |
| 10 | EMP005 | Vu Van Epsilon | 10:00 | 17:30 | Đủ, In > 08:30 | Không | ⏰ `[Late]` — Check-in lúc 10:00 |

### 🗓️ Ngày 03/03/2026

| # | EmpID | Tên | In | Out | Phân loại | Tra đơn? | Kết quả |
|---|-------|-----|-----|------|-----------|----------|---------|
| 11 | EMP001 | Nguyen Van Alpha | 08:10 | 18:00 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |
| 12 | EMP002 | Tran Thi Beta | 08:50 | 17:30 | Đủ, In > 08:30 | Không | ⏰ `[Late]` — Check-in lúc 08:50 |
| 13 | EMP003 | Le Van Gamma | _(trống)_ | _(trống)_ | **Vắng hoàn toàn** | ✅ Có → L001: Annual Leave, **Approved** | 🟢 `[Paid Leave]` — Nghỉ phép năm |
| 14 | EMP004 | Hoang Thi Delta | _(trống)_ | _(trống)_ | **Vắng hoàn toàn** | ✅ Có → L003: Sick Leave, **Approved** | 🟢 `[Paid Leave]` — Nghỉ ốm có phép |
| 15 | EMP005 | Vu Van Epsilon | 08:25 | 17:35 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |

### 🗓️ Ngày 04/03/2026

| # | EmpID | Tên | In | Out | Phân loại | Tra đơn? | Kết quả |
|---|-------|-----|-----|------|-----------|----------|---------|
| 16 | EMP001 | Nguyen Van Alpha | 08:22 | 17:33 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |
| 17 | EMP002 | Tran Thi Beta | 08:15 | 17:40 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |
| 18 | EMP003 | Le Van Gamma | 08:20 | 17:30 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |
| 19 | EMP004 | Hoang Thi Delta | 08:25 | 17:45 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |
| 20 | EMP005 | Vu Van Epsilon | _(trống)_ | _(trống)_ | **Vắng hoàn toàn** | ✅ Có → L004: Unpaid Leave, **Pending** | 🔴 `[Unpaid Leave]` — Đơn chưa duyệt |

### 🗓️ Ngày 05/03/2026

| # | EmpID | Tên | In | Out | Phân loại | Tra đơn? | Kết quả |
|---|-------|-----|-----|------|-----------|----------|---------|
| 21 | EMP001 | Nguyen Van Alpha | _(trống)_ | _(trống)_ | **Vắng hoàn toàn** | ✅ Có → L005: Annual Leave, **Approved** | 🟢 `[Paid Leave]` — Nghỉ phép năm |
| 22 | EMP002 | Tran Thi Beta | 08:10 | 17:30 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |
| 23 | EMP003 | Le Van Gamma | 08:25 | 17:35 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |
| 24 | EMP004 | Hoang Thi Delta | 08:20 | 17:40 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |
| 25 | EMP005 | Vu Van Epsilon | 08:15 | 17:30 | Đủ, ≤ 08:30 | Không | ✅ `[OK]` |

---

## Bảng Tổng Hợp Cuối Cùng (Dạng Final Report)

| EmpID | EmpName | Date | CheckIn | CheckOut | LeaveType | ApprovalStatus | Final_Status |
|-------|---------|------|---------|----------|-----------|----------------|-------------|
| EMP001 | Nguyen Van Alpha | 2026-03-01 | 08:25 | 17:35 | | | [OK] Ngày công chuẩn |
| EMP002 | Tran Thi Beta | 2026-03-01 | 08:30 | 17:40 | | | [OK] Ngày công chuẩn |
| EMP003 | Le Van Gamma | 2026-03-01 | 08:45 | 17:30 | | | [Late] Đi trễ (Check-in lúc 08:45) |
| EMP004 | Hoang Thi Delta | 2026-03-01 | | 17:30 | | | [Missing Punch] Thiếu dữ liệu thẻ (Cần giải trình) |
| EMP005 | Vu Van Epsilon | 2026-03-01 | 08:15 | | | | [Missing Punch] Thiếu dữ liệu thẻ (Cần giải trình) |
| EMP001 | Nguyen Van Alpha | 2026-03-02 | 08:20 | 17:45 | | | [OK] Ngày công chuẩn |
| EMP002 | Tran Thi Beta | 2026-03-02 | 08:25 | 17:35 | | | [OK] Ngày công chuẩn |
| EMP003 | Le Van Gamma | 2026-03-02 | 08:30 | 17:30 | | | [OK] Ngày công chuẩn |
| EMP004 | Hoang Thi Delta | 2026-03-02 | | | Sick Leave | Approved | [Paid Leave] Nghỉ có phép (Sick Leave) |
| EMP005 | Vu Van Epsilon | 2026-03-02 | 10:00 | 17:30 | | | [Late] Đi trễ (Check-in lúc 10:00) |
| EMP001 | Nguyen Van Alpha | 2026-03-03 | 08:10 | 18:00 | | | [OK] Ngày công chuẩn |
| EMP002 | Tran Thi Beta | 2026-03-03 | 08:50 | 17:30 | | | [Late] Đi trễ (Check-in lúc 08:50) |
| EMP003 | Le Van Gamma | 2026-03-03 | | | Annual Leave | Approved | [Paid Leave] Nghỉ có phép (Annual Leave) |
| EMP004 | Hoang Thi Delta | 2026-03-03 | | | Sick Leave | Approved | [Paid Leave] Nghỉ có phép (Sick Leave) |
| EMP005 | Vu Van Epsilon | 2026-03-03 | 08:25 | 17:35 | | | [OK] Ngày công chuẩn |
| EMP001 | Nguyen Van Alpha | 2026-03-04 | 08:22 | 17:33 | | | [OK] Ngày công chuẩn |
| EMP002 | Tran Thi Beta | 2026-03-04 | 08:15 | 17:40 | | | [OK] Ngày công chuẩn |
| EMP003 | Le Van Gamma | 2026-03-04 | 08:20 | 17:30 | | | [OK] Ngày công chuẩn |
| EMP004 | Hoang Thi Delta | 2026-03-04 | 08:25 | 17:45 | | | [OK] Ngày công chuẩn |
| EMP005 | Vu Van Epsilon | 2026-03-04 | | | Unpaid Leave | Pending | [Unpaid Leave] Nghỉ không phép (Không ghi nhận thẻ) |
| EMP001 | Nguyen Van Alpha | 2026-03-05 | | | Annual Leave | Approved | [Paid Leave] Nghỉ có phép (Annual Leave) |
| EMP002 | Tran Thi Beta | 2026-03-05 | 08:10 | 17:30 | | | [OK] Ngày công chuẩn |
| EMP003 | Le Van Gamma | 2026-03-05 | 08:25 | 17:35 | | | [OK] Ngày công chuẩn |
| EMP004 | Hoang Thi Delta | 2026-03-05 | 08:20 | 17:40 | | | [OK] Ngày công chuẩn |
| EMP005 | Vu Van Epsilon | 2026-03-05 | 08:15 | 17:30 | | | [OK] Ngày công chuẩn |

---

## Thống Kê Tổng Quan

| Trạng thái | Số lượng | Tỷ lệ |
|-----------|---------|-------|
| ✅ [OK] Ngày công chuẩn | 15 | 60% |
| ⏰ [Late] Đi trễ | 3 | 12% |
| ⚠️ [Missing Punch] Quên quẹt thẻ | 2 | 8% |
| 🟢 [Paid Leave] Nghỉ có phép | 4 | 16% |
| 🔴 [Unpaid Leave] Nghỉ không phép | 1 | 4% |
| **Tổng** | **25** | **100%** |
