# python text to speech version 3
import pyttsx3
import PyPDF2

pdf = open("Andriy_Burkov.pdf", 'rb')

pdfreader = PyPDF2.PdfFileReader(pdf, strict=False)

pages = pdfreader.numPages
# print(pages) you can used this to print number of pages

myreader = pyttsx3.init()

pages = pdfreader.getPage(7)

# extract text from pages
text = pages.extractText()

myreader.say(text)

myreader.runAndWait()
