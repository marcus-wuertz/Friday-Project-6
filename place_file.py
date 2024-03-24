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
