from tkinter import *
root = Tk()
Label(root, text="用户名").grid(row=0, sticky=W)
Label(root, text="密码").grid(row=1, sticky=W)
Entry(root).grid(row=0, column=1, sticky=E, columnspan=2)
Entry(root).grid(row=1, column=1, sticky=E, columnspan=2)
Button(root, text="Cancel").grid(row=2, column=1, sticky=E+W)
Button(root, text="Login").grid(row=2, column=2, sticky=E+W)
root.mainloop()