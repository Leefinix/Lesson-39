from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x300')

frame = Frame(master=root, height=200, width=360, bg="#d0efff")

lbl1 = Label(frame, text="Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(frame, text="Email", bg="#3895D3", fg='white', width=12)
lbl3 = Label(frame, text="Password", bg="#3895D3", fg='white', width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="*")

def display():
    name = name_entry.get()
    greet = "Hey " + name + "!"
    message = "\nCongratulations on your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg="#BEBEBE", fg="black")
button = Button(text="Sign up", command=display, bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20 , y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
password_entry.place(x=150 , y=140)
button.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()