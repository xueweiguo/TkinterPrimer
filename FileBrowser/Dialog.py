from tkinter import *
from tkinter.ttk import *
from utilities import center_window

class Dialog(Toplevel):
    def __init__(self, ref, title):
        Toplevel.__init__(self, takefocus=True)
        self.ref = ref
        # 指定窗口标题
        self.title(title)
        # 禁止窗口尺寸调整
        self.resizable(width=False, height=False)
        self.create_widgets()
        # 限定rename_dlg接收鼠标和键盘事件，这是实现模态对话框的关键。
        self.grab_set()
        # 使对话框相对于root窗口居中
        center_window(self, ref)
        # 启动对话框主循环
        self.mainloop()

    def create_widgets(self):
        pass