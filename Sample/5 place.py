from tkinter import *
root = Tk()
# 绝对位置
Button(root,text="绝对坐标摆放1").place(x=20, y=10, width=150, height=50)
Button(root, text="绝对坐标摆放2").place(x=20, y = 80, width=150, height=50)
'''
Button(root,text="相对坐标摆放1").place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.2)
Button(root,text="相对坐标摆放2").place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.2)
'''
root.mainloop()
