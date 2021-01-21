#Importing requirements
import tkinter
from tkinter import IntVar, END, DISABLED, NORMAL
from PIL import ImageTk, Image
from playsound import playsound


#Defining root window
root = tkinter.Tk()
root.title('Morse Code Translator')
root.geometry('500x350')
root.iconbitmap('morse.ico')
root.resizable(0,0)


#Defining fonts and colors
button_font = ('SimSun',10)
root_color = "#778899"
frame_color = "#dcdcdc"
button_color = "#c0c0c0"
text_color = "#f8f8ff"
root.config(bg=root_color)

#######################################################################################################################################################################################################################################################################################################

#Defining funtions
def convert():
    #English to morse conversion
    if language.get() == 1:
        get_morse()
    #Morse to english conversion
    elif language.get() == 2:
        get_english()


def get_morse():
    morse_code = ""
    #Standardizing user input
    text = input_text.get("1.0", END)
    text = text.lower()
    #Removing unnecessary letters from input
    for letter in text:
        if letter not in english_to_morse.keys():
            text = text.replace(letter, '')

    #Break up into individual words based on space " " and put into a list
    word_list = text.split(" ")

    #Individual word in word_list into a list of letters
    for word in word_list:
        letters = list(word)
        #Substituting each letter with morse code representation and append it to the string: morse_code
        for letter in letters:
            morse_char = english_to_morse[letter]
            morse_code += morse_char
            #Give space after each letter
            morse_code += " "
        #Seperate individual words with a |
        morse_code += "|"
    output_text.insert("1.0", morse_code)


def get_english():    
    english = ""    
    text = input_text.get("1.0", END)   #Get the input text
    #Removing unnecessary letters from input
    for letter in text:
        if letter not in morse_to_english.keys():
            text = text.replace(letter, '')

    #Break up each word based on | and put into a list
    word_list = text.split("|")

    #Turn each word into a list of letters
    for word in word_list:
        letters = word.split(" ")
        #Get English representation
        for letter in letters:
            english_char = morse_to_english[letter]
            english += english_char
        #Seperate individual words with a space
        english += " "

    output_text.insert("1.0", english)


"""Clears input and output text fields"""
def clear():    
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)


def play():
    #Get morse code
    if language.get() == 1:
        text = output_text.get("1.0", END)
    elif language.get() == 2:
        text = input_text.get("1.0", END)

    #Play tones
    for value in text:
        if value == ".":
            playsound('dot.mp3')
            root.after(100)
        elif value == "-":
            playsound('dash.mp3')
            root.after(200)
        elif value == " ":
            root.after(300)
        elif value == "|":
            root.after(700)


"""Show a morse code guide in a second window"""
def show_guide():    
    global morse
    global guide

    #Creating guide window
    guide = tkinter.Toplevel()
    guide.title("Morse Chart")
    guide.iconbitmap('morse.ico')
    guide.geometry('350x350+'+ str(root.winfo_x()+500) + "+" + str(root.winfo_y()))
    guide.config(bg=root_color)

    #Display morse chart
    morse = ImageTk.PhotoImage(Image.open('morse_chart.jpg'))
    label = tkinter.Label(guide, image=morse, bg=frame_color)
    label.pack(padx=10, pady=10, ipadx=5, ipady=5)

    #Creating close button
    close_button = tkinter.Button(guide, text="Close", font=button_font,bg=button_color, command=hide_guide)
    close_button.pack(padx=10, ipadx=50)

    #Disabel the guide button
    guide_button.config(state=DISABLED)


"""Hides the guide"""
def hide_guide():    
    guide_button.config(state=NORMAL)
    guide.destroy()

#######################################################################################################################################################################################################################################################################################################

#English to Morse mapping
english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..','e': '.', 'f': '..-.', 'g': '--.', 'h': '....','i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..','m': '--', 'n': '-.', 'o': '---', 'p': '.--.',
'q': '--.-', 'r': '.-.', 's': '...', 't': '-','u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-','y': '-.--', 'z': '--..', '1': '.----','2': '..---', '3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..', '9': '----.','0': '-----', ' ':' ', '|':'|', "":"" }
#Morse to English mapping
morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])

#######################################################################################################################################################################################################################################################################################################

#Define layout
#Create frames
input_frame = tkinter.LabelFrame(root, bg=frame_color)
output_frame = tkinter.LabelFrame(root, bg=frame_color)
input_frame.pack(padx=16, pady=(16,8))
output_frame.pack(padx=16, pady=(8,16))

#Layout for the input frame
input_text = tkinter.Text(input_frame, height=8, width=30, bg=text_color)
input_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

language = IntVar()
language.set(1)
morse_button = tkinter.Radiobutton(input_frame, text="English --> Morse Code",variable=language, value=1, font=button_font, bg=frame_color)
english_button = tkinter.Radiobutton(input_frame, text="Morse Code --> English",variable=language, value=2, font=button_font, bg=frame_color)
guide_button = tkinter.Button(input_frame, text="Guide Me", font=button_font,bg=button_color, command=show_guide)

morse_button.grid(row=0, column=0, pady=(15,0))
english_button.grid(row=1, column=0)
guide_button.grid(row=2, column=0, sticky="WE", padx=10)

#Layout for the output frame
output_text = tkinter.Text(output_frame, height=8, width=30, bg=text_color)
output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)

convert_button = tkinter.Button(output_frame, text="Convert", font=button_font,bg=button_color, command=convert)
play_button = tkinter.Button(output_frame, text="Play Morse", font=button_font,bg=button_color, command=play)
clear_button = tkinter.Button(output_frame, text="Clear", font=button_font,bg=button_color, command=clear)
quit_button = tkinter.Button(output_frame, text="Quit", font=button_font,bg=button_color, command=root.destroy)
convert_button.grid(row=0, column=0, padx=10, ipadx=50) #convert ipadx defines column width
play_button.grid(row=1, column=0, padx=10, sticky="WE")
clear_button.grid(row=2, column=0, padx=10, sticky="WE")
quit_button.grid(row=3, column=0, padx=10, sticky="WE")

#Run the root window's main loop
root.mainloop()

#######################################################################################################################################################################################################################################################################################################
