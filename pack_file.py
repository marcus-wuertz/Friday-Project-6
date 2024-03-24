#Import required packages
from tkinter import *
from tkinter import ttk

# establish parent widget
root = Tk()

#create widget to make entry box for the calculator
calcOutput=ttk.Entry(root)
calcOutput.pack(side='top')

# create widget to add buttons for +,-,*,and /
calcBtnDivide=ttk.Button(root, text='÷')
calcBtnDivide.pack(side='right')


calcBtnMultiply=ttk.Button(root, text='x')
calcBtnMultiply.pack(side='right')

calcBtnSub=ttk.Button(root, text='-')
calcBtnSub.pack(side='right')