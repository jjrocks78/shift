from tkinter import *

def sum():
    a1=a.get()
    b1 =b.get()
    c=int(a1)+int(b1)
    labelResult.config(text="sum is %d" %c)
    return c

def sub():
    a1=a.get()
    b1 =b.get()
    c=int(a1)-int(b1)
    labelResult.config(text="difference is %d" %c)
    return c

def mul():
    a1=a.get()
    b1 =b.get()
    c=int(a1)*int(b1)
    labelResult.config(text="product is %d" %c)
    return c

def div():
    a1=a.get()
    b1 =b.get()
    c=int(a1)//int(b1)
    e=int(a1)%int(b1)
    labelResult.config(text="quotient is %d" %c  + "\nremainder is %d" % e)
    return c,e
window = Tk()
window.title("calculator")
window.config(bg='black')
photo1=PhotoImage(file='/home/cocoslabs/Desktop/images_lpr/agif1opt.gif')
label=Label(window,image=photo1,bg="black").pack()
label1=Label(window,text="enter a",bg="black",fg="white",font="none 14").pack()
a=StringVar()
entry1=Entry(window,textvariable=a,fg="black",width=20)
entry1.pack()

label2=Label(window,text="enter b",fg="white",bg="black",font="none 14").pack()
b=StringVar()
entry2 = Entry(window,textvariable=b, fg="black",width=20)
entry2.pack()


label4=Label(window,text="",fg="black",bg="black",font="none 14").pack()
Button(window,fg="red",text="Sum",bg="blue",width=25,height=2,command=sum).pack()
Button(window,fg="red",text="Difference",bg="blue",width=25,height=2,command=sub).pack()
Button(window,fg="red",text="Product",bg="blue",width=25,height=2,command=mul).pack()
Button(window,fg="red",text="Division",bg="blue",width=25,height=2,command=div).pack()
#op=StringVar()
label4=Label(window,text="",fg="black",bg="black",font="none 14").pack()

labelResult = Label(window)
labelResult.pack()
label3=Label(window,text="",fg="black",bg="black",font="none 14").pack()

"""op=Text(window,text=sum(),width=20,background="white",height=2).pack()"""

window.mainloop()

