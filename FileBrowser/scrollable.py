from tkinter import *
from tkinter.ttk import *


def scrollable(master, w_type, **kwargs):
    # 获取SizeGrip设定内容
    size_grip = kwargs.get('size_grip')
    # 从关键词参数中去掉'size_grip'设定
    if size_grip:
        kwargs.pop('size_grip')
    # 构建Frame控件
    frame = Frame(master)
    # 设定控件水平伸展
    frame.grid_rowconfigure(0, weight=1)
    # 设定控件垂直伸展
    frame.grid_columnconfigure(0, weight=1)
    # 构建控件
    widget = w_type(frame, **kwargs)
    # 设定控件布局
    widget.grid(row=0, column=0, sticky='nsew')
    # 构建垂直Scrollbar
    scroll_y = Scrollbar(frame, orient=VERTICAL, command=widget.yview)
    # 设定控件布局
    scroll_y.grid(row=0, column=1, sticky=N + S)
    # 绑定滚动动作
    widget['yscrollcommand'] = scroll_y.set
    # 构建水平Scrollbar
    scroll_x = Scrollbar(frame, orient=HORIZONTAL, command=widget.xview)
    # 设定控件布局
    scroll_x.grid(row=1, column=0, sticky=E + W)
    # 绑定滚动动作
    widget['xscrollcommand'] = scroll_x.set
    # 生成Sizegrip控件
    if size_grip:
        Sizegrip(frame).grid(row=1, column=1)
    return frame,widget

