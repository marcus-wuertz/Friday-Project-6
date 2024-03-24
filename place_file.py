from tkinter import *
from tkinter import ttk

# Establish parent widget
root = Tk()
root.title("Log in page")

# Set the size of the GUI window
window_width = 400
window_height = 300
root.geometry(f"{window_width}x{window_height}")

# create widget for welcome message
label1= ttk.Label(root, text='Returning user? Log in here!', font=('TkDefaultFont',20))
label1.place(x=25, y=25)

# create a button for new users to create an account
newUsrBtn=ttk.Button(root, text='New user? Click here to make an account')
newUsrBtn.place(x=80,y=65)

# create a label for username
usrNameLbl= ttk.Label(root, text='Username',font=(16))
usrNameLbl.place(x=0, y=105)

# create an entry box for username
usrNameEntry=ttk.Entry(root)
usrNameEntry.place(x=80, y=105)

# create a label for password
pswrdLbl= ttk.Label(root, text='Password',font=(16))
pswrdLbl.place(x=0, y=145)

# create an entry box for password
pswrdEntry=ttk.Entry(root)
pswrdEntry.place(x=80, y=145)
