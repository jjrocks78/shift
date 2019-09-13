from tkinter import *
import time
root=Tk()
root.title("NAME,PLACE,THINGS,ANIMALS")
root.geometry("500x500")
root.config(bg="black")

def timer():
    return int(t)-c













label=Label(root,text="              ").grid(row=0)
t=60
c=0
while t>=0:
    c+=1
    label1=Label(root,text=timer,bg="black",fg="white").grid(row=1)
    time.sleep(1)


root.mainloop()