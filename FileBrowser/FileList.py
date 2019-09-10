import os

from tkinter.messagebox import *
import time
from ListView import *
from RenameDialog import *


class FileList(ListView):
    def __init__(self, master, **kwargs):
        ListView.__init__(self, master, columns=5, size_grip=True)
        self.column("#0", width=150, minwidth=150, stretch=YES)
        self.column("#1", width=150, minwidth=150, stretch=YES)
        self.column("#2", width=100, minwidth=100, stretch=YES)
        self.column("#3", width=100, minwidth=100, stretch=NO)
        self.column("#4", width=100, minwidth=50, stretch=YES)

        self.heading("#0", text="Name", anchor=W)
        self.heading("#1", text="Date modified", anchor=W)
        self.heading("#2", text="Type", anchor=W)
        self.heading("#3", text="Size", anchor=W)
        self.enable_edit('#0', True)
        self.tree_view = kwargs.get('tree_view')
        # 绑定鼠标右键
        self.bind('<ButtonPress-3>', self.popup_menu)

    def entry_confirmed(self, row, col, text):
        self.set_text(row, col, text)

    def selected_files(self):
        try:
            dir_node = self.tree_view.focus()
            if dir_node:
                path = self.tree_view.node_path(dir_node)
                return path, map(lambda x: self.item(x, 'text'), self.selection())
        except Exception as e:
            showerror('Error', str(e))
            return None

    def open_current(self):
        path, selections = self.selected_files()
        if path:
            for fn in selections:
                os.startfile(os.path.join(path, fn))

    def rename_current(self):
        path, selections = self.selected_files()
        if path:
            for fn in selections:
                dlg = RenameDialog(self, path, fn)
            self.select_node(None)

    def delete_current(self):
        path, selections = self.selected_files()
        if path and askokcancel('askokcancel', 'Delete the file has been selected?'):
            try:
                for fn in selections:
                    os.remove(os.path.join(path, fn))
            except Exception as e:
                showerror('Delete file Error', str(e))
            self.select_node(None)

    def popup_menu(self, event):
        iid = self.identify_row(event.y)
        if iid:
            if iid not in self.selection():
                self.selection_set(iid)
                self.focus(iid)
            path, selections = self.selected_files()
            if path:
                menu = Menu(self, tearoff=False)
                menu.add_command(label='Open', command=self.open_current)
                if len(list(selections)) == 1:
                    menu.add_command(label='Rename', command=self.rename_current)
                menu.add_command(label='Delete', command=self.delete_current)
                menu.post(event.x_root, event.y_root)

    def select_node(self, event):
        children = self.get_children('')
        for c in children:
            self.delete(c)
        focus = self.tree_view.focus()
        path = self.tree_view.node_path(focus)
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
                            type = item.name[dot_pos + 1:].upper() + type
                        self.insert('', 'end', str(iid), text=item.name, values=(m_time, type, stat_info.st_size))
                        iid += 1
            except Exception as e:
                print(e)





