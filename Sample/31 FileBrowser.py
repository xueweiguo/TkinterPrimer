from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
import string
import os
import time

root = Tk()
root.title('Tkinter Treeview and PanedWindow Demo V1.0')

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

paned_window = PanedWindow(root, orient=HORIZONTAL)
paned_window.grid(row=0, column=0, sticky='eswn')

tree_area = Frame(paned_window)

# create text widget.
font = Font(family='Arial', size=10)
cur_path = os.path.abspath(os.path.dirname(__file__))
pc_image = PhotoImage(file=cur_path + '\\images\\pc.png')
drive_image = PhotoImage(file=cur_path + '\\images\\drive.png')
folder_image = PhotoImage(file=cur_path + '\\images\\folder.png')
file_image = PhotoImage(file=cur_path + '\\images\\file.png')

tree_view = Treeview(tree_area, show='tree', selectmode='browse')
tree_view.grid(row=0, column=0, sticky='nsew')

scroll_ty = Scrollbar(tree_area, orient=VERTICAL, command=tree_view.yview)
scroll_ty.grid(row=0, column=1, sticky=N+S)
tree_view['yscrollcommand']=scroll_ty.set

scroll_tx = Scrollbar(tree_area, orient=HORIZONTAL, command=tree_view.xview)
scroll_tx.grid(row=1, column=0, sticky=E+W)
tree_view['xscrollcommand']=scroll_tx.set

pc_node= tree_view.insert('', 'end',
                          text=os.environ.get('COMPUTERNAME'),
                          image=pc_image,
                          open=False)

def node_path(node):
    path = ''
    parent = node
    while parent:
        node_text = tree_view.item(parent, 'text')
        if len(path) > 0:
            path = os.path.join(node_text, path)
        else:
            path = node_text
        parent = tree_view.parent(parent)
    return path


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

for c in string.ascii_uppercase:
    disk = c + ':'
    if os.path.isdir(disk):
        drive_node = tree_view.insert(pc_node, 'end', text=disk, image=drive_image)

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

tree_area.grid_rowconfigure(0, weight=1)
tree_area.grid_columnconfigure(0, weight=1)

paned_window.add(tree_area)

detail_area = Frame(paned_window)
# create text widget.
font1 = Font(family='Arial', size=15),
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

detail_area.grid_rowconfigure(0, weight=1)
detail_area.grid_columnconfigure(0, weight=1)
paned_window.add(detail_area)

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

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

print(paned_window.panes())
root.mainloop()