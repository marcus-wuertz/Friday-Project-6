#Import required packages
from tkinter import *
from tkinter import ttk

# establish parent widget
root = Tk()

#create widget to make entry box for the calculator
calcOutput=ttk.Entry(root, state='disabled')
calcOutput.pack(side='top')

# create widget to add buttons for +,-,*,and /
calcBtnDivide=ttk.Button(root, text='÷')
calcBtnDivide.pack(side='right')


calcBtnMultiply=ttk.Button(root, text='x')
calcBtnMultiply.pack(side='right')

calcBtnSub=ttk.Button(root, text='-')
calcBtnSub.pack(side='right')

calcBtnAdd=ttk.Button(root, text='+')
calcBtnAdd.pack(side='right')

calcBtnEqual=ttk.Button(root, text='=')
calcBtnEqual.pack(side='right')

# create widget for numbers in the calculator
calcBtn1=ttk.Button(root, text='1')
calcBtn1.pack(side='left')

calcBtn2=ttk.Button(root, text='2')
calcBtn2.pack(side='left')

calcBtn3=ttk.Button(root, text='3')
calcBtn3.pack(side='left')

calcBtn4=ttk.Button(root, text='4')
calcBtn4.pack(side='left')

calcBtn5=ttk.Button(root, text='5')
calcBtn5.pack(side='left')

calcBtn6=ttk.Button(root, text='6')
calcBtn6.pack(side='left')

calcBtn7=ttk.Button(root, text='7')
calcBtn7.pack(side='left')

calcBtn8=ttk.Button(root, text='8')
calcBtn8.pack(side='left')

calcBtn9=ttk.Button(root, text='9')
calcBtn9.pack(side='left')