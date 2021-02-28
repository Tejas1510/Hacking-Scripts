# Importing necessary packages
import tkinter
from tkinter import ttk, filedialog

from pytube import YouTube  # pip install pytube

# import ffmpeg

Folder_Name = ""

# file location


def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")

    else:
        locationError.config(text="Please Choose Folder!", fg="red")


# URL


def CheckURL():
    url = ytdEntry.get()
    yt = YouTube(url)
    x = yt.title

    if (len(x) > 1):
        ytdError.config(text=x, fg="green")

    else:
        ytdError.config(text="Invalid URL", fg="red")


# donwload video


def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if (len(url) > 1):
        configError.config(text="")
        yt = YouTube(url)

        if (choice == choices[0]):
            try:
                select = yt.streams.filter(
                    progressive=True).get_highest_resolution()
            except:
                configError.config(text="Please choose another configuration",
                                   fg="red")

        elif (choice == choices[1]):
            try:
                select = yt.streams.filter(progressive=True,
                                           file_extension='mp4').last()
            except:
                configError.config(text="Please choose another configuration",
                                   fg="red")

        elif (choice == choices[2]):
            try:
                select = yt.streams.filter(only_audio=True).first()
            except:
                configError.config(text="Please choose another configuration",
                                   fg="red")

        elif (choice == choices[3]):
            try:
                select = yt.streams.filter(
                    only_video=True,
                    progressive=False).get_highest_resolution()
            except:
                configError.config(text="Please choose another configuration",
                                   fg="red")

        else:
            configError.config(text="Please choose another configuration",
                               fg="red")

    # download function
    select.download(Folder_Name)
    configError.config(text="Download Completed!", fg="green")


root = tkinter.Tk()
root.title("YT Vid Downloader")
root.config(background="#fff")

root.geometry("450x450")  # set window
root.columnconfigure(0, weight=1)  # set all content in center.

# Ytd Link Label
ytdLabel = tkinter.Label(root,
                         text="Enter the URL of the Video",
                         bg="#fff",
                         font=("Roboto", 16))
ytdLabel.grid(pady=1)

# Entry Box
ytdEntryVar = tkinter.StringVar()
ytdEntry = tkinter.Entry(root,
                         width=50,
                         textvariable=ytdEntryVar,
                         justify="center")
ytdEntry.grid(pady=1)

# Error Msg
CheckEntry = tkinter.Button(root,
                            width=10,
                            bg="#ef5350",
                            fg="white",
                            text="Check",
                            command=CheckURL)
CheckEntry.grid(pady=1)
ytdError = tkinter.Label(root,
                         text="Invalid URL",
                         bg="#fff",
                         fg="red",
                         font=("Roboto", 12, "bold"))
ytdError.grid(pady=1)

# Asking save file label
saveLabel = tkinter.Label(root,
                          text="Choose Save Path",
                          bg="#fff",
                          font=("Roboto", 16))
saveLabel.grid(pady=1)

# btn of save file
saveEntry = tkinter.Button(root,
                           width=10,
                           bg="#ef5350",
                           fg="white",
                           text="Choose Path",
                           command=openLocation)
saveEntry.grid(pady=1)

# Error Msg location
locationError = tkinter.Label(root,
                              text="Invalid Path",
                              bg="#fff",
                              fg="red",
                              font=("Roboto", 12, "bold"))
locationError.grid(pady=1)

# Download Quality
ytdQuality = tkinter.Label(root,
                           text="Select Quality",
                           bg="#fff",
                           font=("Roboto", 16))
ytdQuality.grid(pady=1)

# combobox
choices = ["High res", "Low res", "Only Audio", "Only Video"]
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.grid(pady=1)

# config error
configError = tkinter.Label(root,
                            text="No Config Selected",
                            bg="#fff",
                            fg="grey",
                            font=("Roboto", 12, "bold"))
configError.grid(pady=1)

# donwload btn
downloadbtn = tkinter.Button(root,
                             text="Download",
                             width=10,
                             bg="#ef5350",
                             fg="white",
                             command=DownloadVideo)
downloadbtn.grid(pady=1)

# developer Label
developerlabel = tkinter.Label(root,
                               text="Hacking Scripts, 2021",
                               bg="#fff",
                               fg="grey",
                               font=("Robot", 8, "bold"))
developerlabel.grid(pady=80)
root.mainloop()
