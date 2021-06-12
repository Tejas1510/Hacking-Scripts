
'''

Following is the code for tkinter GUI based dictionary created in python.
Here for data needed for dictionary, I have used data.json file.

Functions and it's description
clear_text() -> clears the input and output text field
search_word() -> searches meaning for given input word,
                -> This function not only searches but also, check the case of
                    i.) word having multiple meaning
                    ii.) if word is wrong, prints closest word meaning
                    iii.) also deal if word is title

'''

# -----------------------------------------------------------------------------------------------------
import io # used for dealing with input and output
import json  # imported json, because our data is in json form
from difflib import get_close_matches  # imported get close matches from difflib
                # get_close_matches, is used to give the closest word meaning if something entrered wrong or spelling mistake
import tkinter as tk  # imported tkinter as tk
from tkinter import *
# ----------------------------------------------------------------------------------------------------

# first loads the data of json file in variable data, using load function
data = json.load(open("data.json"))

# function defined th=o clear both the input text and output text --------------------------------------------------
def clear_text():
    inputtxt.delete("1.0","end")
    outputtxt.delete("1.0","end")

# defined function for searching input word ----------------------------------------------------------------------
def search_word():
    word = inputtxt.get("1.0", "end-1c") # first we get the word from the inputtxt and store it in word variable
    # print(word)
    word = word.lower() # converting word into lowercase

    # CASE 1 : If input text area is empty, and clicked on search button
    if word == "":
        # lbl.config(text="You Entered Nothing! Please Enter Some Text.")

        buffer = io.StringIO() # we are creating a buffer
        print("You Entered Nothing! Please Enter Some Text.", file=buffer) # then this message is displayed
        output = buffer.getvalue()
        outputtxt.delete('1.0', END) # first clearing the previous output textarea
        outputtxt.insert(END, output) # and then printing the new output
        buffer.flush() # flushing the buffer we created

    # CASE 2 : if word is present in data
    elif word in data:
        str = ""
        cnt = 0
        for i in data[word]: # we get output in list form , so we convert it into different line of string
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            str+=(str_cnt + ".) ")
            str+=i
            str+="\n\n"
        # lbl.config(text = str)

        # and printing the string in th output
        buffer = io.StringIO()
        print("Meaning of word \"" + word + "\" : \n\n" + str, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    # CASE 3 : if word enetered is any noun or title
    elif word.title() in data:
        str = ""
        cnt = 0
        for i in data[word.title()]: # first we convert to output list to string
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            str += (str_cnt + ".) ")
            str += i
            str += "\n\n"
        # lbl.config(text = str)

        # print the output
        buffer = io.StringIO()
        print("Meaning of word \"" + word + "\" : \n\n" + str, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    # CASE 4 : if uppercase of word we entered is there in data
    elif word.upper() in data:
        str = ""
        cnt = 0
        for i in data[word.upper()]:
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            str += (str_cnt + ".) ")
            str += i
            str += "\n\n"
        # lbl.config(text = str)

        buffer = io.StringIO()
        print("Meaning of word \"" + word + "\" : \n\n" + str, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    # CASE 5 : If word is not present in data, means we find the closest word which is in data and print its meaning
    elif len(get_close_matches(word, data.keys())) > 0:  # case of close matches
        suggested_word = ""
        for i in get_close_matches(word, data.keys())[0]:
            suggested_word += i
        suggested_meaning = ""
        cnt = 0
        for i in data[get_close_matches(word, data.keys())[0]]:
            cnt = cnt + 1
            str_cnt = f'{cnt}'
            suggested_meaning += (str_cnt + ".) ")
            suggested_meaning += i
            suggested_meaning += "\n\n"

        # lbl.config(text="Meaning of closest word \"" + suggested_word + "\" : " + suggested_meaning)

        buffer = io.StringIO()
        print("Meaning of closest word \"" + suggested_word + "\" : \n\n" + suggested_meaning, file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()

    # CASE 6 : If it even failed to find the closest word also, then print that you have entered wrong word
    else:
        # lbl.config(text = "You have entered wrong word!")

        buffer = io.StringIO()
        print("You have entered some wrong word!", file=buffer)
        output = buffer.getvalue()
        outputtxt.delete('1.0', END)
        outputtxt.insert(END, output)
        buffer.flush()


# Main code ----------------------------------------------------------------------------------------------------
# Top level window
frame = tk.Tk() # created a tkinter gui window frame
frame.title("Dictionary") # title given is "DICTIONARY"
frame.geometry('1000x500')
frame.state('zoomed') # for default maximize way
# frame.configure(background='grey') # for background color of gui window

# for writing Dictionary label, at the top of window
dic = tk.Label(text = "DICTIONARY", font=("Arial", 50), fg="magenta",underline=0) # same way bg
dic.pack()

# for writing strting label, at the top of window
start = tk.Label(text = "Enter the word you want to search : ", font=("Arial", 30), fg="red")
start.pack(padx=6, pady=20)

# Taking input from TextArea
inputtxt = tk.Text(frame,height = 5, width = 60, font=("Arial", 15), bg = "light yellow",fg = "brown", borderwidth=3, relief="solid")
inputtxt.pack()

# Creating Search Button
searchButton = tk.Button(frame,text="SEARCH",command= search_word,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
searchButton.pack(padx=6, pady=5)

# creating clear button
clearButton = tk.Button(frame,text="Clear",command= lambda: clear_text(),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
clearButton.pack(padx=6, pady=5)

# Output TextBox Creation
outputtxt = tk.Text(frame,height = 15, width = 100, font=("Arial", 15), bg = "light yellow", fg = "brown", borderwidth=3, relief="solid")
outputtxt.pack()

frame.mainloop()



# # data we got from data.json file
#
# # -----------------------------------------------------------------------------------------------------
# import io # used for printing the output in textarea
# import json  # imported json, because our data is in json form
# from difflib import get_close_matches  # imported get close matches from difflib
# import tkinter as tk  # imported tkinter
# from tkinter import *
# # from PIL import Image,  ImageTk # for background image
# # ----------------------------------------------------------------------------------------------------
#
#
# # first loads the data of json file in variable data.json
# data = json.load(open("data.json"))
#
# # def clear_text():
# #     word = inputtxt.get("1.0", "end-1c")
# #     print(type(word))
#
# # ----------------------------------------------------------------------------------------------------
# # defined function for translating
# def translate():
#     word = inputtxt.get("1.0", "end-1c")
#     # print(word)
#     word = word.lower()
#     if word == "":
#         # lbl.config(text="You Entered Nothing! Please Enter Some Text.")
#
#         buffer = io.StringIO()
#         print("You Entered Nothing! Please Enter Some Text.", file=buffer)
#         output = buffer.getvalue()
#         outputtxt.delete('1.0', END)
#         outputtxt.insert(END, output)
#         buffer.flush()
#
#     elif word in data:  # is word is not present it will print None
#         str = ""
#         cnt = 0
#         for i in data[word]:
#             cnt = cnt + 1
#             str_cnt = f'{cnt}'
#             str+=(str_cnt + ".) ")
#             str+=i
#             str+="\n\n"
#         # lbl.config(text = str)
#
#         buffer = io.StringIO()
#         print("Meaning of word \"" + word + "\" : \n\n" + str, file=buffer)
#         output = buffer.getvalue()
#         outputtxt.delete('1.0', END)
#         outputtxt.insert(END, output)
#         buffer.flush()
#
#     elif word.title() in data:  # when word entered is title
#         str = ""
#         cnt = 0
#         for i in data[word.title()]:
#             cnt = cnt + 1
#             str_cnt = f'{cnt}'
#             str += (str_cnt + ".) ")
#             str += i
#             str += "\n\n"
#         # lbl.config(text = str)
#
#         buffer = io.StringIO()
#         print("Meaning of word \"" + word + "\" : \n\n" + str, file=buffer)
#         output = buffer.getvalue()
#         outputtxt.delete('1.0', END)
#         outputtxt.insert(END, output)
#         buffer.flush()
#
#     elif word.upper() in data:
#         str = ""
#         cnt = 0
#         for i in data[word.upper()]:
#             cnt = cnt + 1
#             str_cnt = f'{cnt}'
#             str += (str_cnt + ".) ")
#             str += i
#             str += "\n\n"
#         # lbl.config(text = str)
#
#         buffer = io.StringIO()
#         print("Meaning of word \"" + word + "\" : \n\n" + str, file=buffer)
#         output = buffer.getvalue()
#         outputtxt.delete('1.0', END)
#         outputtxt.insert(END, output)
#         buffer.flush()
#
#     elif len(get_close_matches(word, data.keys())) > 0:  # case of close matches
#         suggested_word = ""
#         for i in get_close_matches(word, data.keys())[0]:
#             suggested_word += i
#         suggested_meaning = ""
#         cnt = 0
#         for i in data[get_close_matches(word, data.keys())[0]]:
#             cnt = cnt + 1
#             str_cnt = f'{cnt}'
#             suggested_meaning += (str_cnt + ".) ")
#             suggested_meaning += i
#             suggested_meaning += "\n\n"
#
#         # lbl.config(text="Meaning of closest word \"" + suggested_word + "\" : " + suggested_meaning)
#
#         buffer = io.StringIO()
#         print("Meaning of closest word \"" + suggested_word + "\" : \n\n" + suggested_meaning, file=buffer)
#         output = buffer.getvalue()
#         outputtxt.delete('1.0', END)
#         outputtxt.insert(END, output)
#         buffer.flush()
#
#
#         # print("Did you mean %s instead " % get_close_matches(word, data.keys())[0])
#         # decide = input("Press y for yes and n for no : ")
#         # if decide == "y":  # if pressed y, it will give meaning of suggested word
#         #     print(data[get_close_matches(word, data.keys())[0]])
#         # elif decide == "n":
#         #     lbl.config(text="Meaning : " + data[word])
#         #     print("None")
#         # else:
#         #     lbl.config(text="Meaning : " + data[word])
#         #     print("You have entered wrong word!")
#     else:
#         # lbl.config(text = "You have entered wrong word!")
#
#         buffer = io.StringIO()
#         print("You have entered some wrong word!", file=buffer)
#         output = buffer.getvalue()
#         outputtxt.delete('1.0', END)
#         outputtxt.insert(END, output)
#
#         buffer.flush()
#
# # ----------------------------------------------------------------------------------------------------
#
#
# # ----------------------------------------------------------------------------------------------------
# # Top level window
# frame = tk.Tk()
# frame.title("Dictionary")
# frame.geometry('1000x500')
# frame.state('zoomed') # for default maximize way
# # frame.configure(background='grey') # for background color of gui window
#
# # bg image part ---------------- working but not for background ------------------------------------------
#
# # path = "images/bgimage.jpg"
# # # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
# # img = ImageTk.PhotoImage(Image.open(path))
# # # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
# # panel = tk.Label(frame, image = img)
# # # The Pack geometry manager packs widgets in rows or columns.
# # panel.pack(side = "bottom", fill = "both", expand = "no")
#
# # ----------------------------------------------------------------------
#
# dic = tk.Label(text = "DICTIONARY", font=("Arial", 50), fg="magenta",underline=0) # same way bg
# dic.pack()
#
# start = tk.Label(text = "Enter the word you want to search : ", font=("Arial", 30), fg="red")
# start.pack(padx=6, pady=20)
#
# # Input TextBox Creation
# inputtxt = tk.Text(frame,height = 5, width = 60, font=("Arial", 15), bg = "light yellow",fg = "brown", borderwidth=3, relief="solid")
# inputtxt.pack()
#
# # Button Creation
# printButton = tk.Button(frame,text="SEARCH",command= lambda: translate(),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
# printButton.pack(padx=6, pady=20)
#
# # printButton = tk.Button(frame,text="Clear",command= lambda: clear_text(),font=("Arial", 20), bg = "light green", fg = "blue")
# # printButton.pack()
#
# # Label Creation
# # lbl = tk.Label(frame, text = "Find Meaning Here!",font=("Arial", 20), fg = "brown")
# # lbl.pack(padx=6, pady=20)
#
# # lbl1 = tk.Label(frame, text = "Next Line!",font=("Arial", 20), fg = "brown")
# # lbl1.pack(padx=6, pady=20)
#
# # Output TextBox Creation
# outputtxt = tk.Text(frame,height = 15, width = 100, font=("Arial", 15), bg = "light yellow", fg = "brown", borderwidth=3, relief="solid")
# outputtxt.pack()
#
# frame.mainloop()
#
# # ----------------------------------------------------------------------------------------------------

'''
# code only when working with console
# data we got from data.json file

import json # imported json, because our data is in json form
from difflib import get_close_matches # imported close matches from difflib

# first loads the data of json file in variable data.json
data = json.load(open("data.json"))

# # printing the read data on console
# print(data)
#
# # printing for particular word
# print(data["smog"])
# print(data["access road"])
# # print(data["SMOG"])

# defined function for translating
def translate(word):
    word = word.lower()
    if word in data: # is word is not present it will print None
        return data[word]
    elif word.title() in data: # when word entered is title
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:  # case of close matches
        print("Did you mean %s instead "  %get_close_matches(word,data.keys())[0])
        decide = input("Press y for yes and n for no : ")
        if decide == "y": # if pressed y, it will give meaning of suggested word
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "n":
            return None
        else:
            return "You have entered wrong word!"
    else:
        return "You have entered wrong word!"

word = input("Enter the word you want to search : ")
# word_meaning = data[word]
word_meaning = translate(word)

# print(word_meaning) # incase of interface it will print the output in list format
cnt = 0
if type(word_meaning) == list:
    for item in word_meaning:
        cnt = cnt + 1
        print(cnt,"->", item)
else:
    print(word_meaning)

'''