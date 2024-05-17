# app/text_handlers/resize_window.py

from tkinter import scrolledtext


def create_text_area(window, text_change):
    txt = scrolledtext.ScrolledText(window, height=999)
    txt.grid(row=1, sticky="nsew")

    txt.bind('<KeyPress>', text_change)

    return txt  # Возвращаем созданный объект txt
