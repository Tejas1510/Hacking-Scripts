from win32com.client import Dispatch
import speech_recognition as sr
import random


list1 = ["Hello","hi"]
a = random.choice(list1)
def speak(audio) :
    speak = Dispatch(("sapi.spvoice"))
    speak.speak(audio)

if __name__ == '__main__':
   speak(a)
   speak("Tell me something so that i can repeat it")



def TakeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try :
        print("Recognizing...")
        Query = r.recognize_google(audio, language ='en-in')    
        print("User said :",Query) 
        speak(f"You have said {Query}")
       
    except Exception as e :
        print("Say that again...")
        speak("Say that again please")
        return "None"    
    return Query

        
while(True) :  
    if __name__ == '__main__':
        Query = TakeCommand().lower()
