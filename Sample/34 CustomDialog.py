from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
import string
import os
import time
from tkinter.messagebox import *

root = Tk()
root.title('Custom Dialog Demo V1.0')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.maxsize(width=screen_w, height=screen_h)
rw = int(screen_w / 2)
rh = int(screen_h / 2)
root.geometry('{}x{}+{:g}+{:g}'.format(rw, rh, rw / 2, rh / 2))

top_menu = Menu(root)
root.config(menu=top_menu)

file_menu = Menu(top_menu, tearoff=False)
top_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

theme_menu = Menu(top_menu, tearoff=False)
top_menu.add_cascade(label='Theme', menu=theme_menu)

theme = StringVar()
theme.set(Style().theme_use())
for t in Style().theme_names():
    theme_menu.add_radiobutton(label=t, value=t, variable=theme)

def theme_changed(*arg):
    Style().theme_use(theme.get())
theme.trace_variable('w', theme_changed)


paned_window = PanedWindow(root, orient=HORIZONTAL)
paned_window.grid(row=0, column=0, sticky='eswn')

#生成Frame容器以容纳TreeView,Scrollbar
tree_area = Frame(paned_window)
# 设定水平伸展
tree_area.grid_rowconfigure(0, weight=1)
# 设定垂直伸展
tree_area.grid_columnconfigure(0, weight=1)
# 生成TreeView
tree_view = Treeview(tree_area, show='tree', selectmode='browse')
# 设定TreeView布局位置
tree_view.grid(row=0, column=0, sticky='nsew')

# 生成垂直滚动条
scroll_ty = Scrollbar(tree_area, orient=VERTICAL, command=tree_view.yview)
# 设定滚动条布局位置
scroll_ty.grid(row=0, column=1, sticky=N+S)
# 关联滚动动作
tree_view['yscrollcommand']=scroll_ty.set

# 生成水平滚动条
scroll_tx = Scrollbar(tree_area, orient=HORIZONTAL, command=tree_view.xview)
# 设定滚动条布局位置
scroll_tx.grid(row=1, column=0, sticky=E+W)
# 关联滚动动作
tree_view['xscrollcommand']=scroll_tx.set

paned_window.add(tree_area)

cur_path = os.path.abspath(os.path.dirname(__file__))
pc_image = PhotoImage(file=cur_path + '\\images\\pc.png')
drive_image = PhotoImage(file=cur_path + '\\images\\drive.png')
folder_image = PhotoImage(file=cur_path + '\\images\\folder.png')
file_image = PhotoImage(file=cur_path + '\\images\\file.png')

pc_node= tree_view.insert('', 'end',
                          text=os.environ.get('COMPUTERNAME'),
                          image=pc_image,
                          open=False)
for c in string.ascii_uppercase:
    disk = c + ':'
    if os.path.isdir(disk):
        drive_node = tree_view.insert(pc_node, 'end', text=disk, image=drive_image)

def insert_child_items(parent_node):
    path = node_path(parent_node)
    if os.path.isdir(path):
        try:
            dir_items = os.scandir(path)
            for item in dir_items:
                if item.is_dir() and ('.$'.find(item.name[0])<0):
                    tree_view.insert(parent_node, 'end', text=item.name, image=folder_image)
        except Exception as e:
            print(e)

def open_node(event):
    focus = tree_view.focus()
    for node in tree_view.get_children(focus):
        insert_child_items(node)

tree_view.bind('<<TreeviewOpen>>', open_node)

def close_node(event):
    focus = tree_view.focus()
    for node in tree_view.get_children(focus):
        children = tree_view.get_children(node)
        for c in children:
            tree_view.delete(c)

tree_view.bind('<<TreeviewClose>>', close_node)

detail_area = Frame(paned_window)
detail_area.grid_rowconfigure(0, weight=1)
detail_area.grid_columnconfigure(0, weight=1)
paned_window.add(detail_area)

list_view = Treeview(detail_area)
list_view['columns'] = ('#1', '#2', "#3", '#4')
list_view.column("#0", width=150, minwidth=150, stretch=YES)
list_view.column("#1", width=150, minwidth=150, stretch=YES)
list_view.column("#2", width=100, minwidth=100, stretch=YES)
list_view.column("#3", width=100, minwidth=100, stretch=NO)
list_view.column("#4", width=100, minwidth=50, stretch=YES)

list_view.heading("#0", text="Name", anchor=W)
list_view.heading("#1", text="Date modified", anchor=W)
list_view.heading("#2", text="Type", anchor=W)
list_view.heading("#3", text="Size", anchor=W)

list_view.grid(row=0, column=0, sticky='nsew')

scroll_fy = Scrollbar(detail_area, orient=VERTICAL, command=list_view.yview)
scroll_fy.grid(row=0, column=1, sticky=N+S)
list_view['yscrollcommand']=scroll_fy.set

scroll_fx = Scrollbar(detail_area, orient=HORIZONTAL, command=list_view.xview)
scroll_fx.grid(row=1, column=0, sticky=E+W)
list_view['xscrollcommand']=scroll_fx.set

Sizegrip(detail_area).grid(row=1, column=1)

def select_node(event):
    children = list_view.get_children('')
    for c in children:
        list_view.delete(c)
    focus = tree_view.focus()
    path = node_path(focus)
    if os.path.isdir(path):
        try:
            dir_items = os.scandir(path)
            iid = 0
            for item in dir_items:
                if item.is_file() and ('.$'.find(item.name[0]) < 0):
                    stat_info = os.stat(item.path)
                    m_time = time.strftime("%Y/%m/%d %H:%M", time.localtime(stat_info.st_mtime))
                    type = ' File'
                    dot_pos = item.name.rfind('.')
                    if dot_pos > 0:
                        type = item.name[dot_pos+1:].upper() + type
                    list_view.insert('', 'end', str(iid), text=item.name, values=(m_time, type, stat_info.st_size))
                    iid += 1
        except Exception as e:
            print(e)

tree_view.bind('<<TreeviewSelect>>', select_node)

def selected_files():
    try:
        dir_node = tree_view.focus()
        if dir_node:
            path = node_path(dir_node)
            return path, map(lambda x:list_view.item(x, 'text'), list_view.selection())
    except Exception as e:
        showerror('Error', str(e))
        return None

def open_current():
    path, selections = selected_files()
    if path:
        for fn in selections:
            os.startfile(os.path.join(path, fn))


def center_window(wnd, ref):
    wnd.update()
    width = wnd.winfo_width()
    height = wnd.winfo_height()
    if ref:
        ref_width = ref.winfo_width()
        ref_height = ref.winfo_height()
        x = ref.winfo_x()
        y = ref.winfo_y()
        size = '%dx%d+%d+%d' % (width, height, x + (ref_width - width) / 2, y+(ref_height - height) / 2)
    else:
        s_width = wnd.winfo_screenwidth()
        s_height = wnd.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (s_width - width) / 2, (s_height - height) / 2)
    wnd.geometry(size)

def rename_ok(dlg, path, src, des):
    if src == des:
        return
    try:
        src = os.path.join(path, src)
        des = os.path.join(path, des)
        os.rename(src, des)
    except Exception as e:
        showerror('Error', str(e))
    dlg.quit()


def rename_current():
    path, selections = selected_files()
    if path:
        for fn in selections:
            # 构建顶层窗口作为对话框
            rename_dlg = Toplevel(takefocus=True)
            # 指定窗口标题
            rename_dlg.title('Rename')
            # 禁止窗口尺寸调整
            rename_dlg.resizable(width=False, height=False)
            # 构建Frame对象以容纳Label和Entry对象
            # 使用Frame可以分别调整Label/Entry区域和下面的按钮区域
            fn_frame = Frame(rename_dlg)
            fn_frame.grid(row=0,column=0)
            Label(fn_frame, text='File Name:').grid(row=0, column=0)
            fn_var = StringVar()
            fn_var.set(fn)
            fn_entry = Entry(fn_frame, textvariable=fn_var)
            fn_entry.grid(row=0, column=1)
            # 构建Frame对象以容纳OK和Cancel按钮
            btn_frame = Frame(rename_dlg)
            btn_frame.grid(row=1, column=0, sticky='e')
            # 通过labmda表达式传递构建按钮控件时的对话框控件，路径和文件名信息
            # 修改后的文件名要在按下【OK】按钮是通过fn_var.get获取。
            ok_btn = Button(btn_frame, text='OK',
                            command=(lambda w=rename_dlg,p=path,s=fn: rename_ok(w,p,s,fn_var.get())))
            ok_btn.grid(row=0, column=0)
            # 取消按钮直接销毁窗口对象
            cancel_btn=Button(btn_frame, text='Cancel', command=rename_dlg.destroy)
            cancel_btn.grid(row=0, column=1)
            # 限定rename_dlg接收鼠标和键盘事件，这是实现模态对话框的关键。
            rename_dlg.grab_set()
            # 使对话框相对于root窗口居中
            center_window(rename_dlg, root)
            # 启动对话框主循环
            rename_dlg.mainloop()
            # 销毁对话框窗口
            rename_dlg.destroy()
            # 更新文件列表
            select_node(None)

def delete_current():
    path, selections = selected_files()
    if path and askokcancel('askokcancel', 'Delete the file has been selected?'):
        try:
            for fn in selections:
                os.remove(os.path.join(path, fn))
        except Exception as e:
            showerror('Delete file Error', str(e))
        select_node(None)

def rbutton_down(event):
    iid = list_view.identify_row(event.y)
    if iid:
        if iid not in list_view.selection():
            list_view.selection_set(iid)
            list_view.focus(iid)
        path, selections = selected_files()
        if path:
            menu = Menu(list_view, tearoff=False)
            menu.add_command(label='Open', command=open_current)
            if len(list(selections))==1:
                menu.add_command(label='Rename', command=rename_current)
            menu.add_command(label='Delete', command=delete_current)
            menu.post(event.x_root, event.y_root)

    # 绑定鼠标右键
list_view.bind('<ButtonPress-3>', rbutton_down)


root.mainloop()