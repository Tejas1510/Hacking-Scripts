from moviepy.editor import *
from tkinter import *
import moviepy.video.tools.drawing as dw


filepath = "FROZEN Full UK Trailer Official Disney UK.mp4"


def printtext():
    global e, e1
    global string, string1
    string = e.get()
    print(string)
    string1 = e1.get()


def Freezing_a_region():
    Freezing_a_region = (VideoFileClip(filepath)
                         .subclip((string), (string1))
                         .speedx(0.5)
                         .resize(.4))
    snapshot = (Freezing_a_region
                .crop(x2=Freezing_a_region.w/2)
                .to_ImageClip(0.2)
                .set_duration(Freezing_a_region.duration))
    composition = CompositeVideoClip([Freezing_a_region, snapshot])
    composition.write_gif('Freezing_a_region.gif', fps=15)


def Cropping_the_image():
    Cropping_the_image = (VideoFileClip(filepath)
                          .subclip(string, string1)
                          .resize(0.5)
                          .crop(x1=145, x2=400))
    Cropping_the_image.write_gif("Cropping the image.gif")


def gif_loop():
    castle = (VideoFileClip(filepath, audio=False)
              .subclip(string, string1)
              .speedx(0.2)
              .resize(.4))
    d = castle.duration
    castle = castle.crossfadein(d/2)
    composition = (CompositeVideoClip([castle,
                                       castle.set_start(d/2),
                                       castle.set_start(d)])
                   .subclip(d/2, 3*d/2))
    composition.write_gif('castle.gif', fps=5, fuzz=5)


root = Tk()

root.title('Name')

e = Entry(root)
e.pack()
e.focus_set()


e1 = Entry(root)
e1.pack()
e1.focus_set()

b = Button(root, text='okay', command=printtext)
b.pack(side='bottom')
b1 = Button(root, text='Freezing_a_region', command=Freezing_a_region)
b1.pack(side='bottom')
b2 = Button(root, text='Cropping_the_image', command=Cropping_the_image)
b2.pack(side='bottom')
b3 = Button(root, text='gif_loop', command=gif_loop)
b3.pack(side='bottom')
root.mainloop()

print(string1)
