from tkinter import *
from tkinter import ttk

# Establish parent widget
root = Tk()
root.title("Calculator")

# Create frame for the entry box
entry_frame = ttk.Frame(root)
entry_frame.pack(side='top', fill='x')

# Create entry box for the calculator
calc_output = ttk.Entry(entry_frame, state='disabled')
calc_output.pack(fill='x', expand=True)

# Create frame for the operators
operators_frame = ttk.Frame(root)
operators_frame.pack(side='right', fill='y')

# Create buttons for operators
calc_btn_divide = ttk.Button(operators_frame, text='÷')
calc_btn_divide.pack(side='top')

calc_btn_multiply = ttk.Button(operators_frame, text='×')
calc_btn_multiply.pack(side='top')

calc_btn_sub = ttk.Button(operators_frame, text='-')
calc_btn_sub.pack(side='top')

calc_btn_add = ttk.Button(operators_frame, text='+')
calc_btn_add.pack(side='top')

calc_btn_equal = ttk.Button(operators_frame, text='=')
calc_btn_equal.pack(side='top')

# Create frame for one column of numbers
numbers_frame1 = ttk.Frame(root)
numbers_frame1.pack(side='left')

# Create buttons for numbers
calc_btn_1 = ttk.Button(numbers_frame1, text='1')
calc_btn_1.pack(side='top')

calc_btn_2 = ttk.Button(numbers_frame1, text='2')
calc_btn_2.pack(side='top')

calc_btn_3 = ttk.Button(numbers_frame1, text='3')
calc_btn_3.pack(side='top')

calc_btn_4 = ttk.Button(numbers_frame1, text='4')
calc_btn_4.pack(side='top')

calc_btn_5 = ttk.Button(numbers_frame1, text='5')
calc_btn_5.pack(side='top')

# Create frame for the second column of numbers
numbers_frame2 = ttk.Frame(root)
numbers_frame2.pack(side='left')

calc_btn_6 = ttk.Button(numbers_frame2, text='6')
calc_btn_6.pack(side='top')

calc_btn_7 = ttk.Button(numbers_frame2, text='7')
calc_btn_7.pack(side='top')

calc_btn_8 = ttk.Button(numbers_frame2, text='8')
calc_btn_8.pack(side='top')

calc_btn_9 = ttk.Button(numbers_frame2, text='9')
calc_btn_9.pack(side='top')

calc_btn_decimal = ttk.Button(numbers_frame2, text='.')
calc_btn_decimal.pack(side='top')

root.mainloop()
