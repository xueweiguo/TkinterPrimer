from tkinter import *
from tkinter.ttk import *


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
        self.center_window()
        # 启动对话框主循环
        self.mainloop()

    def center_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        ref_width = self.ref.winfo_width()
        ref_height = self.ref.winfo_height()
        x = self.ref.winfo_x()
        y = self.ref.winfo_y()
        size = '%dx%d+%d+%d' % (width, height, x + (ref_width - width) / 2, y+(ref_height - height) / 2)
        self.geometry(size)

    def create_widgets(self):
        pass