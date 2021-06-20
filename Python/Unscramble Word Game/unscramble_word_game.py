
# Unscramble Word Game

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import random
from random import shuffle
import pandas as pd
from PIL import Image, ImageTk

data = pd.read_csv('big_words.csv')
answers = data['Word'].tolist()

correct_cnt = 0
wrong_cnt = 0
skip_cnt = 0

questions = []

for i in answers:
    words = list(i)
    shuffle(words)
    questions.append(words)

num = random.randint(0, len(questions)-1)

firstclick1 = True
def on_e1_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick1

    if firstclick1: # if this is the first time they clicked it
        firstclick1 = False
        e1.delete(0, "end") # delete all the text in the entry

def see_result():
    mbox.showinfo("See Your Status", "Correct Answer: "+str(correct_cnt) + "\nWrong Answer : "+str(wrong_cnt) + "\nSkipped Answer : " + str(skip_cnt))

def initial():
    global questions, num
    lb1.configure(text=questions[num])

cnt = 20
def next_switch():
    global cnt, skip_cnt
    cnt = cnt - 1
    if(cnt>=0):
        lives_cnt1 = tk.Label(text="       ", font=("Arial", 30), fg="brown")
        lives_cnt1.place(x=880, y=70)
        lives_cnt = tk.Label(text=cnt, font=("Arial", 30), fg="brown")  # same way bg
        lives_cnt.place(x=890, y=70)

    if(cnt==-1):
        mbox.showinfo("GAME OVER", "GAME OVER !")

        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file="Images/score.gif")
        c1.create_image(400, 10, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        score1 = Label(f1, text=str(correct_cnt) + "/20", font=("Arial", 100), fg="green", bg="white")
        score1.place(x=350, y=200)

        c2 = Canvas(f1, width=500, height=300, bg="white")  # blue
        c2.place(x=250, y=350)
        p2 = PhotoImage(file="Images/scoreboard.gif")
        c2.create_image(0, 0, image=p2, anchor="nw")
        w2 = Canvas(window)
        w2.p2 = p2

        score1 = Label(f1, text="Correct :" + str(correct_cnt) + "/20", font=("Arial", 30), fg="brown", bg="gray")
        score1.place(x=350, y=380)
        score1 = Label(f1, text="Wrong :" + str(wrong_cnt) + "/20", font=("Arial", 30), fg="brown", bg="gray")
        score1.place(x=350, y=480)
        score1 = Label(f1, text="Skipped :" + str(skip_cnt) + "/20", font=("Arial", 30), fg="brown", bg="gray")
        score1.place(x=350, y=580)

    global questions, answers, num
    num = random.randint(0, len(questions)-1)
    lb1.configure(text=questions[num])
    e1.delete(0,END)
    # e1.insert(0, 'Enter your correct word here...')

def skip_switch():
    global cnt, skip_cnt
    cnt = cnt - 1
    if(cnt>=0):
        lives_cnt1 = tk.Label(text="       ", font=("Arial", 30), fg="brown")
        lives_cnt1.place(x=880, y=70)
        lives_cnt = tk.Label(text=cnt, font=("Arial", 30), fg="brown")  # same way bg
        lives_cnt.place(x=890, y=70)

    if (cnt == -1):
        mbox.showinfo("GAME OVER", "GAME OVER !")

        f1 = Frame(window, width=1000, height=700)
        f1.propagate(0)
        f1.pack(side='top')

        c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
        c1.pack()
        p1 = PhotoImage(file="Images/score.gif")
        c1.create_image(400, 10, image=p1, anchor="nw")
        w1 = Canvas(window)
        w1.p1 = p1

        score1 = Label(f1, text=str(correct_cnt) + "/20", font=("Arial", 100), fg="green", bg = "white")
        score1.place(x=350, y=200)

        c2 = Canvas(f1, width=500, height=300, bg="white")  # blue
        c2.place(x = 250,y = 350)
        p2 = PhotoImage(file="Images/scoreboard.gif")
        c2.create_image(0, 0, image=p2, anchor="nw")
        w2 = Canvas(window)
        w2.p2 = p2

        score1 = Label(f1, text="Correct :" + str(correct_cnt) + "/20", font=("Arial", 30), fg="brown", bg = "gray")
        score1.place(x=350, y=380)
        score1 = Label(f1, text="Wrong :" + str(wrong_cnt) + "/20", font=("Arial", 30), fg="brown", bg = "gray")
        score1.place(x=350, y=480)
        score1 = Label(f1, text="Skipped :" + str(skip_cnt) + "/20", font=("Arial", 30), fg="brown", bg = "gray")
        score1.place(x=350, y=580)

    global questions, answers, num
    num = random.randint(0, len(questions) - 1)
    lb1.configure(text=questions[num])
    skip_cnt = skip_cnt + 1
    e1.delete(0, END)
    # e1.insert(0, 'Enter your correct word here...')

def answercheck():
    global questions, num, answers, correct_cnt, wrong_cnt
    userinput = e1.get()

    if(userinput=="" or userinput=="Enter your correct word here..."):
        mbox.showerror("Error", "You haven't entered any word.")
    else:
        if userinput == answers[num]:
            mbox.showinfo('Success','Your answer is correct')
            correct_cnt = correct_cnt + 1
            next_switch()
            # e1.delete(0, END)
            # e1.insert(0, 'Enter your word here...')
        else:
            wrong_cnt  = wrong_cnt + 1
            mbox.showerror('Error','Your answer is wrong')
            next_switch()
            # e1.delete(0,END)


window = Tk()
window.geometry("1000x700")
window.title("Unscramble the Word")
# window.iconbitmap(r"icon.ico")

# image on the main window
path = "Images/unscramble.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img, anchor = "nw")
# The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "top", fill = "both", expand = "no")
panel.place(x = 180, y = 80)

start1 = tk.Label(text = "Unscramble the Word", font=("Arial", 40), fg="magenta",underline=0) # same way bg
start1.place(x = 250, y = 10)

lives = tk.Label(text = "LIVES", font=("Arial", 30), fg="brown") # same way bg
lives.place(x = 850, y = 20)

lives_cnt = tk.Label(text = 20, font=("Arial", 30), fg="brown") # same way bg
lives_cnt.place(x = 880, y = 70)

lb1 = Label(window, font=("Arial", 30), fg="brown",bg = "light yellow")
lb1.place(x=300, y = 200)

e1 = Entry(window,font=("Arial", 30) , width=25, border=2)
e1.insert(0, 'Enter your correct word here...')
e1.bind('<FocusIn>', on_e1_click)
e1.place(x = 220, y = 400)

checkb = Button(window, text="CHECK",command=answercheck,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
checkb.place(x =250 , y =500 )

def clear_label():
    e1.delete(0, "end")

clearb = Button(window, text="CLEAR",command=clear_label,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
clearb.place(x =450 , y =500 )

skipb = Button(window, text="SKIP",command=skip_switch,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
skipb.place(x =650 , y =500 )

statusb = Button(window, text="SEE STATUS",command=see_result,font=("Arial", 20), bg = "light blue", fg = "blue", borderwidth=3, relief="raised")
statusb.place(x =300 , y =600 )

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =580 , y =600 )

initial()

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()