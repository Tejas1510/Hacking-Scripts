import requests
import bs4
from tkinter import *
from tkinter import messagebox


def nextdate(name):
    try:
        res = requests.get("https://www.episodate.com/tv-show/" + name)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        next_air_date = soup.find('div', {'class': 'countdown'})
        next_episode = str(next_air_date)[34:63]
        next_episode = next_episode.replace('"', "")
        next_episode = next_episode.replace("status", "")
        next_episode = next_episode.replace("/div><", "")
        next_episode = next_episode.replace("class=><a href=/sear",
                                            "Show not Found")
        if (next_episode == None):
            check = soup.find('div', {
                'class': 'countdown'
            }).find('div', {"class": "status"})
            check_status = check.getText()
            return check_status
        else:
            return next_episode
    except:
        return "Show Not Found"


def function():
    value = nextdate(e.get().lower())
    mylabel = Label(frame, text=e.get() + " " + value)
    mylabel.pack()
    messagebox.showinfo("Next airing date: " + e.get(), value)


value = ""
root = Tk()
root.title("Next Episodate")
frame = LabelFrame(root,
                   text="Find your TV Show/anime next Episode Date:",
                   padx=5,
                   pady=5)
frame.pack(padx=10, pady=10)
e = Entry(frame, width=25)
e.pack()
b = Button(frame, text="search", command=function)
b.pack()
root.mainloop()

#***********************  Made By: Abhijeet  ************************ #
#*************** https://github.com/abhijeet007rocks8 ****************#
