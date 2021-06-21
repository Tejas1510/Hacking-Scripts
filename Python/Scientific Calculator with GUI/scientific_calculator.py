from tkinter import *
import tkinter.messagebox
import math

# on button press
root = Tk()
root.geometry("650x400+300+300")
root.title("Scientific Calculator")

switch = None

# Numbers


def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


# Operations

def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)


def btnp_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')


def btnm_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')


def btnml_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')


def btnd_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')


def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')


def sin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


def cos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


def tan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


def arcsin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.asin(ans))
        else:
            ans = math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


def arccos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.acos(ans))
        else:
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


def arctan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.atan(ans))
        else:
            ans = math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


def pow_clicked():
    pos = len(disp.get())
    disp.insert(pos, '**')


def round_clicked():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


def logarithm_clicked():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


def fact_clicked():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


def sqr_clicked():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')


def pi_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


def e_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))


def bl_clicked():
    pos = len(disp.get())
    disp.insert(pos, '(')


def br_clicked():
    pos = len(disp.get())
    disp.insert(pos, ')')


def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def conv_clicked():
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "Deg"
    else:
        switch = None
        conv_btn['text'] = "Rad"


def ln_clicked():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')


def btneq_clicked(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror(
            "Value Error", "Check your values and operators")


# Labels

data = StringVar()

disp = Entry(root, font="Verdana 20", fg="black", bg="#abbab1",
             bd=0, justify=RIGHT, insertbackground="#abbab1", cursor="arrow")
disp.bind("<Return>", btneq_clicked)
disp.bind("<Escape>", btnc_clicked)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)


# Row 1 Buttons

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

pi_btn = Button(btnrow1, text="π", font="Segoe 18", relief=GROOVE,
                bd=0, command=pi_clicked, fg="white", bg="#333333")
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

fact_btn = Button(btnrow1, text=" x! ", font="Segoe 18", relief=GROOVE,
                  bd=0, command=fact_clicked, fg="white", bg="#333333")
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sin_btn = Button(btnrow1, text="sin", font="Segoe 18", relief=GROOVE,
                 bd=0, command=sin_clicked, fg="white", bg="#333333")
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_btn = Button(btnrow1, text="cos", font="Segoe 18", relief=GROOVE,
                 bd=0, command=cos_clicked, fg="white", bg="#333333")
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_btn = Button(btnrow1, text="tan", font="Segoe 18", relief=GROOVE,
                 bd=0, command=tan_clicked, fg="white", bg="#333333")
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Segoe 23", relief=GROOVE,
              bd=0, command=btn1_clicked, fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Segoe 23", relief=GROOVE,
              bd=0,  command=btn2_clicked, fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Segoe 23", relief=GROOVE,
              bd=0, command=btn3_clicked, fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnp = Button(btnrow1, text="+", font="Segoe 23", relief=GROOVE,
              bd=0, command=btnp_clicked, fg="white", bg="#333333")
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Row 2 Buttons

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

e_btn = Button(btnrow2, text="e", font="Segoe 18", relief=GROOVE,
               bd=0, command=e_clicked, fg="white", bg="#333333")
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqr_btn = Button(btnrow2, text=" √x ", font="Segoe 18", relief=GROOVE,
                 bd=0, command=sqr_clicked, fg="white", bg="#333333")
sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sinh_btn = Button(btnrow2, text="sin−1", font="Segoe 11 bold",
                  relief=GROOVE, bd=0, command=arcsin_clicked, fg="white", bg="#333333")
sinh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cosh_btn = Button(btnrow2, text="cos-1", font="Segoe 11 bold",
                  relief=GROOVE, bd=0, command=arccos_clicked, fg="white", bg="#333333")
cosh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tanh_btn = Button(btnrow2, text="tan-1", font="Segoe 11 bold",
                  relief=GROOVE, bd=0, command=arctan_clicked, fg="white", bg="#333333")
tanh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow2, text="4", font="Segoe 23", relief=GROOVE,
              bd=0, command=btn4_clicked, fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Segoe 23", relief=GROOVE,
              bd=0, command=btn5_clicked, fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow2, text="6", font="Segoe 23", relief=GROOVE,
              bd=0, command=btn6_clicked, fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(btnrow2, text="-", font="Segoe 23", relief=GROOVE,
              bd=0, command=btnm_clicked, fg="white", bg="#333333")
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Row 3 Buttons

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

conv_btn = Button(btnrow3, text="Rad", font="Segoe 12 bold",
                  relief=GROOVE, bd=0, command=conv_clicked, fg="white", bg="#333333")
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

round_btn = Button(btnrow3, text="round", font="Segoe 10 bold",
                   relief=GROOVE, bd=0, command=round_clicked, fg="white", bg="#333333")
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(btnrow3, text="ln", font="Segoe 18", relief=GROOVE,
                bd=0, command=ln_clicked, fg="white", bg="#333333")
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logarithm_btn = Button(btnrow3, text="log", font="Segoe 17", relief=GROOVE,
                       bd=0, command=logarithm_clicked, fg="white", bg="#333333")
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

pow_btn = Button(btnrow3, text="x^y", font="Segoe 17", relief=GROOVE,
                 bd=0, command=pow_clicked, fg="white", bg="#333333")
pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7 = Button(btnrow3, text="7", font="Segoe 23", relief=GROOVE,
              bd=0, command=btn7_clicked, fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Segoe 23", relief=GROOVE,
              bd=0, command=btn8_clicked, fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Segoe 23", relief=GROOVE,
              bd=0, command=btn9_clicked, fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow3, text="*", font="Segoe 23", relief=GROOVE,
               bd=0, command=btnml_clicked, fg="white", bg="#333333")
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Row 4 Buttons

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

mod_btn = Button(btnrow4, text="%", font="Segoe 21", relief=GROOVE,
                 bd=0, command=mod_clicked, fg="white", bg="#333333")
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

bl_btn = Button(btnrow4, text=" ( ", font="Segoe 21", relief=GROOVE,
                bd=0, command=bl_clicked, fg="white", bg="#333333")
bl_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(btnrow4, text=" ) ", font="Segoe 21", relief=GROOVE,
                bd=0, command=br_clicked, fg="white", bg="#333333")
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=" • ", font="Segoe 21", relief=GROOVE,
                 bd=0, command=dot_clicked, fg="white", bg="#333333")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(btnrow4, text="C", font="Segoe 23", relief=GROOVE,
              bd=0, command=btnc_clicked, fg="white", bg="#333333")
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="⌫", font="Segoe 20", relief=GROOVE,
                 bd=0, command=del_clicked, fg="white", bg="#333333")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Segoe 23", relief=GROOVE,
              bd=0, command=btn0_clicked, fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow4, text="=", font="Segoe 23", relief=GROOVE,
               bd=0, command=btneq_clicked, fg="white", bg="#333333")
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Segoe 23", relief=GROOVE,
              bd=0, command=btnd_clicked, fg="white", bg="#333333")
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)


root.mainloop()
