import pandas as pd
import os
from datetime import datetime

def determine_attendance_status(row):
    """
    Xử lý logic 5 nhánh chấm công dựa trên dữ liệu Vân Tay và Hệ thống Phép
    """
    has_checkin = pd.notna(row['CheckIn_Time'])
    has_checkout = pd.notna(row['CheckOut_Time'])
    has_approved_leave = pd.notna(row['ApprovalStatus']) and row['ApprovalStatus'].lower() == 'approved'
    
    # Nhánh 1: Vắng mặt hoàn toàn
    if not has_checkin and not has_checkout:
        if has_approved_leave:
            return f"[Paid Leave] Nghỉ có phép ({row['LeaveType']})"
        else:
            return "[Unpaid Leave] Nghỉ không phép (Không ghi nhận thẻ)"
            
    # Nhánh 2: Quên quẹt thẻ (Chỉ có CheckIn hoặc CheckOut)
    if not has_checkin or not has_checkout:
        return "[Missing Punch] Thiếu dữ liệu thẻ (Cần giải trình)"
        
    # Nhánh 3: Đầy đủ thẻ -> Kiểm tra giờ (Chuẩn Check-in: 08:30, Check-out: 17:30)
    try:
        checkin_t = datetime.strptime(str(row['CheckIn_Time']), '%H:%M').time()
        checkout_t = datetime.strptime(str(row['CheckOut_Time']), '%H:%M').time()
        standard_in = datetime.strptime('08:31', '%H:%M').time()
        standard_out = datetime.strptime('17:30', '%H:%M').time()
        
        if checkin_t >= standard_in:
            return f"[Late] Đi trễ (Check-in lúc {checkin_t.strftime('%H:%M')})"
        elif checkout_t < standard_out:
            return f"[Early Leave] Về sớm (Check-out lúc {checkout_t.strftime('%H:%M')})"
        else:
            return "[OK] Ngày công chuẩn"
    except Exception as e:
        return "[Error] Lỗi định dạng giờ"

def process_attendance(attendance_file, leave_file, output_file):
    print(f"🔄 Đang nạp dữ liệu từ: {attendance_file} và {leave_file}...")
    try:
        # Bước 1: Đọc dữ liệu
        df_att = pd.read_csv(attendance_file)
        df_leave = pd.read_csv(leave_file)
        
        # Bước 2: Ghép nối (Merge) dữ liệu bằng EmpID và Date
        df_merged = pd.merge(
            df_att, 
            df_leave, 
            how='left', 
            left_on=['EmpID', 'Date'], 
            right_on=['EmpID', 'LeaveDate']
        )
        
        # Bước 3: Áp dụng logic 5 nhánh
        df_merged['Final_Status'] = df_merged.apply(determine_attendance_status, axis=1)
        
        # Bước 4: Làm sạch và Chọn cột xuất ra báo cáo
        final_report = df_merged[['EmpID', 'EmpName', 'Date', 'CheckIn_Time', 'CheckOut_Time', 'LeaveType', 'ApprovalStatus', 'Final_Status']]
        
        # Bước 5: Xuất file
        final_report.to_excel(output_file, index=False)
        print(f"✅ Thành công! Báo cáo đã được lưu tại: {output_file}")
        
    except Exception as e:
        print(f"❌ Đã xảy ra lỗi: {str(e)}")

if __name__ == "__main__":
    # Sử dụng Relative Path (Hoạt động trên cả Win/Mac miễn là cùng thư mục)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    att_csv = os.path.join(base_dir, 'raw_attendance.csv')
    leave_csv = os.path.join(base_dir, 'leave_requests.csv')
    out_xlsx = os.path.join(base_dir, 'Final_Attendance_Report.xlsx')
    
    process_attendance(att_csv, leave_csv, out_xlsx)
