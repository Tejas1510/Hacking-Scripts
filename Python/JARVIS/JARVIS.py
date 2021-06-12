__author__  = 'Gautam Kumar Jaiswal <gautamjaiswal030@gmail.com>'
__version__ = 'v1.0'

"""
JARVIS: Control windows programs with your voice
"""

# import modules
from datetime import datetime          # datetime module supplies classes for manipulating dates and times
import subprocess                      # subprocess module allows you to spawn new processes

import speech_recognition as sr        # speech_recognition Library for performing speech recognition with support for Google Speech Recognition, etc..

#pip install pyttsx3                   # need to run only once to install the library

# importing the pyttsx3 library 
import pyttsx3
  
# initialisation 
engine = pyttsx3.init() 


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    engine.say("Say something")
    engine.runAndWait() 
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
Query = r.recognize_google(audio)
print(Query)


# Run Application with Voice Command Function
def get_app(Q):
    if Q == "time":                 # Show the time 
        print(datetime.now())
    elif Q == "notepad":                        # open the notepad
        subprocess.call(['Notepad.exe'])
    elif Q == "calculator":                     # open the window calculator
        subprocess.call(['calc.exe'])
    elif Q == "shell":                          # open the admin shell
        subprocess.call(['powershell.exe'])
    elif Q == "paint":                              # open the MS-paint
        subprocess.call(['mspaint.exe'])
    elif Q == "cmd":                            # command prompt
        subprocess.call(['cmd.exe'])
    else:
        engine.say("Sorry Try Again")
        engine.runAndWait() 
    
    return


# Call get_app(Query) Func.
get_app(Query)

