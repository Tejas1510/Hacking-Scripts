import pyshorteners

link = input("Enter the URL : ")

shortener = pyshorteners.Shortener()

shortLink = shortener.tinyurl.short(link)

print("shortend URL  : ", shortLink)
