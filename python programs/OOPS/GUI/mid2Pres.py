import tkinter as tk 



root  = tk.Tk()
root.geometry("500x500")
root.title("Mid 2 Exam ")


nameLable = tk.Label(root,text="Enter name :",height=2)
nameLable.place(x=10,y=10)

nameEntry = tk.Entry(root,font="joker",border="2px",width=10)
nameEntry.place(x=80 , y=10)

checkBox1  = tk.Checkbutton(root,text="Kb")
checkBox1.place(x=80,y=40)

checkBox2 = tk.Checkbutton(root,text="Kishan")
checkBox2.place(x=80,y=70)

radio1 = tk.Radiobutton(root,text="KB")
radio1.place(x=80,y=100)

radio2 = tk.Radiobutton(root,text="kishan")
radio2.place(x=80,y=120)

spinbox1 = tk.Spinbox(root,from_=0 , to_= 10)
spinbox1.place(x=80,y=150)

labelframe = tk.LabelFrame(root, text="This is a LabelFrame")
labelframe.place(x=100,y=180)
left = tk.Label(root, text="Inside the LabelFrame")



root.mainloop()