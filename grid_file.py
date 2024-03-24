from tkinter import *
from tkinter import ttk

# Establish parent widget
root = Tk()
root.title("Sign up page")

# create widget for welcome message
label1= ttk.Label(root, text='New? Sign up here!', font=('TkDefaultFont',20))
label1.grid(row=0,column=2)

#create a widget for returning users
returnBtn=ttk.Button(root, text='Returning user? Click here to log in')
returnBtn.grid(row=2, column=2)

# create labels and entry boxes for first name
nameLbl1= ttk.Label(root, text='First Name', font=('TkDefaultFont',16))
nameLbl1.grid(row=3, column=1)

nameEntry1=ttk.Entry(root)
nameEntry1.grid(row=3,column=2)

# create labels and entry boxes for last name
nameLbl2= ttk.Label(root, text='Last Name', font=('TkDefaultFont',16))
nameLbl2.grid(row=4, column=1)

nameEntry2=ttk.Entry(root)
nameEntry2.grid(row=4,column=2)

# create label and entry box for username
userNameLbl= ttk.Label(root, text='Username', font=('TkDefaultFont',16))
userNameLbl.grid(row=5, column=1)

userNameEntry=ttk.Entry(root)
userNameEntry.grid(row=5,column=2)
root.mainloop()