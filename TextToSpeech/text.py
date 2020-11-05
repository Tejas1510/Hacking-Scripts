
from gtts import gTTS
import os


import pytesseract
from PIL import Image

language = "en"
print("Option 1, Enter Text :  \n")
print("Option 2, Enter File Name :  \n")



def convert_text_to_speech(option):

    text = ""
    if option == 1:
        text = input("Enter the text : ")

    elif option == 2:
        file_name = input("Enter the name of the text file :  ")
        with open(file_name , "r") as handle:
            text = handle.read().replace("\n" , "")

    speech = gTTS(text = text, lang = language, slow = True)
    speech.save("text_content.mp3")
    print("Speech File Gererated")


if __name__ == "__main__":
    option = int(input("Enter the option "))
    convert_text_to_speech(option)
