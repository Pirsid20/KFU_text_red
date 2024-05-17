# main.py
import subprocess
from tkinter import *
from tkinter import filedialog, messagebox

from app.close_app import on_closing
from app.menu_handler.right_menu import create_right_menu
from app.settings import *
from app.menu_handler.top_menu import create_top_menu
from app.text_handlers.resize_window import create_text_area

import ctypes


# Увеличьте количество Точек на дюйм, чтобы изображение выглядело четче.
ctypes.windll.shcore.SetProcessDpiAwareness(True)


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

    elif action == "print":
        """Печать файла"""
        if currentFilePath == nofileOpenedString:
            messagebox.showinfo("Внимание", "Файл не сохранен. Пожалуйста, сохраните файл перед печатью.")
            return

        try:
            subprocess.run(['notepad.exe', '/p', currentFilePath], check=True)
        except subprocess.CalledProcessError:
            messagebox.showerror("Ошибка", "Ошибка при печати файла.")
        except FileNotFoundError:
            messagebox.showerror("Ошибка",
                                 "Не удалось найти программу для печати файла. Проверьте, что Notepad доступен.")

    elif action == "close":
        """Сохранение текущего файла и закрытие"""

        text_content = txt.get('1.0', 'end-1c')  # Получаем текст из текстового поля

        # Проверяем, были ли внесены изменения в текст
        if text_content.strip() != "":
            save_confirmation = messagebox.askyesnocancel("Предупреждение", "Сохранить изменения перед закрытием?")
            if save_confirmation:  # Пользователь хочет сохранить изменения
                file_dropdown_handler("save", txt)
            elif save_confirmation is None:  # Пользователь отменил действие
                return
        else:
            save_confirmation = True  # Нет изменений, не требуется подтверждение сохранения

        currentFilePath = nofileOpenedString
        txt.delete(1.0, END)
        window.title(appName + " - " + currentFilePath)


def text_change(event):
    """Функции редактирования текста"""
    window.title(appName + " - *" + currentFilePath)


# Создаем область текста
txt = create_text_area(window, text_change)

# боковое меню

right_menu = create_right_menu(window, txt)

# Создаем меню
create_top_menu(window, file_dropdown_handler, txt)

# Привязываем функцию on_closing к событию закрытия окна
window.protocol("WM_DELETE_WINDOW", lambda: on_closing(window, txt, file_dropdown_handler))

# Main Loop
if __name__ == "__main__":
    window.mainloop()
