from tkinter import *

root=Tk()
root.title("simple caculator")
root.config(bg="black")
root.geometry("500x200")

options=["+","-","*","/","%"]

def choose(*arg):
    if var.get()=="+":
        a=int(ent1.get())
        b=int(ent2.get())
        c=a+b
        lab26.config(text="%d"%c,fg="black",bg="white",font="none 16")
        return c
    elif var.get()=="-":
        a = int(ent1.get())
        b = int(ent2.get())
        c = a - b
        lab26.config(text="%d"%c,fg="black",bg="white",font="none 16")
        return c

    elif var.get() == "*":
        a = int(ent1.get())
        b = int(ent2.get())
        c = a * b
        lab26.config(text="%d"%c,fg="black",bg="white",font="none 16")
        return c

    elif var.get() == "/":
        a = int(ent1.get())
        b = int(ent2.get())
        c = a // b
        lab26.config(text="%d"%c,fg="black",bg="white",font="none 16")
        return c

    elif var.get() == "%":
        a = int(ent1.get())
        b = int(ent2.get())
        c = a % b
        lab26.config(text="%d"%c,fg="black",bg="white",font="none 16")
        return c


lab1=Label(root,text="     ",bg="black").grid(row=0)

ent1=Entry(root,bg="white",fg="black",font="none 16",width=10)
ent1.grid(row=2,column=0)

lab21=Label(root,text="   ",bg="black").grid(row=2,column=1)

var=StringVar()
var.set(options[0])

opt=OptionMenu(root,var,"+","-","*","/","%")
opt.grid(row=2,column=2)
    
lab22=Label(root,text="   ",bg="black").grid(row=2,column=3)

ent2=Entry(root,bg="white",fg="black",font="none 16",width=10)
ent2.grid(row=2,column=4)

lab23=Label(root,text="   ",bg="black").grid(row=2,column=5)

lab24=Label(root,text="  =  ",font="none 16",bg="white",fg="black").grid(row=2,column=6)

lab25=Label(root,text="   ",bg="black").grid(row=2,column=7)

lab26=Label(root)
lab26.grid(row=2,column=8)

but=Button(root,text="calculate",fg="black",bg="red",width=10,height=2,font="none 16",command=choose).place(x=170,y=100)
root.mainloop()