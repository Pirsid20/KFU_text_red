# app/menu_handler/right_menu.py
from tkinter import Menu, Button, Frame, END, Toplevel, Label, Entry
from tkinter.colorchooser import askcolor


def create_right_menu(window, txt):
    edit_menu_frame = Frame(window)
    edit_menu_frame.grid(row=1, column=1, sticky="nsew")  # Помещаем фрейм на тот же ряд, что и текстовая область
    edit_menu_frame.grid_columnconfigure(0, minsize=70)  # Устанавливаем минимальную ширину фрейма в 100 пикселей

    edit_menu = Menu(edit_menu_frame)

    # Функции для редактирования текста
    def cut_text():
        txt.event_generate("<<Cut>>")

    def copy_text():
        txt.event_generate("<<Copy>>")

    def paste_text():
        txt.event_generate("<<Paste>>")

    def find_and_replace():
        find_replace_window = Toplevel(window)
        find_replace_window.title("Find and Replace")

        Label(find_replace_window, text="Find:").grid(row=0, column=0, padx=4, pady=4)
        find_entry = Entry(find_replace_window)
        find_entry.grid(row=0, column=1, padx=4, pady=4)

        Label(find_replace_window, text="Replace:").grid(row=1, column=0, padx=4, pady=4)
        replace_entry = Entry(find_replace_window)
        replace_entry.grid(row=1, column=1, padx=4, pady=4)

        def replace_text():
            find_text = find_entry.get()
            replace_text = replace_entry.get()
            content = txt.get(1.0, END)
            new_content = content.replace(find_text, replace_text)
            txt.delete(1.0, END)
            txt.insert(1.0, new_content)

        Button(find_replace_window, text="Replace", command=replace_text).grid(row=2, column=0, columnspan=2, pady=4)

    # Создаем кнопки в меню редактирования
    cut_button = Button(edit_menu_frame, text="Cut", command=cut_text)
    cut_button.grid(row=0, column=0, sticky="ew", pady=2)

    copy_button = Button(edit_menu_frame, text="Copy", command=copy_text)
    copy_button.grid(row=1, column=0, sticky="ew", pady=2)

    paste_button = Button(edit_menu_frame, text="Paste", command=paste_text)
    paste_button.grid(row=2, column=0, sticky="ew", pady=2)

    clear_button = Button(edit_menu_frame, text="Clear", command=lambda: txt.delete(1.0, END))
    clear_button.grid(row=3, column=0, sticky="ew", pady=2)

    select_all_button = Button(edit_menu_frame, text="Select All", command=lambda: txt.tag_add("sel", "1.0", "end"))
    select_all_button.grid(row=4, column=0, sticky="ew", pady=2)

    find_replace_button = Button(edit_menu_frame, text="Find and Replace", command=find_and_replace)
    find_replace_button.grid(row=5, column=0, sticky="ew", pady=2)

    return edit_menu
