
# Image Editor

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import os
import numpy as np
import random

#created main window
window = Tk()
window.geometry("1000x700")
window.title("Image Editor")

# defined variable
global count, emig
# global bright, con
# global frp, tname  # list of paths
frp = []
tname = []
con = 1
bright = 0
panelB = None
panelA = None

# function defined to get the path of the image selected
def getpath(path):
    a = path.split(r'/')
    # print(a)
    fname = a[-1]
    l = len(fname)
    location = path[:-l]
    return location

# function defined to get the folder name from which image is selected
def getfoldername(path):
    a = path.split(r'/')
    # print(a)
    name = a[-1]
    return name

# function defined to get the file name of image is selected
def getfilename(path):
    a = path.split(r'/')
    fname = a[-1]
    a = fname.split('.')
    a = a[0]
    return a

# function defined to open the image file
def openfilename():
    filename = filedialog.askopenfilename(title='"pen')
    return filename

# function defined to open the selected image
def open_img():
    global x, panelA, panelB
    global count, eimg, location, filename
    count = 0
    x = openfilename()
    img = Image.open(x)
    eimg = img
    img = ImageTk.PhotoImage(img)
    temp = x
    location = getpath(temp)
    filename = getfilename(temp)
    if panelA is None or panelB is None:
        panelA = Label(image=img)
        panelA.image = img
        panelA.pack(side="left", padx=10, pady=10)
        panelB = Label(image=img)
        panelB.image = img
        panelB.pack(side="right", padx=10, pady=10)
    else:
        panelA.configure(image=img)
        panelB.configure(image=img)
        panelA.image = img
        panelB.image = img

# function defined for make the sketch of image selected
def sketch_convert():
    image = cv2.imread(x)
    global count, eimg
    count = 1
    # if image is None:
    #     print("can not find image")
    #     sys.exit()
    # gray scale
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # invert gray image
    grayImageInv = 255 - grayImage
    # gaussian blur
    grayImageInv = cv2.GaussianBlur(grayImageInv, (21, 21), 0)
    # blend using color dodge
    output = cv2.divide(grayImage, 255 - grayImageInv, scale=256.0)
    # edge
    gray = cv2.medianBlur(grayImage, 1)
    edges = cv2.adaptiveThreshold(gray, 10, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(output, 6, 60, 200)
    global o1
    o1 = cv2.bitwise_and(color, color, mask=edges)
    image = Image.fromarray(o1)
    eimg = image
    image = ImageTk.PhotoImage(image)
    panelB.configure(image=image)
    panelB.image = image
    mbox.showinfo("Success", "Image converted to Sketch format!")

# function defined to make the image sharp
def sharpen_convert():
    image = cv2.imread(x)[:, :, ::-1]
    global count, eimg
    count = 2
    # if image is None:
    #     print("can not find image")
    #     sys.exit()
    k2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    global o2
    o2 = cv2.filter2D(image, -1, k2)
    image = Image.fromarray(o2)
    eimg = image
    image = ImageTk.PhotoImage(image)
    panelB.configure(image=image)
    panelB.image = image
    mbox.showinfo("Success", "Image made more sharpen!")


# function defined to convert the image into cartoon type image
def cartoon_convert():
    image = cv2.imread(x)[:, :, ::-1]
    global count, eimg
    count = 4
    # if image is None:
    #     print("can not find image")
    #     exit()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray = cv2.GaussianBlur(image_gray, (3, 3), 0)
    image_edge = cv2.Laplacian(image_gray, -1, ksize=5)
    image_edge = 255 - image_edge
    ret, image_edge = cv2.threshold(image_edge, 150, 255, cv2.THRESH_BINARY)
    edgePreservingImage = cv2.edgePreservingFilter(image, flags=2, sigma_s=50, sigma_r=0.4)
    global o4
    output = np.zeros(image_gray.shape)
    output = cv2.bitwise_and(edgePreservingImage, edgePreservingImage, mask=image_edge)
    o4 = cv2.convertScaleAbs(output, alpha=1, beta=60)
    image = Image.fromarray(o4)
    eimg = image
    image = ImageTk.PhotoImage(image)
    panelB.configure(image=image)
    panelB.image = image
    mbox.showinfo("Success", "Image converted to Cartoon format!")


# def conto():
#     img = cv2.imread(x)[:, :, ::-1]
#     global count, eimg
#     count = 3
#     image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # check if image exists
#     if image is None:
#         print("can not find image")
#         sys.exit()
#     # apply canny to the input image
#     canny = cv2.Canny(image, 50, 150, apertureSize=3)
#     # find contours
#     contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     # output image to draw contours on
#     output = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
#     # draw contours
#     for i in range(0, len(contours)):
#         cv2.drawContours(output, contours, i, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
#                          2)
#     global o3
#     o3 = output
#     image = Image.fromarray(o3)
#     eimg = image
#     image = ImageTk.PhotoImage(image)
#     panelB.configure(image=image)
#     panelB.image = image


def kelvin_convert():
    image = cv2.imread(x)[:, :, ::-1]
    global count, eimg
    count = 5
    result = np.copy(image)

    original_Val = np.array([0, 50, 100, 150, 200, 255])
    red_Val = np.array([0, 20, 40, 75, 150, 255])
    blue_Val = np.array([0, 80, 150, 190, 220, 255])
    all_Val = np.arange(0, 256)
    redLookupTable = np.interp(all_Val, original_Val, red_Val)

    blueLookupTable = np.interp(all_Val, original_Val, blue_Val)

    B, G, R = cv2.split(result)
    R = cv2.LUT(R, redLookupTable)
    R = np.uint8(R)
    B = cv2.LUT(B, blueLookupTable)
    B = np.uint8(B)

    result = cv2.merge([B, G, R])
    global o5
    o5 = result
    image = Image.fromarray(o5)
    eimg = image
    image = ImageTk.PhotoImage(image)
    panelB.configure(image=image)
    panelB.image = image
    mbox.showinfo("Success", "Image converted to Kelvin format!")


# function defined to reset the edited image to original one
def reset():
    image = cv2.imread(x)[:, :, ::-1]
    global count, eimg
    count = 6
    global o6
    o6 = image
    image = Image.fromarray(o6)
    eimg = image
    image = ImageTk.PhotoImage(image)
    panelB.configure(image=image)
    panelB.image = image
    mbox.showinfo("Success", "Image reset to original format!")

# function defined to same the edited image
def save_img():
    global location, filename, eimg
    # eimg.save(location + filename + r"_edit.png")
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    eimg.save(filename)
    mbox.showinfo("Success", "Edited Image Saved Successfully!")



# top label
start1 = tk.Label(text = "Image  Editor", font=("Arial", 40), fg="magenta",underline=0) # same way bg
start1.place(x = 350, y = 10)

# original image label
start1 = tk.Label(text = "Original\nImage", font=("Arial", 40), fg="magenta") # same way bg
start1.place(x = 100, y = 270)

# edited image label
start1 = tk.Label(text = "Edited\nImage", font=("Arial", 40), fg="magenta") # same way bg
start1.place(x = 700, y = 270)

# choose button created
chooseb = Button(window, text="Choose",command=open_img,font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
chooseb.place(x =30 , y =20 )

# save button created
saveb = Button(window, text="Save",command=save_img,font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
saveb.place(x =170 , y =20 )

# skecth button created
sketchb = Button(window, text="Sketch",command=sketch_convert,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
sketchb.place(x =80 , y =620 )

# sharpen button created
sharpb = Button(window, text="Sharpen",command=sharpen_convert,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
sharpb.place(x =250 , y =620 )

# cartoon button created
cartoonb = Button(window, text="Cartoon",command=cartoon_convert,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
cartoonb.place(x =440 , y =620 )

# kelvin button created
kelvinb = Button(window, text="kelvin",command=kelvin_convert,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
kelvinb.place(x =630 , y =620 )

# reset button created
resetb = Button(window, text="Reset",command=reset,font=("Arial", 20), bg = "yellow", fg = "blue", borderwidth=3, relief="raised")
resetb.place(x =800 , y =620 )

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =880 , y =20 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()