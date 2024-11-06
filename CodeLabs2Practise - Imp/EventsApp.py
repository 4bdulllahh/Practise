#import tkinter module and messagebox
from tkinter import *
import tkinter.messagebox
# Set the output window
root = Tk()
root.title('Display Name')
root.geometry('400x200')
root.config(bg='#234567')
#Create a label
l1 = Label(root, text = "Enter Name",
bg='#234567',fg="white",font=("tahoma",12))
l1.place(x=10, y=20)

#Create entry widget
e1 = Entry(root,font=("tahoma",12))
e1.place(x=120, y=20)

#Create a button
b1 = Button(root, text = "Show Name", fg="yellow", bg="#001111",font=("tahoma",12))
b1.place(x=140,y=60)

#Create a label to display name
l2 = Label(root, text = "",bg='#234567',fg="white",font=("tahoma",12))
l2.place(x=10, y=100)
root.mainloop()
