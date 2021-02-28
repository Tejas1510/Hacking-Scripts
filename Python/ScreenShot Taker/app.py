import pyautogui
import keyboard
from tkinter import filedialog


while True:
    try:
        if keyboard.is_pressed('p'):
            screenshots = pyautogui.screenshot()
            file_path = filedialog.asksaveasfilename(defaultextension='.png')
            screenshots.save(file_path)
            break
        else:
            pass
    except:
        break
