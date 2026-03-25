import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import os
from datetime import datetime

class AttendanceMatcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Công Cụ Đối Soát Chấm Công & Phép - V1.0")
        self.root.geometry("650x380")
        self.root.configure(bg="#f8f9fa")
        
        # Biến lưu trữ đường dẫn file
        self.raw_attendance_path = tk.StringVar()
        self.leave_requests_path = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10))
        
        # Tiêu đề
        lbl_title = tk.Label(self.root, text="HỆ THỐNG ĐỐI SOÁT TỰ ĐỘNG", font=("Arial", 16, "bold"), bg="#f8f9fa", fg="#2c3e50")
        lbl_title.pack(pady=15)

        # Frame 1: Chọn file chấm công
        frame1 = tk.Frame(self.root, bg="#f8f9fa")
        frame1.pack(fill="x", padx=20, pady=5)
        tk.Label(frame1, text="1. File quẹt thẻ (CSV/Excel):", width=22, anchor="w", bg="#f8f9fa", font=("Arial", 10)).pack(side="left")
        tk.Entry(frame1, textvariable=self.raw_attendance_path, width=45, state="readonly").pack(side="left", padx=10)
        ttk.Button(frame1, text="Browse...", command=self.browse_attendance).pack(side="left")

        # Frame 2: Chọn file đơn phép
        frame2 = tk.Frame(self.root, bg="#f8f9fa")
        frame2.pack(fill="x", padx=20, pady=5)
        tk.Label(frame2, text="2. File đơn phép (CSV/Excel):", width=22, anchor="w", bg="#f8f9fa", font=("Arial", 10)).pack(side="left")
        tk.Entry(frame2, textvariable=self.leave_requests_path, width=45, state="readonly").pack(side="left", padx=10)
        ttk.Button(frame2, text="Browse...", command=self.browse_leave).pack(side="left")

        # Frame 3: Nút Chạy
        frame3 = tk.Frame(self.root, bg="#f8f9fa")
        frame3.pack(fill="x", pady=15)
        self.btn_run = tk.Button(frame3, text="🚀 XỬ LÝ & XUẤT BÁO CÁO", font=("Arial", 12, "bold"), 
                                 bg="#28a745", fg="white", height=2, command=self.run_process, cursor="hand2", relief="flat")
        self.btn_run.pack()
        
        # Log Box
        self.log_box = tk.Text(self.root, height=7, width=75, state="disabled", bg="#e9ecef", font=("Courier", 9))
        self.log_box.pack(pady=5, padx=20)
        
        self.log_message("Sẵn sàng. Hệ thống Rule Engine đã nạp.")
        self.log_message("Vui lòng duyệt 2 tệp dữ liệu gốc để bắt đầu...")

    def browse_attendance(self):
        filename = filedialog.askopenfilename(title="Chọn tệp chấm công thô", filetypes=[("CSV/Excel", "*.csv *.xlsx")])
        if filename:
            self.raw_attendance_path.set(filename)

    def browse_leave(self):
        filename = filedialog.askopenfilename(title="Chọn tệp đơn phép", filetypes=[("CSV/Excel", "*.csv *.xlsx")])
        if filename:
            self.leave_requests_path.set(filename)
            
    def log_message(self, message):
        self.log_box.config(state="normal")
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)
        self.log_box.config(state="disabled")

    def determine_status(self, row):
        check_in = str(row.get('CheckIn_Time', 'nan')).strip()
        check_out = str(row.get('CheckOut_Time', 'nan')).strip()
        leave_appr = str(row.get('ApprovalStatus', 'nan')).strip()
        leave_type = str(row.get('LeaveType', 'nan')).strip()
        
        has_in = check_in != 'nan' and check_in != ''
        has_out = check_out != 'nan' and check_out != ''
        
        # Trống hoàn toàn (vắng)
        if not has_in and not has_out:
            if leave_appr == 'Approved':
                return f"[Paid Leave] Nghỉ có phép ({leave_type})"
            else:
                return "[Unpaid Leave] Nghỉ không phép (Không ghi nhận thẻ)"
                
        # Thiếu 1 trong 2
        if (has_in and not has_out) or (not has_in and has_out):
            return "[Missing Punch] Thiếu dữ liệu thẻ (Cần giải trình)"
            
        # Có đủ In và Out
        if has_in and has_out:
            # Check In Time <= 08:30
            try:
                t_in = datetime.strptime(check_in, "%H:%M").time()
                t_limit = datetime.strptime("08:30", "%H:%M").time()
                if t_in <= t_limit:
                    return "[OK] Ngày công chuẩn"
                else:
                    return f"[Late] Đi trễ (Check-in lúc {check_in})"
            except:
                 return "[Late] Đi trễ (Lỗi format giờ)"
                 
        return "Unknown"

    def read_file(self, path):
        if path.endswith('.csv'):
            return pd.read_csv(path, dtype=str).fillna('')
        elif path.endswith('.xlsx'):
            return pd.read_excel(path, dtype=str).fillna('')
        return None

    def run_process(self):
        p1 = self.raw_attendance_path.get()
        p2 = self.leave_requests_path.get()
        
        if not p1 or not p2:
            messagebox.showerror("Lỗi đầu vào", "Vui lòng chọn đầy đủ 2 file cấu trúc!")
            return
            
        self.log_message("\n--- ĐANG XỬ LÝ ---")
        try:
            # Đọc Data
            df_att = self.read_file(p1)
            df_lv = self.read_file(p2)
            
            if df_att is None or df_lv is None:
                raise ValueError("Định dạng tệp không được hỗ trợ (cần .csv hoặc .xlsx)")
                
            self.log_message(f"► Nạp {len(df_att)} lượt chấm công.")
            self.log_message(f"► Nạp {len(df_lv)} đơn phép.")
            
            # Khớp tên cột Date bên bảng Phép nếu cần
            if 'LeaveDate' in df_lv.columns:
                df_lv = df_lv.rename(columns={'LeaveDate': 'Date'})
                
            # LEFT JOIN
            self.log_message("► Đang gộp dữ liệu (LEFT JOIN)...")
            merged_df = pd.merge(df_att, df_lv[['EmpID', 'Date', 'LeaveType', 'ApprovalStatus']], 
                                 on=['EmpID', 'Date'], how='left')
            merged_df = merged_df.fillna('')
            
            # Rule Engine
            self.log_message("► Đang chạy Rule AI phân loại...")
            merged_df['Final_Status'] = merged_df.apply(self.determine_status, axis=1)
            
            # Trim cột thừa (nếu có)
            final_columns = ['EmpID', 'EmpName', 'Date', 'CheckIn_Time', 'CheckOut_Time', 'LeaveType', 'ApprovalStatus', 'Final_Status']
            final_df = merged_df[final_columns]
            
            # Lưu file
            output_dir = os.path.dirname(p1)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_path = os.path.join(output_dir, f"Final_Report_{timestamp}.csv")
            final_df.to_csv(output_path, index=False, encoding='utf-8-sig')
            
            self.log_message(f"✅ HOÀN TẤT! File lưu tại:\n  {output_path}")
            messagebox.showinfo("Thành công", f"Kiểm tra thư mục chứa file gốc để lấy:\nFinal_Report_{timestamp}.csv")
            
        except KeyError as e:
             self.log_message(f"❌ LỖI DỮ LIỆU: Bảng gốc thiếu cột {str(e)}")
             messagebox.showerror("Sai cấu trúc", f"File thiếu cột bắt buộc: {str(e)}\nHãy kiểm tra lại file đưa vào.")
        except Exception as e:
            self.log_message(f"❌ LỖI: {str(e)}")
            messagebox.showerror("Lỗi hệ thống", f"Phát sinh lỗi:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceMatcherApp(root)
    root.mainloop()
