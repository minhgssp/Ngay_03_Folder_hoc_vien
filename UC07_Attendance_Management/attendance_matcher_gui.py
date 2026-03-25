import pandas as pd
import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def determine_attendance_status(row):
    """ Xử lý logic 5 nhánh chấm công """
    has_checkin = pd.notna(row['CheckIn_Time'])
    has_checkout = pd.notna(row['CheckOut_Time'])
    has_approved_leave = pd.notna(row['ApprovalStatus']) and str(row['ApprovalStatus']).lower() == 'approved'
    
    if not has_checkin and not has_checkout:
        if has_approved_leave:
            return f"[Paid Leave] Nghỉ có phép ({row['LeaveType']})"
        else:
            return "[Unpaid Leave] Nghỉ không phép"
            
    if not has_checkin or not has_checkout:
        return "[Missing Punch] Thiếu dữ liệu thẻ (Quên quẹt)"
        
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
        return "[Error] Sai định dạng giờ"

def process_attendance(attendance_file, leave_file, output_file):
    df_att = pd.read_csv(attendance_file)
    df_leave = pd.read_csv(leave_file)
    df_merged = pd.merge(df_att, df_leave, how='left', left_on=['EmpID', 'Date'], right_on=['EmpID', 'LeaveDate'])
    df_merged['Final_Status'] = df_merged.apply(determine_attendance_status, axis=1)
    
    final_report = df_merged[['EmpID', 'EmpName', 'Date', 'CheckIn_Time', 'CheckOut_Time', 'LeaveType', 'ApprovalStatus', 'Final_Status']]
    final_report.to_excel(output_file, index=False)
    return True

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Công Cụ Đối Soát Chấm Công (Antigravity)")
        self.root.geometry("600x350")
        self.root.resizable(False, False)
        
        # Biến lưu đường dẫn
        self.att_file = tk.StringVar()
        self.leave_file = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="HỆ THỐNG ĐỐI SOÁT CHẤM CÔNG VÀ NGHỈ PHÉP", font=("Arial", 14, "bold")).pack(pady=20)
        
        # Frame for File 1
        f1 = ttk.Frame(self.root)
        f1.pack(fill='x', padx=20, pady=10)
        ttk.Label(f1, text="1. File Chấm Công (CSV):", width=25).pack(side='left')
        ttk.Entry(f1, textvariable=self.att_file, width=40, state='readonly').pack(side='left', padx=10)
        ttk.Button(f1, text="Chọn File", command=lambda: self.select_file(self.att_file)).pack(side='left')
        
        # Frame for File 2
        f2 = ttk.Frame(self.root)
        f2.pack(fill='x', padx=20, pady=10)
        ttk.Label(f2, text="2. File Nghỉ Phép (CSV):", width=25).pack(side='left')
        ttk.Entry(f2, textvariable=self.leave_file, width=40, state='readonly').pack(side='left', padx=10)
        ttk.Button(f2, text="Chọn File", command=lambda: self.select_file(self.leave_file)).pack(side='left')
        
        # Run Button
        ttk.Button(self.root, text="🚀 XỬ LÝ ĐỐI SOÁT & XUẤT EXCEL", command=self.run_process, style="Accent.TButton").pack(pady=30)
        
    def select_file(self, var):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filepath:
            var.set(filepath)
            
    def run_process(self):
        f_att = self.att_file.get()
        f_leave = self.leave_file.get()
        
        if not f_att or not f_leave:
            messagebox.showwarning("Thiếu File", "Vui lòng chọn đầy đủ 2 file dữ liệu đầu vào!")
            return
            
        try:
            out_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], initialfile="Final_Attendance_Report.xlsx")
            if out_file:
                process_attendance(f_att, f_leave, out_file)
                messagebox.showinfo("Thành Công", f"Đã xuất file đối soát thành công tại:\n{out_file}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra trong quá trình xử lý:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure("Accent.TButton", font=("Arial", 11, "bold"), foreground="blue")
    app = AttendanceApp(root)
    root.mainloop()
