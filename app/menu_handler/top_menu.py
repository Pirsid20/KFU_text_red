# app/menu_handler/top_menu.py

from tkinter import Menu
from functools import partial


def create_top_menu(window, file_dropdown_handler, txt):
    menu = Menu(window)

    file_dropdown = Menu(menu, tearoff=False)
    file_dropdown.add_command(label='New', command=partial(file_dropdown_handler, "new", txt))
    file_dropdown.add_command(label='Open', command=partial(file_dropdown_handler, "open", txt))
    file_dropdown.add_command(label='Close', command=lambda: file_dropdown_handler("close", txt))
    file_dropdown.add_separator()
    file_dropdown.add_command(label='Save', command=partial(file_dropdown_handler, "save", txt))
    file_dropdown.add_command(label='Save as', command=partial(file_dropdown_handler, "saveAs", txt))
    file_dropdown.add_separator()
    file_dropdown.add_command(label='Print', command=lambda: file_dropdown_handler("print", txt))

    menu.add_cascade(label='File', menu=file_dropdown)
    window.config(menu=menu)
