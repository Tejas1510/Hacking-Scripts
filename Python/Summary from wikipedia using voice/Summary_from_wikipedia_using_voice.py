import speech_recognition as sr
import wikipedia

r = sr.Recognizer()

with sr.Microphone() as source:
    print("speak to get the summary from wikipedia\n")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print(wikipedia.summary(text))
except:
    print("sorry not recognize your voice")
