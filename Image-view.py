from tkinter import *
root = Tk()

img_1 = PhotoImage(file="C:\\Users\\Thendral\\Desktop\\Python code\\Images\\sum.png")
img_2 = PhotoImage(file="C:\\Users\\Thendral\\Desktop\\Python code\\Images\\sum2.png")
img_3 = PhotoImage(file="C:\\Users\\Thendral\\Desktop\\Python code\\Images\\sum3.png")

img_list=[img_1,img_2,img_3]
lab = Label(image = img_list[0])
lab.grid(row=0,column=0,columnspan=3)
status = Label(root,text="Image 1 of "+str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)

def forward(image_number):
	global lab
	global prev
	global nex
	# disappear for previous image func
	lab.grid_forget()
	lab = Label(image = img_list[image_number])
	lab.grid(row=0,column=0,columnspan=3)
	nex = Button(root,text="  >>  ",command=lambda:forward(image_number+1))
	prev = Button(root,text="  <<  ",command=lambda:backward(image_number-1))
	if image_number == 2:
		nex = Button(root,text="  >>  ",state=DISABLED)
	prev.grid(row=1,column=0)
	exit.grid(row=1,column=1)
	nex.grid(row=1,column=2)

	status = Label(root,text="Image "+ str(image_number+1)+" of "+str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def backward(image_number):
	global lab
	global prev
	global nex
	lab.grid_forget()
	lab = lab = Label(image = img_list[image_number])
	lab.grid(row=0,column=0,columnspan=3)
	nex = Button(root,text="  >>  ",command=lambda:forward(image_number+1))
	prev = Button(root,text="  <<  ",command=lambda:backward(image_number-1))
	if image_number == 0:
		prev = Button(root,text="  <<  ",command=lambda:backward(image_number=image_number-1),state=DISABLED)
	prev.grid(row=1,column=0)
	exit.grid(row=1,column=1)
	nex.grid(row=1,column=2)

	status = Label(root,text="Image "+ str(image_number+1)+" of "+str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)

prev = Button(root,text="  <<  ",state=DISABLED)
exit = Button(root,text = " Exit Program ",command=root.quit,)
nex = Button(root,text="  >>  ",command=lambda:forward(1))

prev.grid(row=1,column=0)
exit.grid(row=1,column=1)
nex.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()
