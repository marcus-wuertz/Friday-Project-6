#Import required packages
from tkinter import *
from tkinter import ttk

# establish parent widget
root = Tk()

#create widget to make entry box for the calculator
calcOutput=ttk.Entry(root)
calcOutput.pack(side='top')
