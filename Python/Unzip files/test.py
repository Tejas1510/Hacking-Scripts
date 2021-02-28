import os
import zipfile
from tkinter import filedialog
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
from tkinter import filedialog

filenames = filedialog.askopenfilename(initialdir="/",
                                       title="Select file",
                                       filetypes=(("*.jpeg", "*.jpg"),
                                                  ("all files", "*.*")))
for filename in os.listdir("."):
    filename = filenames
    if filename.endswith(".zip"):
        print(filename)
        name = os.path.splitext(os.path.basename(filename))[0]
        if not os.path.isdir(name):
            try:
                zip = zipfile.ZipFile(filename)
                os.mkdir(name)
                zip.extractall(path=name)
            except zipfile.BadZipfile as e:
                print("BAD ZIP: " + filename)
                try:
                    os.remove(filename)
                except OSError as e:
                    if e.errno != errno.ENOENT:
                        raise
