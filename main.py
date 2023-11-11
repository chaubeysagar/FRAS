from tkinter import*
from tkinter import ttk
from tkinter import messagebox 
from PIL import Image ,ImageTk
from time import strftime
from datetime import datetime
from student import Student
from attendance import Attendance
from our_team import Our_Team
import os
import cv2
import numpy as np
import mysql.connector
from PIL import Image as pil
from pkg_resources import parse_version
if parse_version(pil.__version__)>=parse_version('10.0.0'):
    Image.ANTIALIAS=Image.LANCZOS

class Face_Recognition_System:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1200x700+0+0")
		self.root.title("Face Recognition Attendance System")

		#Heading
		title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("algerian",35,"underline"),bg="#e1dfdf",fg="black")
		title_lbl.place(x=0,y=0,width=1200,height=54)

		#background image
		img3=Image.open(r"Assets\bg FRAS.jpg")
		img3=img3.resize((1200,700),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		bg_img=Label(self.root,image=self.photoimg3)
		bg_img.place(x=0,y=54,width=1200,height=700)

		#time
		def time():
			string=strftime("%H:%M:%S %p")
			time_lbl.config(text=string)
			time_lbl.after(1000,time)

		time_lbl=Label(bg_img,font=("copperplate gothic bold",18),bg="white",fg="black")
		time_lbl.place(x=1020,y=5,width=170,height=30)
		time()


		#button	student info
		img4=Image.open(r"Assets\button student info.png")
		img4=img4.resize((180,180),Image.ANTIALIAS)
		self.photoimg4=ImageTk.PhotoImage(img4)

		b1=Button(bg_img,image=self.photoimg4,command=self.student_detail,cursor="hand2")
		b1.place(x=220,y=75,width=182,height=182)

		#button face verification/mark attendance
		img5=Image.open(r"Assets\button face verification.png")
		img5=img5.resize((180,180),Image.ANTIALIAS)
		self.photoimg5=ImageTk.PhotoImage(img5)

		b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_reco)
		b1.place(x=510,y=75,width=182,height=182)

		#button attendance
		img6=Image.open(r"Assets\button attendance.png")
		img6=img6.resize((180,180),Image.ANTIALIAS)
		self.photoimg6=ImageTk.PhotoImage(img6)

		b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
		b1.place(x=800,y=75,width=182,height=182)


		#button process images
		img7=Image.open(r"Assets\button process images.png")
		img7=img7.resize((180,180),Image.ANTIALIAS)
		self.photoimg7=ImageTk.PhotoImage(img7)

		b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_classifier)
		b1.place(x=220,y=325,width=182,height=182)


		#button images
		img8=Image.open(r"Assets\button images.png")
		img8=img8.resize((180,180),Image.ANTIALIAS)
		self.photoimg8=ImageTk.PhotoImage(img8)

		b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_images)
		b1.place(x=510,y=325,width=182,height=182)


		#button our team
		img9=Image.open(r"Assets\button our team.png")
		img9=img9.resize((180,180),Image.ANTIALIAS)
		self.photoimg9=ImageTk.PhotoImage(img9)

		b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.our_team_page)
		b1.place(x=800,y=325,width=182,height=182)

		#log out button
		logout_btn = Button(bg_img, text="Log Out", cursor="hand2", width=15,height=1,border=7,
                            font=("ariel", 12, "bold"), bg="#e1dfdf", fg="red")
		logout_btn.place(x=530,y=580)
        #update_btn.grid(row=13, column=3, pady=5, sticky=W)


	#========================button functions======================
	
	def open_images(self):
		os.startfile(r"Data")

	def student_detail(self):
		self.new_window=Toplevel(self.root)
		self.app=Student(self.new_window)



################################################################################
#	def process_data(self):
#		self.new_window=Toplevel(self.root)
#		self.app=Process(self.new_window)
	#===========================train images=====================
	def train_classifier(self):
		data_dir = r"Data"
		path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
		faces = []
		ids = []

		for image in path:
			img = Image.open(image).convert('L')      # Convert to grayscale
			imageNp = np.array(img, "uint8")
			id = int(os.path.split(image)[1].split('.')[1])
			faces.append(imageNp)
			ids.append(id)
			cv2.imshow("Processing", imageNp)
			cv2.waitKey(1) == 13
		ids = np.array(ids)

        # Train the classifier and save
		clf = cv2.face.LBPHFaceRecognizer_create()
		clf.train(faces, ids)
		clf.write(r"classifier.xml")
		cv2.destroyAllWindows()
		messagebox.showinfo("Result", "Training Datasets Completed!")

#################################################################################
	#def face_data(self):
	#	self.new_window=Toplevel(self.root)
	#	self.app=Face_Recognition(self.new_window)

# =============================attendance========================
	def mark_attendance(self, i, r, n, d):
		with open("attendance.csv", "r+", newline="\n") as f:
			myDataList = f.readlines()
			name_list = []
			for line in myDataList:
				entry = line.split((","))
				name_list.append(entry[0])
			if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
				now = datetime.now()
				d1 = now.strftime("%d/%m/%y")
				dtString = now.strftime("%H:%M:%S")
				f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

#============================face recognition======================================

	def face_reco(self):
		def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
			gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

			coord = []

			for (x, y, w, h) in features:
				cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
				id, predict = clf.predict(gray_image[y:y + h, x:x + w])
				confidence = int((100 * (1 - predict / 300)))

				conn = mysql.connector.connect(host="localhost", user='root', passwd='toor',
											   database='face_recognizer', auth_plugin="mysql_native_password")
				my_cursor = conn.cursor()

				my_cursor.execute("select name from student where id=" + str(id))
				n = my_cursor.fetchone()
				n = "+".join(n)

				my_cursor.execute("select roll from student where id=" + str(id))
				r = my_cursor.fetchone()
				r = "+".join(r)

				my_cursor.execute("select dep from student where id=" + str(id))
				d = my_cursor.fetchone()
				d = "+".join(d)

				my_cursor.execute("select id from student where id=" + str(id))
				i = my_cursor.fetchone()
				i = "+".join(i)

				if confidence < 77:
					cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
					cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
					cv2.putText(img, f"Name:{n}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
					cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
					self.mark_attendance(i, r, n, d)
				else:
					cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
					cv2.putText(img, "Unknown Person", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

				coord = [x, y, w, h]

			return coord

		def recognize(img, clf, faceCascade):
			coord = draw_boundary(img,faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
			return img

		faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		clf = cv2.face.LBPHFaceRecognizer_create()
		clf.read(r"classifier.xml")

		video_cap = cv2.VideoCapture(0)

		while TRUE:
			ret, img = video_cap.read()
			img = recognize(img, clf, faceCascade)
			cv2.imshow("Welcome to Face Recognition", img)

			if cv2.waitKey(1) == 13:
				break
		video_cap.release()
		cv2.destroyAllWindows()
#########################################################################

	def attendance_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Attendance(self.new_window)


	def our_team_page(self):
		self.new_window=Toplevel(self.root)
		self.app=Our_Team(self.new_window)





if __name__=="__main__":
	root=Tk()
	obj=Face_Recognition_System(root)
	root.mainloop()