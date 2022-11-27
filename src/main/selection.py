import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import *
from tkinter import ttk
import time
import json
def driveSelection():
    root = tk.Tk()
    root.iconify()
    while True:
        drive=fd.askdirectory()
        if drive=="":
            tk.messagebox.showerror(title="Invalid Backup Location", message="You have not selected a backup location. Please select an appropriate backup location.")
        else:
            answer = askyesno(title='Confirm Backup Location',message='Are you sure that you want to save your backup at ' + drive + '?')
            if answer==True:
                root.destroy()
                break
            else:
                continue