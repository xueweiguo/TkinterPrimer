#from tkinter import *
import tkinter as tk
# 构建主窗口
main = tk.Tk()
# 构建标签
tk.Label(main, text='Hello Tkinter!').pack()
# 构建退出按钮
tk.Button(main, text='Quit', command=main.quit).pack()
# 执行主循环
main.mainloop()