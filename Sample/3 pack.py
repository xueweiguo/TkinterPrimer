from tkinter import *

root = Tk()
Button(root, text="Cat").pack(side=LEFT, expand=YES, fill=BOTH)
Button(root, text="Dog").pack(side=LEFT, expand=YES, fill=BOTH)
Button(root, text="Tiger").pack(side=TOP, expand=YES, fill=BOTH)
Button(root, text="Bear").pack(side=TOP, expand=YES, fill=BOTH)

'''
Button(root, text="C").pack(side=RIGHT, expand=YES, fill=BOTH)
Button(root, text="D").pack(side=LEFT, expand=NO, fill=Y)
Button(root, text="E").pack(side=TOP, expand=YES, fill=BOTH)
Button(root, text="E1").pack(side=LEFT, expand=YES, fill=BOTH)
Button(root, text="E1").pack(side=LEFT, expand=YES, fill=BOTH)

Button(root, text="F").pack(side=RIGHT, expand=NO, fill=NONE)
Button(root, text="G").pack(side=BOTTOM, expand=YES, fill=Y)
Button(root, text="H").pack(side=TOP, expand=NO, fill=BOTH)
Button(root, text="I").pack(side=RIGHT, expand=NO)
Button(root, text="J").pack(anchor=SE)
'''
root.mainloop()