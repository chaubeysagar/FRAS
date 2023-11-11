from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk
import cv2
import os
from PIL import Image as pil
from pkg_resources import parse_version
if parse_version(pil.__version__)>=parse_version('10.0.0'):
    Image.ANTIALIAS=Image.LANCZOS


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+0+0")
        self.root.title("Face Recognition Attendance System")

        # ============table variables=====================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_divi = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_cont = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()

        # Heading
        title_lbl = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("algerian", 35, "underline"), bg="orange",
                          fg="black")
        title_lbl.place(x=0, y=0, width=1200, height=54)

        # background image
        img3 = Image.open(r"Assets\bg student management.jpg")
        img3 = img3.resize((1200, 700), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=54, width=1200, height=700)

        # main frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=5, y=15, width=1183, height=620)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Information",
                                font=("cooper black", 12))
        left_frame.place(x=10, y=10, width=570, height=600)


        # current course
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                                          font=("cooper black", 12))
        current_course_frame.place(x=2, y=60, width=560, height=100)

        # department
        dep_label = Label(current_course_frame, text="Department", font=("algerian", 10, "bold"))
        dep_label.grid(row=0, column=0, padx=2, pady=5)
        # department combobox
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep,
                                 font=("time new roman", 8, "underline"), state="readonly")
        dep_combo["value"] = ("Select Department", "CSE", "IT", "CV", "ME", "EN")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=5)

        # Course
        cour_label = Label(current_course_frame, text="Course", font=("algerian", 10, "bold"))
        cour_label.grid(row=0, column=2, padx=10, pady=5)
        # Cource combobox
        cour_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,
                                  font=("time new roman", 8, "underline"), state="readonly")
        cour_combo["value"] = ("Select Course", "B.tech", "Polytechnic", "BBA", "MBA", "BCA")
        cour_combo.current(0)
        cour_combo.grid(row=0, column=3, padx=2, pady=5)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("algerian", 10, "bold"))
        year_label.grid(row=1, column=0, padx=2, pady=5)
        # Year combobox
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,
                                  font=("time new roman", 8, "underline"), state="readonly")
        year_combo["value"] = ("Select Year", "2019-20", "2020-21", "2021-22", "2022-23")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=0, pady=5)

        # Semester
        sem_label = Label(current_course_frame, text="Semester", font=("algerian", 10, "bold"))
        sem_label.grid(row=1, column=2, padx=10, pady=5)
        # Semester combobox
        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem,
                                 font=("time new roman", 8, "underline"), state="readonly")
        sem_combo["value"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=0, pady=0)

        # Class student information
        student_info_frame = LabelFrame(left_frame, bd=2, bg="yellow", relief=RIDGE, text="Class Student Information",
                                        font=("cooper black", 12))
        student_info_frame.place(x=2, y=150, width=560, height=400)

        # Student ID
        studentid_label = Label(student_info_frame, text="Studend ID :", font=("ariel", 10, "bold"), bg="white")
        studentid_label.grid(row=1, column=2, padx=5, sticky=W)
        # Student ID input
        studentid_entry = ttk.Entry(student_info_frame, textvariable=self.var_id, width=20, font=("ariel", 10, "bold"))
        studentid_entry.grid(row=1, column=3, padx=5, sticky=W)

        # student name

        stname_label = Label(student_info_frame, text="Student Name:", font=("ariel", 10, "bold"), bg="white")
        stname_label.grid(row=1, column=4, padx=5, sticky=W)

        stname_entry = ttk.Entry(student_info_frame, textvariable=self.var_name, width=16, font=("ariel", 10, "bold"))
        stname_entry.grid(row=1, column=5, padx=5, sticky=W)

        # class diviision
        classdivi_label = Label(student_info_frame, text="Class Division:", font=("ariel", 10, "bold"), bg="white")
        classdivi_label.grid(row=3, column=2, padx=1, pady=5, sticky=W)

        divi_combo = ttk.Combobox(student_info_frame, textvariable=self.var_divi,
                                  font=("time new roman", 8, "underline"),
                                  state="readonly")
        divi_combo["value"] = ("Select Division", "A", "B", "C", "D", "E")
        divi_combo.current(0)
        divi_combo.grid(row=3, column=3, padx=0, pady=0)


        # roll number
        roll_label = Label(student_info_frame, text="Roll Number:", font=("ariel", 10, "bold"), bg="white")
        roll_label.grid(row=3, column=4, padx=10, pady=5, sticky=W)

        roll_entry = ttk.Entry(student_info_frame, textvariable=self.var_roll, width=16, font=("ariel", 10, "bold"))
        roll_entry.grid(row=3, column=5, padx=5, sticky=W)

        # Gender
        gender_label = Label(student_info_frame, text="Gender:", font=("ariel", 10, "bold"), bg="white")
        gender_label.grid(row=5, column=2, padx=5, pady=5, sticky=W)

        gender_combo = ttk.Combobox(student_info_frame, textvariable=self.var_gender, font=("ariel", 8, "underline"),
                                    state="readonly")
        gender_combo["value"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=5, column=3, padx=0, pady=0)

        # dob
        dob_label = Label(student_info_frame, text="DOB:", font=("ariel", 10, "bold"), bg="white")
        dob_label.grid(row=5, column=4, padx=20, pady=5, sticky=W)

        dob_entry = ttk.Entry(student_info_frame, textvariable=self.var_dob, width=16, font=("ariel", 10, "bold"))
        dob_entry.grid(row=5, column=5, padx=5, pady=5, sticky=W)

        # Email id
        email_id_label = Label(student_info_frame, text="Email ID:", font=("ariel", 10, "bold"), bg="white")
        email_id_label.grid(row=7, column=2, pady=5, sticky=W)

        email_id_entry = ttk.Entry(student_info_frame, textvariable=self.var_email, width=20,
                                   font=("ariel", 10, "bold"))
        email_id_entry.grid(row=7, column=3, padx=10, pady=5, sticky=W)

        # Contact number
        contact_label = Label(student_info_frame, text="Contact Number:", font=("ariel", 10, "bold"), bg="white")
        contact_label.grid(row=7, column=4, pady=5, sticky=W)

        contact_entry = ttk.Entry(student_info_frame, textvariable=self.var_cont, width=16, font=("ariel", 10, "bold"))
        contact_entry.grid(row=7, column=5, padx=5, pady=5, sticky=W)

        # address
        address_label = Label(student_info_frame, text="Address:", font=("ariel", 10, "bold"), bg="white")
        address_label.grid(row=9, column=2, pady=5, sticky=W)

        address_entry = ttk.Entry(student_info_frame, textvariable=self.var_address, width=20,
                                  font=("ariel", 10, "bold"))
        address_entry.grid(row=9, column=3, padx=10, pady=5, sticky=W)

        # teacher name
        teacher_label = Label(student_info_frame, text="Teacher Name:", font=("ariel", 10, "bold"), bg="white")
        teacher_label.grid(row=9, column=4, pady=5, sticky=W)

        teacher_entry = ttk.Entry(student_info_frame, textvariable=self.var_teacher, width=16,
                                  font=("ariel", 10, "bold"))
        teacher_entry.grid(row=9, column=5, padx=5, pady=5, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        radiobutton1 = ttk.Radiobutton(student_info_frame, variable=self.var_radio1, text="Take Photo Sample",
                                       cursor="hand2", value="yes")
        radiobutton1.grid(row=11, column=2)

        radiobutton1 = ttk.Radiobutton(student_info_frame, variable=self.var_radio1, text="No Photo Sample",
                                       cursor="hand2", value="no")
        radiobutton1.grid(row=11, column=3)

        # button frame
        # Save Button
        save_btn = Button(student_info_frame, text="Save", command=self.add_data, cursor="hand2", width=20,
                          font=("ariel", 8, "underline"), bg="black", fg="white")
        save_btn.grid(row=13, column=2, pady=5, sticky=W)

        # Update Button
        update_btn = Button(student_info_frame, text="Update", command=self.update_data, cursor="hand2", width=20,
                            font=("ariel", 8, "underline"), bg="black", fg="white")
        update_btn.grid(row=13, column=3, pady=5, sticky=W)

        # Delete button
        del_btn = Button(student_info_frame, text="Delete", command=self.delete_data, cursor="hand2", width=20,
                         font=("ariel", 8, "underline"), bg="black", fg="white")
        del_btn.grid(row=13, column=4, sticky=W)

        # Reset button
        reset_btn = Button(student_info_frame, text="Reset", command=self.reset_data, cursor="hand2", width=20,
                           font=("ariel", 8, "underline"), bg="black", fg="white")
        reset_btn.grid(row=13, column=5, sticky=W)

        # take photo sample
        take_photo_btn = Button(student_info_frame, command=self.generate_dataset,text="Take Photo sample",
                                cursor="hand2", width=20, font=("ariel", 8, "underline"), bg="black", fg="white")
        take_photo_btn.grid(row=16, column=3, sticky=W)

        # update photo sample
        update_photo_btn = Button(student_info_frame, text="Update Photo sample", cursor="hand2", width=20,
                                  font=("ariel", 8, "underline"), bg="black", fg="white")
        update_photo_btn.grid(row=16, column=4)

        # right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Database", font=("cooper black", 12))
        right_frame.place(x=590, y=10, width=580, height=600)

        # Search frame system
        search_frame = LabelFrame(right_frame, bd=3, bg="yellow", relief=RIDGE, text="Database Search Engine",
                                  font=("ariel", 8))
        search_frame.place(x=15, y=1, width=550, height=60)

        # search by
        search_label = Label(search_frame, text="Search by:", bg="yellow", font=("times new roman", 13)).grid(row=0,
                                                                                                              column=0)

        search_combo = ttk.Combobox(search_frame, font=("ariel", 8, "underline"), state="readonly", width=12)
        search_combo["values"] = ("Select", "Student Name", "Roll Number", "Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=("ariel", 10))
        search_entry.grid(row=0, column=2, padx=5, sticky=W)

        search_btn = Button(search_frame, text="Search", cursor="hand2", width=15, font=("ariel", 8, "underline"),
                            bg="black", fg="white")
        search_btn.grid(row=0, column=4, sticky=W)

        showAll_btn = Button(search_frame, text="show All", width=15, font=("ariel", 8, "underline"), bg="black",
                             fg="white")
        showAll_btn.grid(row=0, column=5, sticky=W)

        # table frame

        table_frame = LabelFrame(right_frame, bd=3, bg="white", relief=RIDGE, text="Student Database Table",
                                 font=("ariel", 8))
        table_frame.place(x=0, y=61, width=570, height=510)

        scrol_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scrol_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            "dep", "course", "year", "sem", "id", "name", "divi", "roll", "gender", "dob", "email", "cont", "address",
            "teacher", "photo"), xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_x.config(command=self.student_table.xview)
        scrol_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student_ID")
        self.student_table.heading("name", text="Student_Name")
        self.student_table.heading("divi", text="Division")
        self.student_table.heading("roll", text="Roll_Number")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("cont", text="Contact")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher_Name")
        self.student_table.heading("photo", text="Photo_Sample_Status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("divi", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=70)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("cont", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        # self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ============================button functions==============================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("ERROR", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user='root', passwd='toor', database='face_recognizer',
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_divi.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_cont.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

            # =================fetch data=================================

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user='root', passwd='toor', database='face_recognizer',
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM face_recognizer.student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ======================get cursor=========================
    def get_cursor(self, event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_divi.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_cont.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),

    # =====================UPDATE FUNCTION=====================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Invalid Input", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("UPDATE", "Do you want to update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", user='root', passwd='toor',
                                                   database='face_recognizer', auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, divi=%s, roll=%s, gender=%s, "
                        " dob=%s,email=%s, cont=%s, address=%s, teacher=%s, photo=%s where id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_name.get(),
                            self.var_divi.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_cont.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_id.get()
                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student details are updated......")
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # ======================delet function=====================
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Detail row and page",
                                             "do you want to delete this student details")
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user='root', passwd='toor',
                                                   database='face_recognizer', auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()
                    sql = ("DELETE FROM STUDENT WHERE id=%s")
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfull deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f" due to :{str(es)}", parent=self.root)

    # ===================reset data set================
    def reset_data(self):
        self.var_dep.set("Select department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_divi.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_cont.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ==========================Generate dataset or take photo sample==========================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
             messagebox.showerror("ATTENTION", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user='root', passwd='toor',
                                                   database='face_recognizer', auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute(
                    "update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, divi=%s, roll=%s, gender=%s, "
                    " dob=%s,email=%s, cont=%s, address=%s, teacher=%s, photo=%s where id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_divi.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_cont.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ===================load predefined data on face frontals from opencv========
                face_classifier = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/id." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("cropped face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 30:
                        break      
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Photo sample Completed!!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()