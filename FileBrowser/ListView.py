from tkinter import *
from tkinter.ttk import *


class ItemEdit(Entry):
    def __init__(self, view, row, col):
        Entry.__init__(self, view)
        bbox = view.bbox(row, col)
        cur_width = self['width']
        req_width = self.winfo_reqwidth()
        width = int(cur_width * bbox[2] / req_width)
        self.configure(width=width)
        cur_width = self['width']
        req_width = self.winfo_reqwidth()
        width = int(cur_width * bbox[2] / req_width)
        self.configure(width=width)
        req_width = self.winfo_reqwidth()
        self.insert(INSERT, view.get_text(row, col))
        self.view = view
        self.row = row
        self.col = col
        self.place(x=bbox[0]+(bbox[2]-req_width)/2, y=bbox[1]-1)
        self.bind('<FocusOut>', self.confirm)
        self.bind('<Return>', self.confirm)
        self.focus_set()
        self.update()
        self.bind('<Expose>', self.confirm)

    def confirm(self, event):
        self.view.entry_confirmed(self.row, self.col, self.get())
        self.destroy()

    def config(self, event):
        print(event)


class ListView(Treeview):
    def __init__(self, master, **kwargs):
        columns = kwargs.get('columns')
        kwargs.pop('columns')
        Treeview.__init__(self, master)
        if columns:
            cols = []
            for c in range(1, columns):
                cols.append('#{}'.format(c))
            self['columns'] = cols
        self.editable = {}
        self.bind('<<TreeviewSelect>>', self.item_selected)
        self.bind('<Double-1>', self.item_double_clicked)  # 双击左键进入编辑

    def enable_edit(self, col, editable):
        self.editable[col] = editable

    def item_double_clicked(self, event):
        column = self.identify_column(event.x)  # 列
        row = self.identify_row(event.y)  # 行
        editable = self.editable.get(column)
        if editable:
            ItemEdit(self, row, column)

    def entry_confirmed(self, row, col, text):
        self.set_text(row, col, text)

    def item_selected(self, event):
        try:
            self.master.item_selected(event)
        except:
            pass

    def get_text(self, row, col):
        if col == '#0':
            return self.item(row, 'text')
        else:
            return self.set(row, col)

    def set_text(self, row, col, text):
        if col == '#0':
            self.item(row, text=text)
        else:
            self.set(row, col, text)

    def sort_column(self, cols, reverse):
        key_pairs = []
        for iid in self.get_children(''):
            key = ''
            for c in cols:
                key = key + self.set(iid, c) + '#'
            key_pairs.append((key, iid))

        key_pairs.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (key, iid) in enumerate(key_pairs):
            self.move(iid, '', index)

