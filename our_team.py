from tkinter import*
from PIL import Image ,ImageTk
from PIL import Image as pil
from pkg_resources import parse_version
if parse_version(pil.__version__)>=parse_version('10.0.0'):
    Image.ANTIALIAS=Image.LANCZOS

class Our_Team:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1200x700+0+0")
		self.root.title("Face Recognition Attendance System")



		#Label
		title_lbl=Label(self.root,text="<<< Developer >>>",font=("algerian",35,"underline"),bg="#ff008a",fg="black")
		title_lbl.place(x=0,y=0,width=1200,height=50)

		bg_lbl=Label(self.root,bg="#ff1ead")
		bg_lbl.place(x=0,y=52,width=1200,height=700)



		#left top frame
		lt_frame=Frame(bg_lbl,bd=2)
		lt_frame.place(x=33,y=25,width=1134,height=250)

		#profile photo
		img4=Image.open(r"Assets\tm sagar.jpg")
		img4=img4.resize((180,240),Image.ANTIALIAS)
		self.photoimg4=ImageTk.PhotoImage(img4)

		lbl_img4=Label(lt_frame,image=self.photoimg4)
		lbl_img4.place(x=3,y=3,width=180,height=240)

		#name heading
		lbl_sagar=Label(lt_frame,text="Sagar Kumar Chaubey",font=("times new roman",24,"bold"),bg="pink",justify="left",anchor="w",padx=12)
		lbl_sagar.place(x=186,y=3,width=941,height=70)

		#sub heading
		lbl_sagar=Label(lt_frame,text="Software Engineer\nGithub- @chaubeysagar\nInstagram- @quasaragas",font=("times new roman",18,"bold"),bg="pink",justify="left",anchor="w",padx=12)
		lbl_sagar.place(x=186,y=75,width=941,height=170)




if __name__=="__main__":
	root=Tk()
	obj=Our_Team(root)
	root.mainloop()