from tkinter import *
root=Tk()
root.title("Addition")
root.geometry("400x200")
heading=Label(root,text="Addition")
heading.pack()
a=Label(root,text="1")
a.pack()
b=Label(root,text="2")
b.pack()
sum=Label(root)
sum.pack()
def add():
    r=1+2
    sum["text"]=str(r)


btn=Button(root,text="Add", command=add)
btn.pack()

root.mainloop()