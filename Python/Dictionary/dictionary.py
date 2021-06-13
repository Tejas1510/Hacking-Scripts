
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
