from tkinter import*
from tkinter import ttk ,messagebox
from PIL import Image ,ImageTk
import os
import csv
from tkinter import filedialog
from PIL import Image as pil
from pkg_resources import parse_version
if parse_version(pil.__version__)>=parse_version('10.0.0'):
    Image.ANTIALIAS=Image.LANCZOS

lst_csvdata=[]

class Attendance:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1200x700+0+0")
		self.root.title("Face Recognition Attendance System")


		#==========================variables=========================
		self.var_atten_id=StringVar()
		self.var_atten_iroll=StringVar()
		self.var_atten_name=StringVar()
		self.var_atten_dep=StringVar()
		self.var_atten_time=StringVar()
		self.var_atten_date=StringVar()
		self.var_atten_attendance=StringVar()


		#Heading
		title_lbl=Label(self.root,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",font=("algerian",35,"underline"),bg="light green",fg="black")
		title_lbl.place(x=0,y=0,width=1200,height=54)

		#background image
		img3=Image.open(r"Assets\bg student attendance management.jpg")
		img3=img3.resize((1200,700),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		bg_img=Label(self.root,image=self.photoimg3)
		bg_img.place(x=0,y=54,width=1200,height=700)

		#main frame
		main_frame=Frame(bg_img,bd=2)
		main_frame.place(x=5,y=15,width=1185,height=620)

		#left label frame
		Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Information",font=("cooper black",12))
		Left_frame.place(x=15,y=10,width=580,height=600)

		img4=Image.open(r"Assets\bg student attendance management.jpg")
		img4=img4.resize((1200,700),Image.ANTIALIAS)
		self.photoimg4=ImageTk.PhotoImage(img4)

		lbl_img4=Label(Left_frame,image=self.photoimg4)
		lbl_img4.place(x=6,y=0,width=564,height=155)


		#left in frame
		left_in_frame=Frame(Left_frame,bd=2,relief="ridge")
		left_in_frame.place(x=5,y=160,width=565,height=300)

		#Label and entry
		#attendance id
		attendanceID_label=Label(left_in_frame,text="AttendanceId:",font=("ariel",11,"bold"),bg="white")
		attendanceID_label.grid(row=0,column=0,pady=5,sticky=W)

		attendanceID_entry=ttk.Entry(left_in_frame,width=20,font=("ariel",11,"bold"),textvariable=self.var_atten_id)
		attendanceID_entry.grid(row=0,column=1,pady=5,sticky=W)


		#roll id
		roll_label=Label(left_in_frame,text="Roll:",font=("ariel",11,"bold"),bg="white")
		roll_label.grid(row=0,column=2,pady=5,sticky=W)

		roll_entry=ttk.Entry(left_in_frame,width=20,font=("ariel",11,"bold"),textvariable=self.var_atten_iroll)
		roll_entry.grid(row=0,column=3,pady=5,sticky=W)


		#name id
		date_label=Label(left_in_frame,text="Name:",font=("ariel",11,"bold"),bg="white")
		date_label.grid(row=1,column=0,pady=5,sticky=W)

		date_entry=ttk.Entry(left_in_frame,width=20,font=("ariel",11,"bold"),textvariable=self.var_atten_name)
		date_entry.grid(row=1,column=1,pady=5,sticky=W)


		#department id
		dep_label=Label(left_in_frame,text="Department:",font=("ariel",11,"bold"),bg="white")
		dep_label.grid(row=1,column=2,pady=5,sticky=W)

		dep_entry=ttk.Entry(left_in_frame,width=20,font=("ariel",11,"bold"),textvariable=self.var_atten_dep)
		dep_entry.grid(row=1,column=3,pady=5,sticky=W)


		#time id
		attendanceID_label=Label(left_in_frame,text="Time:",font=("ariel",11,"bold"),bg="white")
		attendanceID_label.grid(row=2,column=0,pady=5,sticky=W)

		attendanceID_entry=ttk.Entry(left_in_frame,width=20,font=("ariel",11,"bold"),textvariable=self.var_atten_time)
		attendanceID_entry.grid(row=2,column=1,pady=5,sticky=W)


		#date id
		attendanceID_label=Label(left_in_frame,text="Date:",font=("ariel",11,"bold"),bg="white")
		attendanceID_label.grid(row=2,column=2,pady=5,sticky=W)

		attendanceID_entry=ttk.Entry(left_in_frame,width=20,font=("ariel",11,"bold"),textvariable=self.var_atten_date)
		attendanceID_entry.grid(row=2,column=3,pady=5,sticky=W)


		#attendance
		attendancelabel=Label(left_in_frame,text="Attendance",font=("ariel",11,"bold"),bg="white")
		attendancelabel.grid(row=3,column=0,sticky=W,pady=5)

		self.atten_status=ttk.Combobox(left_in_frame,text="Attendance",font=("ariel",11,"bold"),state="readonly",textvariable=self.var_atten_attendance)
		self.atten_status["values"]=("Status","Present","Absent")
		self.atten_status.grid(row=3,column=1,pady=5,sticky=W)
		self.atten_status.current(0)


		#buttonsframe
		btn_frame=Frame(left_in_frame,bd=2,relief=GROOVE,bg="red")
		btn_frame.place(x=0,y=250,width=564,height=41)

		import_btn=Button(btn_frame,text="Import csv",width=13,font=("ariel",13,"bold"),bg="pink",fg="black",command=self.importcsv)
		import_btn.grid(row=0,column=0,pady=2)

		export_btn=Button(btn_frame,text="Export csv",width=13,font=("ariel",13,"bold"),bg="pink",fg="black",command=self.exportcsv)
		export_btn.grid(row=0,column=1,pady=2)

		update_btn=Button(btn_frame,text="Update",width=13,font=("ariel",13,"bold"),bg="pink",fg="black")
		update_btn.grid(row=0,column=2,pady=2)

		reset_btn=Button(btn_frame,text="Reset",width=13,font=("ariel",13,"bold"),bg="pink",fg="black",command=self.reset_data)
		reset_btn.grid(row=0,column=3,pady=2)


		#right label frame
		Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Information",font=("cooper black",12))
		Right_frame.place(x=595,y=10,width=570,height=600)

		#right in frame
		right_in_frame=Frame(Right_frame,bd=2,relief=GROOVE,bg="white")
		right_in_frame.place(x=2,y=1,width=562,height=575)

		#scroll bar
		scroll_x=ttk.Scrollbar(right_in_frame,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(right_in_frame,orient=VERTICAL)

		self.AttendanceReportTable=ttk.Treeview(right_in_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		
		scroll_x.pack(side="bottom",fill="x")
		scroll_y.pack(side="right",fill="y")

		scroll_x.config(command=self.AttendanceReportTable.xview)
		scroll_y.config(command=self.AttendanceReportTable.yview)

		self.AttendanceReportTable.heading("id",text="Attendance Id")
		self.AttendanceReportTable.heading("roll",text="Roll")
		self.AttendanceReportTable.heading("name",text="Name")
		self.AttendanceReportTable.heading("department",text="Department")
		self.AttendanceReportTable.heading("time",text="Time")
		self.AttendanceReportTable.heading("date",text="Date")
		self.AttendanceReportTable.heading("attendance",text="Attendance")

		self.AttendanceReportTable["show"]="headings"

		self.AttendanceReportTable.column("id",width=120)
		self.AttendanceReportTable.column("roll",width=120)
		self.AttendanceReportTable.column("name",width=120)
		self.AttendanceReportTable.column("department",width=120)
		self.AttendanceReportTable.column("time",width=120)
		self.AttendanceReportTable.column("date",width=120)
		self.AttendanceReportTable.column("attendance",width=120)

		self.AttendanceReportTable.pack(fill=BOTH,expand=1)

		self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


	#=======================fetch data=====================================================
	def fetchdata(self,rows):
		self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
		for i in rows:
			self.AttendanceReportTable.insert("",END,values=i)

	#import csv
	def importcsv(self):
		global lst_csvdata
		lst_csvdata.clear()
		fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetype=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
		with open(fln) as csvfile:
			csvread=csv.reader(csvfile,delimiter=",")
			for i in csvread:
				lst_csvdata.append(i)
			self.fetchdata(lst_csvdata)


	#exort csv
	def exportcsv(self):
		try:
			if len(lst_csvdata)<1:
				messagebox.showerror("No Data","No data found to export",parent=self.root)
				return False
			fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save as",filetype=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
			with open(fln,mode="w",newline="") as savefile:
				exp_write=csv.writer(savefile,delimiter=",")
				for i in lst_csvdata:
					exp_write.writerow(i)
				messagebox.showinfo("Export","Data Exported to "+os.path.basename(fln)+" successfully")
		except Exception as es:
			messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


	#data on entry field by cursor click
	def get_cursor(self,event=""):
		cursor_row=self.AttendanceReportTable.focus()
		content=self.AttendanceReportTable.item(cursor_row)
		rows=content["values"]
		self.var_atten_id.set(rows[0])
		self.var_atten_iroll.set(rows[1])
		self.var_atten_name.set(rows[2])
		self.var_atten_dep.set(rows[3])
		self.var_atten_time.set(rows[4])
		self.var_atten_date.set(rows[5])
		self.var_atten_attendance.set(rows[6])


	#reset
	def reset_data(self):
		self.var_atten_id.set("")
		self.var_atten_iroll.set("")
		self.var_atten_name.set("")
		self.var_atten_dep.set("")
		self.var_atten_time.set("")
		self.var_atten_date.set("")
		self.var_atten_attendance.set("")







		

if __name__=="__main__":
	root=Tk()
	obj=Attendance(root)
	root.mainloop()