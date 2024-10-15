from tkinter import *
main = Tk()
main.title('Using Pack()')
Button(main,text="A").pack(side=LEFT, expand=YES, fill=Y)
Button(main,text="B",bd=15 ,bg="red", fg="white").pack(side=TOP, expand=YES, fill=BOTH)
Button(main,text="C").pack(side=RIGHT, expand=YES, fill=NONE, anchor=NE,pady=6)
Button(main,text="D").pack(side=BOTTOM, expand=NO, fill=Y,pady=6)
main.mainloop()

