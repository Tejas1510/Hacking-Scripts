#POMODORO CLOCK GUI IN PYTHON

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time

#colours
GREEN = '#17B169'
LIGHT_GREEN = '#98FB98'

#!----------FUNCTIONAL CODE STARTS----------!

#global variable to store time
temp = 0

#----------function for countdown timer----------
def timer_start():
    global temp
    #taking session duration as input
    try:
        #temp variable to store the duration of session
        temp = int(min.get())*60+int(sec.get())
    except:
        messagebox.showinfo('Message', 'Enter session duration')

    #start the session
    time_label.config(text = "Keep going! You got this! 🤩", bg = LIGHT_GREEN)
    while(temp > -1):
        mins,secs = divmod(temp,60)

        min.set("{0:2d}".format(mins))
        sec.set("{0:2d}".format(secs))

        clk.update()
        time.sleep(1)

        #if session duration is over
        if(temp==0):
            time_label.config(text = "Enter the time in min:sec format", bg = LIGHT_GREEN)

        #countdown the time
        temp -= 1



#----------function to reset timer----------
def timer_reset():
    global temp
    temp = 0
    min.set("00")
    sec.set("00")
    time_label.config(text = "Enter the time in min:sec format", bg = LIGHT_GREEN)



#----------function to exit the application----------
def quit_app():
    root.destroy()


#!----------FUNCTIONAL CODE ENDS----------!


#!----------GUI CODE STARTS----------!

#initial window
root = Tk()
#title of the window
root.title('PomoFocus')
#disabling resizing of window
root.resizable(0, 0)
root['bg'] = GREEN

#---creating frames and canvas---

#title frame
top = Frame(root, bd=8, relief="raised", bg = LIGHT_GREEN, width = 600, height = 200)
top.grid(row = 0, column = 0, padx = 10, pady = 5)

#label frame
lbl = Frame(root, bd=8, relief="flat", bg = GREEN, width = 600, height = 400)
lbl.grid(row = 1, column = 0, padx = 10)

#clock frame
clk = Frame(root, bd=8, relief="flat", bg = GREEN, width = 600, height = 400)
clk.grid(row = 2, column = 0, padx = 20)


#buttons frame
btn = Frame(root, bd=5, relief="raised", bg = GREEN, width = 1000, height = 400)
btn.grid(row = 3, column = 0, padx = 10, pady = 5, ipady = 5)


#---adding labels and buttons---

#in the top frame
#top label
name = Label(top, text = "PomoFocus", bg = LIGHT_GREEN, width = 30, font = ("Courier New", 20, "bold underline"))
name.grid(row = 0, column = 1, padx = 3, pady = 3)

#in the lbl frame
time_label = Label(lbl, text = "Enter the time in min:sec format", bg = LIGHT_GREEN, width = 35, height = 2, font = ("Courier New", 15, "bold"))
time_label.grid(row = 0, column = 1, padx = 15)

#in the clk frame
#variables for session time period
min = StringVar()
sec = StringVar()

#initial values
min.set("00")
sec.set("00")

#row 1 - for selecting duration of session
min_entry = Entry(clk, textvariable = min, bg = LIGHT_GREEN, width = 5, font = ("Courier New", 45))
min_entry.grid(row = 1, column = 1, padx = 10)

sec_entry = Entry(clk, textvariable = sec, width = 5, bg = LIGHT_GREEN, font = ("Courier New", 45))
sec_entry.grid(row = 1, column = 2, padx = 10)


#in the btn frame
#row 1 - start, reset buttons
strt = Button(btn, text = "Start", bg = LIGHT_GREEN, width = 8, height = 2, font = ("Courier New", 15, "italic bold"), command = timer_start)
strt.grid(row = 1, column = 1, padx = 35)

reset = Button(btn, text = "Reset", bg = LIGHT_GREEN, width = 8, height = 2, font = ("Courier New", 15, "italic bold"), command = timer_reset)
reset.grid(row = 1, column = 3, padx = 35)


#row 2 - quit button
quit = Button(btn, text = "Quit", bg = LIGHT_GREEN, width = 8, height = 2, font = ("Courier New", 15, "italic bold"), command = quit_app)
quit.grid(row = 2, column = 2, padx = 10)


#!--------GUI CODE ENDS----------!

if __name__ == '__main__':
    root.mainloop()
