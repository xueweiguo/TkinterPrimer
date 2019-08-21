import sys
import os
from tkinter import *
from tkinter.font import *

# 准备命令行执行时需要的系统路径
cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)

# create the main window
root = Tk()

'''
ftTimes1 = Font(family='Times', size=12, weight=BOLD)
ftTimes2 = Font(family='Times', size=48, weight=BOLD)
root.option_add('*Label.background', "#a0ffa0")
root.option_add('*upperDisplay.font', ftTimes1)
root.option_add('*lowerDisplay.font', ftTimes2)
root.option_add('*Button*font', ftTimes1)
'''
root.option_readfile('26 OpDb.txt')

# create a label to change state.
upper_display = Label(root,
                      name='upperDisplay',
                      foreground="#000000",
                      width=24, anchor=E)
upper_display.grid(row=1, column=0, columnspan=4, sticky=E + W)

# create a label to change state.
lower_display = Label(root,
                      name='lowerDisplay',
                      foreground="#000000",
                      width=12, anchor=E)
lower_display.grid(row=2, column=0, columnspan=4, sticky=E + W)

# 如果是刚刚完成计算，者接下来的任何操作都清楚所有显示内容
def clear_result():
    upper = upper_display.cget('text')
    if len(upper) > 0 and upper[len(upper) - 1] == '=':
        clear()
        return True
    else:
        return False

# 清除操作数
def clear_lower():
    clear_result()
    lower_display.config(text='')

# CE按钮.
Button(root, text="CE", name='cekey',
       width=2, command=clear_lower).grid(row=3, column=0, sticky=E + W)

# 清除所有显示内容
def clear():
    upper_display.config(text='')
    lower_display.config(text='')

# C按钮
Button(root, text="C", name='ckey',
       width=2, command=clear).grid(row=3, column=1, sticky=E + W)

# 如果不是计算完成状态，去掉当前操作数的最后一个字符
def back():
    if not clear_result():
        lower = str(lower_display.cget('text'))
        if len(lower) > 0:
            lower_display.config(text=lower[:len(lower) - 1])

# back button.
Button(root, text="<-", name='back',
       width=2, command=back).grid(row=3, column=2, sticky=E + W)

def add_op(op):
    clear_result()
    upper = upper_display.cget('text')
    lower = lower_display.cget('text')
    if len(lower) > 0:
        upper_display.config(text=upper + lower + op)
        lower_display.config(text='')

# change state button.
Button(root, text="÷", name='devkey',
       width=2, command=lambda: add_op('÷')).grid(row=3, column=3, sticky=E + W)
Button(root, text="×", name='mulkey',
       width=2, command=lambda: add_op('×')).grid(row=4, column=3, sticky=E + W)
Button(root, text="-", name='minukey',
       width=2, command=lambda: add_op('-')).grid(row=5, column=3, sticky=E + W)
Button(root, text="+", name='pluskey',
       width=2, command=lambda: add_op('+')).grid(row=6, column=3, sticky=E + W)

def add_number(n):
    clear_result()
    lower = lower_display.cget('text')
    lower_display.config(text=lower + n)

# change nubmer button.
Button(root, text="7", width=2,
       command=lambda: add_number('7')).grid(row=4, column=0, sticky=E + W)
Button(root, text="8", width=2,
       command=lambda: add_number('8')).grid(row=4, column=1, sticky=E + W)
Button(root, text="9", width=2,
       command=lambda: add_number('9')).grid(row=4, column=2, sticky=E + W)
Button(root, text="4", width=2,
       command=lambda: add_number('4')).grid(row=5, column=0, sticky=E + W)
Button(root, text="5", width=2,
       command=lambda: add_number('5')).grid(row=5, column=1, sticky=E + W)
Button(root, text="6", width=2,
       command=lambda: add_number('6')).grid(row=5, column=2, sticky=E + W)
Button(root, text="1", width=2,
       command=lambda: add_number('1')).grid(row=6, column=0, sticky=E + W)
Button(root, text="2", width=2,
       command=lambda: add_number('2')).grid(row=6, column=1, sticky=E + W)
Button(root, text="3", width=2,
       command=lambda: add_number('3')).grid(row=6, column=2, sticky=E + W)
Button(root, text="0", width=2,
       command=lambda: add_number('0')).grid(row=7, column=1, sticky=E + W)
Button(root, text=".", width=2,
       command=lambda: add_number('.')).grid(row=7, column=2, sticky=E + W)

def plus_minus():
    clear_result()
    upper = upper_display.cget('text')
    if len(upper) == 0:
        lower = lower_display.cget('text')
        if lower[0] == '-':
            lower_display.config(text=lower[1:])
        else:
            lower_display.config(text='-' + lower)

Button(root, text="+/-", name='revkey',
       width=2, command=plus_minus).grid(row=7, column=0, sticky=E + W)

def calculate():
    add_op('=')
    upper = upper_display.cget('text')
    upper = upper.replace('=', '')
    upper = upper.replace('÷', '/')
    upper = upper.replace('×', '*')
    result = format(eval(upper), 'g')
    lower_display.config(text=result)

Button(root, text="=", name='equalkey',
       width=2, command=calculate).grid(row=7, column=3, sticky=E + W)

# run main loop.
root.mainloop()
