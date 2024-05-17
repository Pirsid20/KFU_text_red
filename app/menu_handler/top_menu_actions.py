# app/menu_handler/top_menu_actions.py
from tkinter import filedialog, END, INSERT

from app.settings import *


# функция обработчик действий с файлами
def file_dropdown_handler(action, txt):
    """Обработчик выпадающих списков файлов"""
    global currentFilePath

    if action == "open":
        file = filedialog.askopenfilename(filetypes=fileTypes)
        if file:  # Проверяем, что файл был выбран
            window.title(appName + " - " + file)
            currentFilePath = file

            with open(file, 'r') as f:
                txt.delete(1.0, END)
                txt.insert(INSERT, f.read())

    elif action == "new":
        currentFilePath = nofileOpenedString
        txt.delete(1.0, END)
        window.title(appName + " - " + currentFilePath)

    elif action == "save" or action == "saveAs":
        if currentFilePath == nofileOpenedString or action == 'saveAs':
            currentFilePath = filedialog.asksaveasfilename(filetypes=fileTypes)
        if currentFilePath:  # Проверяем, что был указан путь для сохранения файла
            with open(currentFilePath, 'w') as f:
                f.write(txt.get('1.0', 'end'))
            window.title(appName + " - " + currentFilePath)