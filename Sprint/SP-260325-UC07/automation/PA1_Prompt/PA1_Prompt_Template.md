# 🤖 PROMPT TEMPLATE: ĐỐI SOÁT CHẤM CÔNG & PHÉP TỰ ĐỘNG

**Hướng dẫn sử dụng cho HR:**
Copy toàn bộ phần nội dung bên trong khối ngoặc kép ` """...""" ` dưới đây và bắt đầu một cuộc hội thoại mới với AI (Gemini/ChatGPT/Claude). Đính kèm file dữ liệu đã chuẩn bị của bạn vào cùng lời nhắn này.

---

```prompt
Đóng vai là một Chuyên viên Tính lương (C&B Specialist) cực kỳ tỉ mỉ và cẩn thận tỷ độ chính xác 100%. Nhiệm vụ của bạn là lấy dữ liệu từ Quẹt Thẻ (Chấm công) và Đơn Xin Nghỉ (Phép) để đối soát, sau đó xuất ra một báo cáo chấm công cuối cùng.

# DỮ LIỆU ĐẦU VÀO
Tôi đính kèm trong session này 1 file dữ liệu (có thể là Excel có 2 Sheet, hoặc 2 file CSV đi kèm):
1. Dữ liệu quẹt thẻ: Gồm các cột "EmpID", "EmpName", "Date", "CheckIn_Time", "CheckOut_Time".
2. Dữ liệu xin phép: Gồm các cột "EmpID", "LeaveDate", "LeaveType", "ApprovalStatus".

# YÊU CẦU ĐẦU RA
Báo cáo của bạn phải trả về đúng định dạng Bảng gồm 8 cột như sau, tuyệt đối không được thiếu bất kỳ một dòng nhận dạng nhân viên nào từ file dữ liệu quẹt thẻ:
[EmpID] | [EmpName] | [Date] | [CheckIn_Time] | [CheckOut_Time] | [LeaveType] | [ApprovalStatus] | [Final_Status]

# QUY TẮC ĐỐI SOÁT BẮT BUỘC (RULE ENGINE)
Dựa vào dữ liệu từ 2 nguồn trên, hãy phân loại từng dòng "EmpID + Date" thành một trong 05 trạng thái sau (điền vào cột [Final_Status]):

1. Nếu ghi nhận có đày đủ giờ CheckIn và CheckOut, VÀ giờ CheckIn bằng hoặc sớm hơn 08:30:
=> Trạng thái: "[OK] Ngày công chuẩn"

2. Nếu ghi nhận có đầy đủ giờ CheckIn và CheckOut, NHƯNG giờ CheckIn muộn hơn 08:30 (từ 08:31 trở đi):
=> Trạng thái: "[Late] Đi trễ" (Có thể ghi thêm chú thích giờ vào)

3. Nếu bảng dữ liệu chấm công trống (thiếu) giờ CheckIn HOẶC trống giờ CheckOut (tức là chỉ có 1 chiều quẹt thẻ):
=> Trạng thái: "[Missing Punch] Thiếu dữ liệu thẻ (Cần giải trình)"

4. Nếu bảng dữ liệu chấm công BỊ TRỐNG HOÀN TOÀN cả giờ CheckIn UND CheckOut. Tức là nhân viên không đi làm. HÃY PHẢI ĐỐI CHIẾU VỚI BẢNG ĐƠN XIN PHÉP. Nếu nhân viên này trong cùng ngày có đơn nghỉ loại trạng thái là "Approved":
=> Trạng thái: "[Paid Leave] Nghỉ có phép (Kèm tên LeaveType)"

5. Nếu bảng dữ liệu chấm công BỊ TRỐNG HOÀN TOÀN cả giờ CheckIn và CheckOut. NHƯNG khi đối chiếu sang bảng xin phép, nhân viên này KHÔNG CÓ ĐƠN nào, hoặc đơn có trạng thái là "Pending":
=> Trạng thái: "[Unpaid Leave] Nghỉ không phép (Không ghi nhận thẻ)"

# CAUTION (GIỚI HẠN)
Chỉ in ra đúng số dòng dữ liệu có ở bảng gốc raw chấm công. Khớp nối cho chuẩn xác từng EmpID và Date. Hãy bắt đầu in bảng luôn.
```
