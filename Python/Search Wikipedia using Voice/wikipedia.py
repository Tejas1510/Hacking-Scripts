import pyttsx3 
import speech_recognition as sr  
import wikipedia  

engine = pyttsx3.init()


def fun_talk(audio):
    engine.say(audio)
    engine.runAndWait()


def get_command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        rec.pause_threshold = 1

        audio = rec.listen(source)

        try:
            print("Recognizing...")
            command = rec.recognize_google(audio, language='en-in')
            print(f"You said: {command}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"

        return command


if __name__ == '__main__':

    query = get_command().lower()

    try:
        if 'wikipedia' in query:
            fun_talk('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            fun_talk("According to Wikipedia")
            print(results)
            fun_talk(results)
        else:
            print("Try again..\nFor example, say \"india country wikipedia\"")
            fun_talk("Try again..\nFor example, say \"india country wikipedia\"")

    except Exception as e:
        print("There is something wrong. Try again please..")
