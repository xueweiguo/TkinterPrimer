import os
from tkinter.messagebox import *
from Dialog import *

class RenameDialog(Dialog):
    def __init__(self, file_list, path, fn):
        self.path = path
        self.fn = fn
        self.fn_var = StringVar()
        self.fn_var.set(self.fn)
        Dialog.__init__(self, file_list.winfo_toplevel(), 'Rename File')

    def create_widgets(self):
        # 构建Frame对象以容纳Label和Entry对象
        # 使用Frame可以分别调整Label/Entry区域和下面的按钮区域
        fn_frame = Frame(self)
        fn_frame.grid(row=0, column=0)
        Label(fn_frame, text='File Name:').grid(row=0, column=0)
        fn_entry = Entry(fn_frame, textvariable=self.fn_var)
        fn_entry.grid(row=0, column=1)
        # 构建Frame对象以容纳OK和Cancel按钮
        btn_frame = Frame(self)
        btn_frame.grid(row=1, column=0, sticky='e')
        # 通过labmda表达式传递构建按钮控件时的对话框控件，路径和文件名信息
        # 修改后的文件名要在按下【OK】按钮是通过fn_var.get获取。
        ok_btn = Button(btn_frame, text='OK', command=self.__rename)
        ok_btn.grid(row=0, column=0)
        # 取消按钮直接销毁窗口对象
        cancel_btn = Button(btn_frame, text='Cancel', command=self.destroy)
        cancel_btn.grid(row=0, column=1)

    def __rename(self):
        if self.fn_var.get() == self.fn:
            return
        try:
            src = os.path.join(self.path, self.fn)
            des = os.path.join(self.path, self.fn_var.get())
            os.rename(src, des)
        except Exception as e:
            showerror('Error', str(e))
        self.quit()
