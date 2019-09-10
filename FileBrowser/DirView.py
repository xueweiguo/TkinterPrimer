from tkinter import *
from tkinter.ttk import *
import os
import string


class DirView(Treeview):
    def __init__(self, master):
        Treeview.__init__(self, master, show='tree', selectmode='browse')
        self.__prepare_images()
        self.pc_node = self.insert('', 'end',
                                   text=os.environ.get('COMPUTERNAME'),
                                   image=self.pc_image,
                                   open=False)
        for c in string.ascii_uppercase:
            disk = c + ':'
            if os.path.isdir(disk):
                drive_node = self.insert(self.pc_node, 'end',
                                         text=disk, image=self.drive_image)
        self.bind('<<TreeviewOpen>>', self.open_node)
        self.bind('<<TreeviewClose>>', self.close_node)

    def close_node(self, event):
        focus = self.focus()
        for node in self.get_children(focus):
            children = self.get_children(node)
            for c in children:
                self.delete(c)

    def node_path(self, node):
        path = ''
        parent = node
        while parent:
            node_text = self.item(parent, 'text')
            if len(path) > 0:
                path = os.path.join(node_text, path)
            else:
                path = node_text
            parent = self.parent(parent)
        return path

    def insert_child_items(self, parent_node):
        path = self.node_path(parent_node)
        if os.path.isdir(path):
            try:
                dir_items = os.scandir(path)
                for item in dir_items:
                    if item.is_dir() and ('.$'.find(item.name[0]) < 0):
                        self.insert(parent_node, 'end', text=item.name, image=self.folder_image)
            except Exception as e:
                print(e)

    def open_node(self, event):
        focus = self.focus()
        for node in self.get_children(focus):
            self.insert_child_items(node)

    def __prepare_images(self):
        cur_path = os.path.abspath(os.path.dirname(__file__))
        self.pc_image = PhotoImage(file=cur_path + '\\images\\pc.png')
        self.drive_image = PhotoImage(file=cur_path + '\\images\\drive.png')
        self.folder_image = PhotoImage(file=cur_path + '\\images\\folder.png')
        self.file_image = PhotoImage(file=cur_path + '\\images\\file.png')