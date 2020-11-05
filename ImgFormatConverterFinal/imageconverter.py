import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 250, bg = 'azure3', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getIMG ():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

browseButton_PNG = tk.Button(text="      Import PNG File     ", command=getIMG, bg='deeppink', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_PNG)

def convertToJPG ():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)

saveAsButton_JPG = tk.Button(text='Convert IMG to JPG', command=convertToJPG, bg='deeppink', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_JPG)

root.mainloop()
