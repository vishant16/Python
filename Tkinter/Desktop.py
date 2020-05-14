from tkinter import *
import Desktop_backend

window=Tk() #object of screen

def view_command():
    for i in Desktop_backend.view():
        detail.insert(END,i)

l1=Label(window,text="Product")
l1.grid(row=0,column=0) #positon

e1=Entry(window,textvariable=StringVar())
e1.grid(row=0,column=1)

l1=Label(window,text="Profit")
l1.grid(row=0,column=2)

e1=Entry(window,textvariable=StringVar())
e1.grid(row=0,column=3)

l1=Label(window,text="Loss")
l1.grid(row=1,column=0)

e1=Entry(window,textvariable=StringVar())
e1.grid(row=1,column=1)

l1=Label(window,text="Client")
l1.grid(row=1,column=2)

e1=Entry(window,textvariable=StringVar())
e1.grid(row=1,column=3)

detail=Listbox(window,height=6,width=35)
detail.grid(row=2,column=0,rowspan=6,columnspan=2)

sb=Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6)

detail.configure(yscrollcommand=sb.set)
sb.configure(command=detail.yview)

b=Button(window,text="view all",width=12,command=view_command)
b.grid(row=2,column=3)
b1=Button(window,text="Search",width=12)
b1.grid(row=3,column=3)
b2=Button(window,text="Add",width=12)
b2.grid(row=4,column=3)
b3=Button(window,text="Update",width=12)
b3.grid(row=5,column=3)
b4=Button(window,text="Delete",width=12)
b4.grid(row=6,column=3)
b5=Button(window,text="close",width=12)
b5.grid(row=7,column=3)

window.mainloop()
