# import random
# import string
# from tkinter import *
#
# root=Tk()
# root.title("Name Place Things Animals")
# root.config(bg="black")
# root.geometry("500x200")


# from tkinter import *
# import time
# tk=Tk()
# def clock():
#     t=time.strftime('%I:%M:%S',time.localtime())
#     if t!='':
#         label1.config(text=t,font='times 25')
#     tk.after(100,clock)
# label1=Label(tk,justify='center')
# label1.pack()
# clock()
# tk.mainloop()

from tkinter import *
import time
tk=Tk()
def clock():
    t=60
    for i in range(t):
        st = t - i
        print(st," seconds")
        time.sleep(1)
        #label1.config(text="%s"%st,font='times 25')
    # tk.after(1,clock)
label1=Label(tk,justify='center')
label1.pack()
# clock()
tk.mainloop()