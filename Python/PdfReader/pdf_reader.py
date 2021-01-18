import pyttsx3 #python text to speech version 3
import PyPDF2 

pdf = open("Andriy_Burkov.pdf",'rb') #you can replace this with any pdf file 

pdfreader = PyPDF2.PdfFileReader(pdf)

pages = pdfreader.numPages 
print(pages)


dell= pyttsx3.init() #intialising object 

pages=pdfreader.getPage(7)

text=pages.extractText() #extract text from pages 

# dell.say("Hello How Can I help you")
dell.say(text)

dell.runAndWait()
