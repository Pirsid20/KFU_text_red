# app/settings.py
from tkinter import Tk


appName = 'Simple Text Editor'
nofileOpenedString = 'New File'
currentFilePath = nofileOpenedString
fileTypes = [("Text Files", "*.txt"), ("Markdown", "*.md")]

window = Tk()
window.title(appName + " - " + currentFilePath)
window.geometry('500x400')
window.grid_columnconfigure(0, weight=1)


