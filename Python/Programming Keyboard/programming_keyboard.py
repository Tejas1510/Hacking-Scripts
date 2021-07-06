from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox
import tkinter as tk

# created a main window
root = Tk()
root.title("Programming Keyboard")
root.geometry('1000x750')

# class Keypad created for creating keyboard
class Keypad(tk.Frame):

    cells = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0','!', '#', '%', '&', '*','+','-','%', '/', '\'', '.', ',', ':','"',"(",")"],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.target = None
        self.memory = ''

        for y, row in enumerate(self.cells):
            for x, item in enumerate(row):
                b = tk.Button(self, text=item, command=lambda text=item:self.append(text),font=("Arial", 14), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
                b.grid(row=y, column=x, sticky='news')

        # ----------
        x = tk.Button(self, text='False', command=self.Falseb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=0, columnspan='2', sticky='news')

        x = tk.Button(self, text='class', command=self.classb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=2, columnspan='2', sticky='news')

        x = tk.Button(self, text='from', command=self.fromb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=4, columnspan='2', sticky='news')

        x = tk.Button(self, text='or', command=self.orb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=6, columnspan='2', sticky='news')

        x = tk.Button(self, text='None', command=self.Noneb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=8, columnspan='2', sticky='news')

        x = tk.Button(self, text='continue', command=self.continueb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=10, columnspan='2', sticky='news')

        x = tk.Button(self, text='global', command=self.globalb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=12, columnspan='2', sticky='news')

        x = tk.Button(self, text='paas', command=self.passb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=14, columnspan='2', sticky='news')

        x = tk.Button(self, text='True', command=self.Trueb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=16, columnspan='2', sticky='news')

        x = tk.Button(self, text='def', command=self.defb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=18, columnspan='2', sticky='news')

        x = tk.Button(self, text='if', command=self.ifb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=20, columnspan='2', sticky='news')

        x = tk.Button(self, text='raise', command=self.raiseb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=22, columnspan='2', sticky='news')

        x = tk.Button(self, text='and', command=self.andb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=3, column=24, columnspan='2', sticky='news')

        x = tk.Button(self, text='del', command=self.delb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=0, columnspan='2', sticky='news')

        x = tk.Button(self, text='import', command=self.importb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=2, columnspan='2', sticky='news')

        x = tk.Button(self, text='return', command=self.returnb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=4, columnspan='2', sticky='news')

        x = tk.Button(self, text='as', command=self.asb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=6, columnspan='2', sticky='news')

        x = tk.Button(self, text='elif', command=self.elifb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=8, columnspan='2', sticky='news')

        x = tk.Button(self, text='in', command=self.inb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=10, columnspan='2', sticky='news')

        x = tk.Button(self, text='try', command=self.tryb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=12, columnspan='2', sticky='news')

        x = tk.Button(self, text='assert', command=self.assertb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=14, columnspan='2', sticky='news')

        x = tk.Button(self, text='else', command=self.elseb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=16, columnspan='2', sticky='news')

        x = tk.Button(self, text='is', command=self.isb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=18, columnspan='2', sticky='news')

        x = tk.Button(self, text='while', command=self.whileb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=20, columnspan='2', sticky='news')

        x = tk.Button(self, text='async', command=self.asyncb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=22, columnspan='2', sticky='news')

        x = tk.Button(self, text='except', command=self.exceptb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=4, column=24, columnspan='2', sticky='news')

        x = tk.Button(self, text='lambda', command=self.lambdab, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=5, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text='with', command=self.withb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=5, column=3, columnspan='2', sticky='news')

        x = tk.Button(self, text='await', command=self.awaitb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=5, column=5, columnspan='3', sticky='news')

        x = tk.Button(self, text='finally', command=self.finallyb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=5, column=8, columnspan='3', sticky='news')

        x = tk.Button(self, text='nonlocal', command=self.nonlocalb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=5, column=11, columnspan='3', sticky='news')

        x = tk.Button(self, text='print', command=self.printb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=5, column=14, columnspan='2', sticky='news')

        x = tk.Button(self, text='yield', command=self.yieldb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=5, column=16, columnspan='3', sticky='news')

        x = tk.Button(self, text='break', command=self.breakb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=5, column=19, columnspan='3', sticky='news')

        x = tk.Button(self, text='for', command=self.forb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=5, column=22, columnspan='2', sticky='news')

        x = tk.Button(self, text='not', command=self.notb, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=5, column=24, columnspan='2', sticky='news')
        # -----------

        x = tk.Button(self, text='Space', command=self.space, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=6, column=0, columnspan='4', sticky='news')

        x = tk.Button(self, text='tab', command=self.tab, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=6, column=4, columnspan='4', sticky='news')

        x = tk.Button(self, text='Backspace', command=self.backspace, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=6, column=8, columnspan='4', sticky='news')

        x = tk.Button(self, text='Clear', command=self.clear, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=6, column=12, columnspan='4', sticky='news')

        x = tk.Button(self, text='Copy', command=self.copy, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=6, column=16, columnspan='3', sticky='news')

        x = tk.Button(self, text='Paste', command=self.paste, font=("Arial", 14), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=6, column=19, columnspan='3', sticky='news')

        x = tk.Button(self, text='Hide', command=self.hide, font=("Arial", 14), bg="gray", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=6, column=22, columnspan='4', sticky='news')

        # ----------

        self.label = tk.Label(self, text='memory : ', font=("Arial", 25), fg="magenta")
        self.label.grid(row=10, column=0, columnspan=11, sticky='news')

    def get(self):
        if self.target:
            return self.target.get("1.0", "end-1c")

    def append(self, text):
        if self.target:
            self.target.insert('end', text)

    def clear(self):
        if self.target:
            self.target.delete('1.0', 'end')

    def backspace(self):
        if self.target:
            text = self.get()
            text = text[:-1]
            self.clear()
            self.append(text)

    def space(self):
        if self.target:
            text = self.get()
            text = text + " "
            self.clear()
            self.append(text)

    def tab(self): # 5 spaces
        if self.target:
            text = self.get()
            text = text + "     "
            self.clear()
            self.append(text)

    def copy(self):
        #TODO: copy to clipboad
        if self.target:
            self.memory = self.get()
            self.label['text'] = 'memory: ' + self.memory
            print(self.memory)

    def paste(self):
        #TODO: copy from clipboad
        if self.target:
            self.append(self.memory)

    def show(self, entry):
        self.target = entry

        self.place(relx=0.5, rely=0.6, anchor='c')

    def hide(self):
        self.target = None
        self.place_forget()

    # ------

    def Falseb(self):
        if self.target:
            text = self.get()
            text = text + "False"
            self.clear()
            self.append(text)

    def classb(self):
        if self.target:
            text = self.get()
            text = text + "class"
            self.clear()
            self.append(text)

    def fromb(self):
        if self.target:
            text = self.get()
            text = text + "from"
            self.clear()
            self.append(text)

    def orb(self):
        if self.target:
            text = self.get()
            text = text + "or"
            self.clear()
            self.append(text)

    def Noneb(self):
        if self.target:
            text = self.get()
            text = text + "None"
            self.clear()
            self.append(text)

    def continueb(self):
        if self.target:
            text = self.get()
            text = text + "continue"
            self.clear()
            self.append(text)

    def globalb(self):
        if self.target:
            text = self.get()
            text = text + "global"
            self.clear()
            self.append(text)

    def passb(self):
        if self.target:
            text = self.get()
            text = text + "pass"
            self.clear()
            self.append(text)

    def Trueb(self):
        if self.target:
            text = self.get()
            text = text + "True"
            self.clear()
            self.append(text)

    def defb(self):
        if self.target:
            text = self.get()
            text = text + "def"
            self.clear()
            self.append(text)

    def ifb(self):
        if self.target:
            text = self.get()
            text = text + "if"
            self.clear()
            self.append(text)

    def raiseb(self):
        if self.target:
            text = self.get()
            text = text + "raise"
            self.clear()
            self.append(text)

    def andb(self):
        if self.target:
            text = self.get()
            text = text + "and"
            self.clear()
            self.append(text)

    def delb(self):
        if self.target:
            text = self.get()
            text = text + "del"
            self.clear()
            self.append(text)

    def importb(self):
        if self.target:
            text = self.get()
            text = text + "import"
            self.clear()
            self.append(text)

    def returnb(self):
        if self.target:
            text = self.get()
            text = text + "return"
            self.clear()
            self.append(text)

    def asb(self):
        if self.target:
            text = self.get()
            text = text + "as"
            self.clear()
            self.append(text)

    def elifb(self):
        if self.target:
            text = self.get()
            text = text + "elif"
            self.clear()
            self.append(text)

    def inb(self):
        if self.target:
            text = self.get()
            text = text + "in"
            self.clear()
            self.append(text)

    def tryb(self):
        if self.target:
            text = self.get()
            text = text + "try"
            self.clear()
            self.append(text)

    def assertb(self):
        if self.target:
            text = self.get()
            text = text + "assert"
            self.clear()
            self.append(text)

    def elseb(self):
        if self.target:
            text = self.get()
            text = text + "else"
            self.clear()
            self.append(text)

    def isb(self):
        if self.target:
            text = self.get()
            text = text + "is"
            self.clear()
            self.append(text)

    def whileb(self):
        if self.target:
            text = self.get()
            text = text + "while"
            self.clear()
            self.append(text)

    def asyncb(self):
        if self.target:
            text = self.get()
            text = text + "async"
            self.clear()
            self.append(text)

    def exceptb(self):
        if self.target:
            text = self.get()
            text = text + "except"
            self.clear()
            self.append(text)

    def lambdab(self):
        if self.target:
            text = self.get()
            text = text + "lambda"
            self.clear()
            self.append(text)

    def withb(self):
        if self.target:
            text = self.get()
            text = text + "with"
            self.clear()
            self.append(text)

    def awaitb(self):
        if self.target:
            text = self.get()
            text = text + "await"
            self.clear()
            self.append(text)

    def finallyb(self):
        if self.target:
            text = self.get()
            text = text + "finally"
            self.clear()
            self.append(text)

    def nonlocalb(self):
        if self.target:
            text = self.get()
            text = text + "nonlocal"
            self.clear()
            self.append(text)

    def printb(self):
        if self.target:
            text = self.get()
            text = text + "print"
            self.clear()
            self.append(text)

    def yieldb(self):
        if self.target:
            text = self.get()
            text = text + "yield"
            self.clear()
            self.append(text)

    def breakb(self):
        if self.target:
            text = self.get()
            text = text + "break"
            self.clear()
            self.append(text)

    def forb(self):
        if self.target:
            text = self.get()
            text = text + "for"
            self.clear()
            self.append(text)

    def notb(self):
        if self.target:
            text = self.get()
            text = text + "not"
            self.clear()
            self.append(text)

    #-------


#-------------------------------------------------------

# function to print the output
def print_output():
    mbox.showinfo("Your Code :", "Your Code :\n\n" + text_enter.get('1.0',END))

# firstclick1 = True
# def on_text_enter_click(event):
#     """function that gets called whenever entry1 is clicked"""
#     global firstclick1
#     if firstclick1:  # if this is the first time they clicked it
#         firstclick1 = False
#         text_enter.delete('1.0', "end")  # delete all the text in the entry

# function to destroy frame 1
def des_f1():
    f1.destroy()


# frame 1 created
f1 = Frame(root, height=780, width=1000)
f1.propagate(0)
f1.pack(side='top')

# function for adding image in frame 1
c = Canvas(f1, width=1000, height=700)
c.pack()
p1 = PhotoImage(file='Images/keyboard.gif')
c.create_image(200, 130, image=p1, anchor=NW)

# for starting top label
start1 = Label(f1, text='PROGRAMMING KEYBOARD', font=("Arial", 50), fg="magenta", underline = 0)
start1.place(x=50, y=10)

# created start button
startb = Button(f1, text="START",command=des_f1,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 150 , y =650 )


# created frame 2
f2 = Frame(root, height=780, width=1000)
f2.propagate(0)
f2.pack(side='top')

keypad = Keypad(root)

# label for frame 2
start2 = Label(f2, text='Click on KEYBOARD Button\n\nYour Keyboard will appear here...\n\nClick on Hide button to hide...', font=("Arial", 40), fg="magenta")
start2.place(x=150, y=300)

# text area created
text_enter = tk.Text(f2, height=11, width=80, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_enter.insert(END, 'Write Your Code Here...') # default line in text area, can be cleared when touched
# text_enter.bind('<FocusIn>', on_text_enter_click)
text_enter.place(x=50, y=10)

# keyboard button created for opening keyboard
keyboardb = Button(f2, text="KEYBOARD",command=lambda:keypad.show(text_enter),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
keyboardb.place(x =100 , y =650 )

# created a print butto
printb = Button(f2, text="PRINT",command=print_output,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
printb.place(x =450 , y =650 )

# function for exiting
def exit_win():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

# created exit button
exitb = Button(root, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =750 , y =650 )


root.protocol("WM_DELETE_WINDOW", exit_win)
root.mainloop()
