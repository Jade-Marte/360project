import tkinter as tk
from tkinter import Message, filedialog


def fileDialog():
    filetypes = (
        ('csv files','*.csv'),
        ('exel files','*.xlsx')
    )
    filename = filedialog.askopenfile(
        title = "Import",
        initialdir='/',
        filetypes=filetypes)
    showinfo(
        title='Selected File',
        message=filename
    )

