from tkinter import *
root1=Tk()
root1.title("Choice")
root1.geometry("725x250")

def add():
    root2=Tk()
    root2.title("addition")
    root2.geometry("300x300")
    x = StringVar()
    y = StringVar()


    def ad():
        a11 = ent1.get()
        b11 = ent2.get()
        c = int(a11) + int(b11)
        labelResult.config(text="sum is %d" % c)
        return c

    label11=Label(root2,text="enter a",font="none 16")
    label11.grid(row=0)
    ent1=Entry(root2,fg="black",font="none 16")
    ent1.grid(row=0,column=1)

    label12=Label(root2,text="enter b",font="none 16")
    label12.grid(row=1)
    ent2 = Entry(root2, fg="black", font="none 16")
    ent2.grid(row=1, column=1)

    but1=Button(root2,text="sum",width=20,height=2,fg="brown",bg="white",font="none 14",command=ad)
    but1.grid(row=3,column=1)

    labelResult=Label(root2,fg="black")
    labelResult.grid(row=2,column=1)


    root2.mainloop()


def sub():
    root3 = Tk()
    root3.title("subraction")
    root3.geometry("300x300")
    x2 = StringVar()
    y2 = StringVar()

    def su():
        a12 = ent1.get()
        b12 = ent2.get()
        c = int(a12) - int(b12)
        labelResult.config(text="difference is %d" % c)
        return c

    label21 = Label(root3, text="enter a", font="none 16")
    label21.grid(row=0)
    ent1 = Entry(root3,  fg="black", font="none 16",width=20)
    ent1.grid(row=0, column=1)

    label22 = Label(root3, text="enter b", font="none 16")
    label22.grid(row=1)
    ent2 = Entry(root3,  fg="black", font="none 16",width=20)
    ent2.grid(row=1, column=1)

    but1 = Button(root3, text="difference", width=20, height=2, fg="brown", bg="white", font="none 14", command=su)
    but1.grid(row=3, column=1)

    labelResult = Label(root3, fg="black")
    labelResult.grid(row=2, column=1)

    root3.mainloop()


def mul():
    root4 = Tk()
    root4.title("multiplication")
    root4.geometry("300x300")
    x3 = StringVar()
    y3 = StringVar()

    def mu():
        a13 = ent1.get()
        b13 = ent2.get()
        c = int(a13) *int(b13)
        labelResult.config(text="product is %d" % c)
        return c

    label11 = Label(root4, text="enter a", font="none 16")
    label11.grid(row=0)
    ent1 = Entry(root4,  fg="black", font="none 16")
    ent1.grid(row=0, column=1)

    label12 = Label(root4, text="enter b", font="none 16")
    label12.grid(row=1)
    ent2 = Entry(root4, fg="black", font="none 16")
    ent2.grid(row=1, column=1)

    but1 = Button(root4, text="product", width=20, height=2, fg="brown", bg="white", font="none 14", command=mu)
    but1.grid(row=3, column=1)

    labelResult = Label(root4, fg="black")
    labelResult.grid(row=2, column=1)

    root2.mainloop()

def div():
    root5 = Tk()
    root5.title("division")
    root5.geometry("300x300")
    x4 = StringVar()
    y4= StringVar()

    def di():
        a14 = ent1.get()
        b14 = ent2.get()
        c = int(a14) / int(b14)
        e=int(a14)%int(b14)
        labelResult.config(text="quotient is %d" % c +"\nremainder is %d"%e)
        return c

    label11 = Label(root5, text="enter a", font="none 16")
    label11.grid(row=0)
    ent1 = Entry(root5,  fg="black", font="none 16")
    ent1.grid(row=0, column=1)

    label12 = Label(root5, text="enter b", font="none 16")
    label12.grid(row=1)
    ent2 = Entry(root5, fg="black", font="none 16")
    ent2.grid(row=1, column=1)

    but1 = Button(root5, text="division", width=20, height=2, fg="brown", bg="white", font="none 14", command=di)
    but1.grid(row=3, column=1)

    labelResult= Label(root5, fg="black")
    labelResult.grid(row=2, column=1)

    root5.mainloop()


label1=Label(root1,text="choose the operation",font="none 16")
label1.pack()

b1=Button(root1,text="addition",width=20,height=2,font="none 14",fg="red",bg="black",command=add)
b1.place(x=50,y=50)

b2=Button(root1,text="subraction",width=20,height=2,font="none 14",fg="red",bg="black",command=sub)
b2.place(x=50,y=150)

b3=Button(root1,text="multiplcation",width=20,height=2,font="none 14",fg="red",bg="black",command=mul)
b3.place(x=400,y=50)

b4=Button(root1,text="division",width=20,height=2,font="none 14",fg="red",bg="black",command=div)
b4.place(x=400,y=150)



root1.mainloop()

