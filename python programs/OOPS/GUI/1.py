import tkinter as tk 
from tkinter import *

studentList = []
def savedata():
    stuName = name.get()
    sturoll = rollNo.get()
    marks = totalmarks.get()
    studentdic = {"name":stuName,"rollno":sturoll,"marks":marks}
    studentList.append(studentdic)
    
def showResult():
    print(studentList)

# import messageBox 
root = tk.Tk()
root.geometry("500x300")
root.title("Student  !")

# name roll no and 3 subject of marks 

lname = tk.Label(root, text="Name : ", fg='Black', font="JOKER")
lname.place(x=10, y=30)

name = tk.Entry(root, font="JOKER")
name.place(x=95,y=30)

lrollno = tk.Label(root, text="Roll No : ", fg='Black', font="JOKER")
lrollno.place(x=10, y=60)

rollNo = tk.Entry(root, font="JOKER")
rollNo.place(x=95,y=60)

lmarks = tk.Label(root, text="Marks: ", fg='Black', font="JOKER")
lmarks.place(x=10, y=90)

totalmarks = tk.Entry(root, font="JOKER")
totalmarks.place(x=95,y=90)

saveStn = tk.Button(root, text="Save Student",command=lambda:savedata(),fg="white",background="green",  width=10)
saveStn.place(x=350, y=30)
showStn = tk.Button(root, text="show result",command=lambda :showResult(),background="blue",fg="white" , width=10)
showStn.place(x=350, y=60)
root.mainloop()



    