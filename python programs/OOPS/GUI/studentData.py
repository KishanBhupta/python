from tkinter import * 
from tkinter import messagebox
import json 
import os 

root = Tk()
root.geometry("500x500")
root.title("Student information")

studentData = []
class Student():
	def __init__(self):
		try:
			file1 = open("studentData.json","w")
		except Exception as e:
			messagebox.showinfo(f"Error: {e}")

	def insertData(self):
		self.name = nameEntry.get()
		self.email = emailEntry.get()
		self.phone = phoneEntry.get()
		self.sub1 = sub1Entry.get()
		self.sub2 = sub2Entry.get()
		self.sub3 = sub3Entry.get()
		self.sub4 = sub4Entry.get()
		self.sub5 = sub5Entry.get()
		self.total = int(self.sub1)+int(self.sub2)+int(self.sub3)+int(self.sub4)+int(self.sub5)

		studData = { "rollno":f"{rollno}","name":f"{self.name}","email":f"{self.email}","phone":f"{self.phone}" ,"marks":f"{self.total}"}
		studentData.append(studData)
		file1 = open("studentData.json","w")
		file1.truncate()
		data = json.dump(studentData,file1)
		file1.close()
		messagebox.showinfo("Done","record insert !")

	def showData(self):
		self.searchElement = reschEntry.get()
		file1 =open("studentData.json")
		data = json.load(file1)

		for newData in data :
			if (newData["rollno"] == self.searchElement):
				self.per = float(newData["marks"]) / 5
				nameL["text"] = f"Name : {newData['name']}"
				phoneL["text"] = f"Phone : {newData['phone']}"
				emailL["text"] = f"Email : {newData['email']}"
				totalL["text"] = f"Total : {newData['marks']}"
				perL["text"] = f"Percentage  : {self.per}"

stud = Student()

nameLabel = Label(root , text="Name :")
nameLabel.place(x=30,y=50)
emailLabel = Label(root , text="Email :")
emailLabel.place(x=30,y=80)
phoneLabel = Label(root , text="phone :")
phoneLabel.place(x=30,y=110)
sub1Label = Label(root , text="sub1 :")
sub1Label.place(x=30,y=140)
sub2Label = Label(root , text="sub2 :")
sub2Label.place(x=30,y=160)
sub3Label = Label(root , text="sub3 :")
sub3Label.place(x=30,y=190)
sub4Label = Label(root , text="sub4 :")
sub4Label.place(x=30,y=220)
sub5Label = Label(root , text="sub5 :")
sub5Label.place(x=30,y=250)

nameEntry = Entry(root)
nameEntry.place(x=80,y=50)
emailEntry = Entry(root)
emailEntry.place(x=80,y=80)
phoneEntry = Entry(root)
phoneEntry.place(x=80,y=110)
sub1Entry = Entry(root)
sub1Entry.place(x=80,y=140)
sub2Entry = Entry(root)
sub2Entry.place(x=80,y=160)
sub3Entry = Entry(root)
sub3Entry.place(x=80,y=190)
sub4Entry = Entry(root)
sub4Entry.place(x=80,y=220)
sub5Entry = Entry(root)
sub5Entry.place(x=80,y=250)

btnSubmit = Button(root,text="Submit",width=25,command=lambda:stud.insertData())
btnSubmit.place(x=80,y=280)

reschLabel = Label(root,text="Sreach Roll No :")
reschLabel.place(x=210,y=50)

reschEntry = Entry(root)
reschEntry.place(x=300,y=50)

btnShow = Button(root,text="Show Data",width=25,command=lambda:stud.showData())
btnShow.place(x=300,y=80)


nameL = Label(root , text="Name :")
nameL.place(x=300,y=110)
emailL = Label(root , text="Email :")
emailL.place(x=300,y=140)
phoneL = Label(root , text="phone :")
phoneL.place(x=300,y=170)
totalL = Label(root , text="Total :")
totalL.place(x=300,y=200)
perL = Label(root , text="Percentage :")
perL.place(x=300,y=230)

root.mainloop()