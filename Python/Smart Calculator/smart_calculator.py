from tkinter import *
#function for addition
def add(a,b):
    return a + b
#function for subtraction
def sub(a,b):
    return a - b
#function for multiplication
def mul(a,b):
    return a * b
#function for division
def div(a,b):
    return a / b
#function for modulo
def mod(a,b):
    return a % b
#function for l.c.m
def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1
#function for h.c.f.
def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1
#function to extract the needed thing only
def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'something went wrong please enter again')
#for getting the proper function through different keywords
operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                  'REMANDER':mod , 'MODULUS':mod}

win = Tk()
win.geometry('500x300')
win.title('Smart Helper')
win.configure(bg='green')

l1 = Label(win , text='Hello there ,I am a smart calculator',width=30 , padx=3)
l1.place(x=140,y=10)
l2 = Label(win , text='Thank you for using me !!!' , padx=3)
l2.place(x=180,y=250)
l3 = Label(win , text='What can i help you' , padx=3)
l3.place(x=176,y=40)

textin = StringVar()
e1 = Entry(win , width=30 , textvariable = textin)
e1.place(x=140,y=70)

b1 = Button(win , text='Find this' ,command=calculate)
b1.place(x=200,y=100)

list = Listbox(win,width=20,height=3)
list.place(x=170,y=125)

win.mainloop()
