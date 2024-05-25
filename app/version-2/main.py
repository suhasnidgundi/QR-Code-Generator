from tkinter import*
from tkinter import messagebox, ttk
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage

class Qr_Generator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR CODE GENERATOR | DEVELOPED BY SUHAS NIDGUNDI")
        self.root.resizable(False, False)
        self.root.geometry("900x500+200+50")

        title = Label(self.root, text="QR CODE GENERATOR BY SUHAS NIDGUNDI", font=("calibri", 30), bg="#053246", fg="white", justify=CENTER).place(x=0, y=0, relwidth=1)

        #======================= All Variables =========================== #
        self.var_emp_code = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()

        # ========================= Empolyee Details Window ================================== #
        emp_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        emp_Frame.place(x=50, y=100, width=500, height=380)
        emp_title = Label(emp_Frame, text="Employee Details", font=("calibri", 20), bg="#053246", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1)

        lbl_emp_code = Label(emp_Frame, text="Employee ID", font=("comicsans", 15, "bold"), bg="white", anchor="w", padx=20).place(x=20, y=60)
        lbl_emp_name = Label(emp_Frame, text="Name", font=("comicsans", 15, "bold"), bg="white", anchor="w", padx=20).place(x=20, y=100)
        lbl_emp_department = Label(emp_Frame, text="Department", font=("comicsans", 15, "bold"), bg="white", anchor="w", padx=20).place(x=20, y=140)
        lbl_emp_designation = Label(emp_Frame, text="Designation", font=("comicsans", 15, "bold"), bg="white", anchor="w", padx=20).place(x=20, y=180)

        txt_emp_code = Entry(emp_Frame, textvariable=self.var_emp_code, font=("consolos", 15), bg="lightgrey").place(x=200, y=60)
        txt_emp_name = Entry(emp_Frame, textvariable=self.var_name, font=("consolos", 15), bg="lightgrey").place(x=200, y=100)
        txt_emp_department = Entry(emp_Frame, textvariable=self.var_department, font=("consolos", 15), bg="lightgrey").place(x=200, y=140)
        txt_emp_designation = Entry(emp_Frame, textvariable=self.var_designation, font=("consolos", 15), bg="lightgrey").place(x=200, y=180)

        btn_generate = Button(emp_Frame, command=self.generate, text="Generate QR", font=("calibri", 15), bg="#2196f3", fg="white", activebackground="#262626", activeforeground="white", bd=0, cursor="hand2").place(x=90, y=250, width=180, height=30)
        btn_clear = Button(emp_Frame, text="Clear", command=self.clear, font=("calibri", 15), bg="#607d8b", fg="white", activebackground="red", activeforeground="white", bd=0, cursor="hand2").place(x=280, y=250, width=120, height=30)

        self.msg = ""
        self.lbl_msg = Label(emp_Frame, text=self.msg, font=("calibri", 15, "bold"), bg="white", fg="green")
        self.lbl_msg.place(x=0, y=320, relwidth=1)

        # ======================= Employee QR CODE Window =========================== #
        qr_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        qr_frame.place(x=600, y=100, width=250, height=380)

        emp_title = Label(qr_frame, text="Employee QR", font=("calibri", 20), bg="#053246", fg="white").place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_frame, text="NO QR\nAVAILABLE", font=("times new roman", 15), bg="#3f51b5", fg="white", bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.lbl_msg.config(text="")

    def generate(self):
        if self.var_emp_code.get()=="" or self.var_name.get()=="" or self.var_department.get()=="" or self.var_designation.get()=="":
            self.msg = "All Fields are Required !!!"
            self.lbl_msg.config(text=self.msg, fg="red")
        else:
            qr_data = (f"Employee ID : {self.var_emp_code.get()}\nEmployee Name : {self.var_name.get()}\nDepartment : {self.var_department.get()}\nDesignation : {self.var_designation.get()}")
            qr_code = qrcode.make(qr_data)
            # print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])
            qr_code.save("Employee_QR/Emp_"+str(self.var_emp_code.get())+'.png')
            # ==================== QR Code Image Update =================#
            self.im = ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            # ==================== Update Notification =================#
            self.msg = "QR CODE GENERATED SUCCESSFULLY !!!"
            self.lbl_msg.config(text=self.msg, fg="green")

root = Tk()
obj = Qr_Generator(root)
root.mainloop()