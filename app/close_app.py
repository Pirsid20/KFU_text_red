# app/close_app.py
from tkinter import messagebox


def on_closing(window, txt, file_dropdown_handler):
    """Обработка закрытия окна"""
    global currentFilePath

    text_content = txt.get('1.0', 'end-1c')  # Получаем текст из текстового поля

    # Проверяем, были ли внесены изменения в текст
    if text_content.strip() != "":
        save_confirmation = messagebox.askyesnocancel("Предупреждение", "Сохранить изменения перед закрытием?")
        if save_confirmation:  # Пользователь хочет сохранить изменения
            file_dropdown_handler("save", txt)
        elif save_confirmation is None:  # Пользователь отменил действие
            return

    # Закрываем окно
    window.destroy()



