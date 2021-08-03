
# Video Stitching

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
from moviepy.editor import *


# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Video Stitching") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "VIDEO  STITCHING", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 170, y = 10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =180 , y =600 )

# image on the main window
path = "Images/vid_stitch.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 130, y = 120)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =700 , y =600 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Video Stitching") # title given is "DICTIONARY"
window1.geometry('1000x700')

path_list = []
clip_list = []


def open_file():
    global path_list
    filename = filedialog.askopenfilenames(title="Select file")
    # print(filename)
    path_text.delete("1.0", "end")
    path_text.insert(END, filename)

def row_fun():
    input_txt = str(path_text.get("1.0", "end-1c"))
    path_list = input_txt.rstrip().split(' ')


    for i in range(0,len(path_list)):
        clip_list.append(VideoFileClip(path_list[i]))
    final_clip = clips_array([clip_list])
    final_clip.write_videofile('row_stitch.mp4')


def col_fun():
    input_txt = str(path_text.get("1.0", "end-1c"))
    path_list = input_txt.rstrip().split(' ')

    for i in range(0,len(path_list)):
        clip_list.append(VideoFileClip(path_list[i]))

    if(len(path_list)==2):
        final_clip = clips_array([[clip_list[0]], [clip_list[1]]])
        final_clip.write_videofile('col_stitch.mp4')
    elif(len(path_list)==3):
        final_clip = clips_array([[clip_list[0]],[clip_list[1]], [clip_list[2]]])
        final_clip.write_videofile('col_stitch.mp4')



# top label
start1 = tk.Label(text = "VIDEO  STITCHING", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 180, y = 10)

lbl1 = tk.Label(text="Select the videos\nyou want to stitch & proceed...", font=("Arial", 40),fg="green")  # same way bg
lbl1.place(x=130, y=100)

lbl2 = tk.Label(text="Selected Videos", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=260)

path_text = tk.Text(window1, height=10, width=73, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
path_text.place(x=80, y = 310)

# Select Button
selectb=Button(window1, text="SELECT",command=open_file,  font=("Arial", 20), bg = "light green", fg = "blue")
selectb.place(x = 80, y = 600)

# Stitch in row Button
stitch_rowb=Button(window1, text="STITCH IN ROWS",command=row_fun,  font=("Arial", 20), bg = "orange", fg = "blue")
stitch_rowb.place(x = 265, y = 600)

# Stitch in column Button
stitch_rowb=Button(window1, text="STITCH IN COLUMNS",command=col_fun,  font=("Arial", 20), bg = "yellow", fg = "blue")
stitch_rowb.place(x = 585, y = 600)

def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()
window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()
