import pandas as pd
import os

base_dir = r"c:\commandcenter\08_Ylake\02_Production\Course\C01_Masterclass_HR_AI\Ngay_03_Folder_hoc_vien\UC07_Attendance_Management"
raw_path = os.path.join(base_dir, "raw_attendance.csv")
leave_path = os.path.join(base_dir, "leave_requests.csv")
output_dir = os.path.join(base_dir, "Ket_qua_PA1")
output_path = os.path.join(output_dir, "PA1_Reconciliation_Result.csv")

os.makedirs(output_dir, exist_ok=True)

raw_df = pd.read_csv(raw_path)
leave_df = pd.read_csv(leave_path)

def process_row(row):
    empid = row['EmpID']
    date = row['Date']
    cin = pd.isna(row['CheckIn_Time'])
    cout = pd.isna(row['CheckOut_Time'])
    cin_val = str(row['CheckIn_Time']) if not cin else ""
    
    leave_info = leave_df[(leave_df['EmpID'] == empid) & (leave_df['LeaveDate'] == date)]
    leave_type = leave_info['LeaveType'].iloc[0] if not leave_info.empty else ""
    approval = leave_info['ApprovalStatus'].iloc[0] if not leave_info.empty else ""
    
    status = ""
    # Trống cả 2
    if cin and cout:
        if approval == "Approved":
            status = f"[Paid Leave] Nghỉ có phép ({leave_type})"
        else:
            status = "[Unpaid Leave] Nghỉ không phép (Không ghi nhận thẻ)"
    # Trống 1 trong 2
    elif cin or cout:
        status = "[Missing Punch] Thiếu dữ liệu thẻ (Cần giải trình)"
    # Có cả 2
    else:
        if cin_val <= "08:30":
            status = "[OK] Ngày công chuẩn"
        else:
            status = f"[Late] Đi trễ (Vào lúc {cin_val})"
            
    return pd.Series([leave_type, approval, status])

raw_df[['LeaveType', 'ApprovalStatus', 'Final_Status']] = raw_df.apply(process_row, axis=1)

output_df = raw_df[['EmpID', 'EmpName', 'Date', 'CheckIn_Time', 'CheckOut_Time', 'LeaveType', 'ApprovalStatus', 'Final_Status']]
output_df.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"✅ Success! Da xu ly xong {len(output_df)} dong du lieu.")
print(f"📂 Output duoc luu tai: {output_path}")
