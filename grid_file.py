from tkinter import *
from tkinter import ttk

# Establish parent widget
root = Tk()
root.title("Sign up page")

# create widget for welcome message
label1= ttk.Label(root, text='New? Sign up here!', font=(30))
label1.grid(row=0,column=2)

#create a widget for returning users
returnBtn=ttk.Button(root, text='Returning user? Click here to log in')
returnBtn.grid(row=2, column=2)

# create labels and entry boxes for Name
nameLbl= ttk.Label(root, text='Name', font=(18))
nameLbl.grid(row=3, column=1)

nameEntry=ttk.Entry(root)
nameEntry.grid(row=3,column=2)
root.mainloop()