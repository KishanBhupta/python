import tkinter as tk 
from tkinter import messagebox
import random 
import json

studentList = []   
def insert():
	try:
		name = nameEntry.get()
		email = emailEntry.get()
		phone = phoneEntry.get()
		password = passwordEntry.get()
		stud = {"name" :f"{name}","email":f"{email}","phone":f"{phone}","password" :f"{password}"}
		studentList.append(stud)
		file1 = open("kb.json","w")
		file1.truncate()
		data = json.dump(studentList,file1)
		# file1.seek(file1.tell() - 1)
		file1.close()
		messagebox.showinfo("Success"," insert Done !!")
	except Exception as e:
		messagebox.showerror("Error",e)
def showData():
    try:
        searchElemetn = searchEntry.get()
        file1 = open("file1.json","r")
        data = json.load(file1)
        for newData in data :
            if(newData['name']==searchElemetn):
                resNameLabel['text'] = f" Name :{newData['name']}"
                resEmailLabel['text'] = f" Email :{newData['email']}"
                resPhoneLable['text'] = f" Phone :{newData['phone']}"
                resPassLabel['text'] = f" Password :{newData['password']}"
    except Exception as e:
        messagebox.showerror("Success",e)
				

root = tk.Tk()
root.geometry("500x500")
root.title("Student Info ")

titlelabel = tk.Label(root,text=" Student Information ",width=25)
titlelabel.place(x=80,y=50)

nameLable = tk.Label(root , text="Name :")
nameLable.place(x=20,y=80)

nameEntry = tk.Entry(root , width=25)
nameEntry.place(x=80 , y=80)


emailLable = tk.Label(root , text="Email :")
emailLable.place(x=20,y=120)

emailEntry = tk.Entry(root , width=25)
emailEntry.place(x=80 , y=120)

phoneLable = tk.Label(root , text="Phone :")
phoneLable.place(x=20,y=160)

phoneEntry = tk.Entry(root , width=25)
phoneEntry.place(x=80 , y=160)

passwordLable = tk.Label(root , text="Password :")
passwordLable.place(x=20,y=200)

passwordEntry = tk.Entry(root , width=25)
passwordEntry.place(x=80 , y=200)

btnSubmit = tk.Button(root,text="Submit",width=30,command=lambda:insert())
btnSubmit.place(x=80,y=240)

searchLable = tk.Label(root , text="Password :")
searchLable.place(x=20,y=280)

searchEntry = tk.Entry(root , width=25)
searchEntry.place(x=80 , y=280)

btnShow = tk.Button(root,text="Show Data",width=30,command=lambda:showData())
btnShow.place(x=80,y=320)

resNameLabel = tk.Label(root)
resEmailLabel = tk.Label(root)
resPhoneLable = tk.Label(root)
resPassLabel = tk.Label(root)
resNameLabel.place(x=30,y=340)
resEmailLabel.place(x=30,y=360)
resPhoneLable.place(x=30,y=380)
resPassLabel.place(x=30,y=400)

root.mainloop()