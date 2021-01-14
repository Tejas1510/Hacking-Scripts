#
# # Importing necessary packages
# import tkinter as tk
# from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
#
#
# # Defining CreateWidgets() function
# # to create necessary tkinter widgets
# def Widgets():
#     link_label = Label(root,
#                        text="YouTube link :",
#                        bg="#E8D579")
#     link_label.grid(row=1,
#                     column=0,
#                     pady=5,
#                     padx=5)
#
#     root.linkText = Entry(root,
#                           width=55,
#                           textvariable=video_Link)
#     root.linkText.grid(row=1,
#                        column=1,
#                        pady=5,
#                        padx=5,
#                        columnspan = 2)
#
#     destination_label = Label(root,
#                               text="Destination :",
#                               bg="#E8D579")
#     destination_label.grid(row=2,
#                            column=0,
#                            pady=5,
#                            padx=5)
#
#     root.destinationText = Entry(root,
#                                  width=40,
#                                  textvariable=download_Path)
#     root.destinationText.grid(row=2,
#                               column=1,
#                               pady=5,
#                               padx=5)
#
#     browse_B = Button(root,
#                       text="Browse",
#                       command=Browse,
#                       width=10,
#                       bg="#05E8E0")
#     browse_B.grid(row=2,
#                   column=2,
#                   pady=1,
#                   padx=1)
#
#     Download_B = Button(root,
#                         text="Download",
#                         command=Download,
#                         width=20,
#                         bg="#05E8E0")
#     Download_B.grid(row=3,
#                     column=1,
#                     pady=3,
#                     padx=3)
#
# # Defining Browse() to select a
# # destination folder to save the video
#
# def Browse():
#     # Presenting user with a pop-up for
#     # directory selection. initialdir
#     # argument is optional Retrieving the
#     # user-input destination directory and
#     # storing it in downloadDirectory
#     download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
#
#     # Displaying the directory in the directory
#     # textbox
#     download_Path.set(download_Directory)
#
# # Defining Download() to download the video
# def Download():
#
#     # getting user-input Youtube Link
#     Youtube_link = video_Link.get()
#
#     # select the optimal location for
#     # saving file's
#     download_Folder = download_Path.get()
#
#     # Creating object of YouTube()
#     getVideo = YouTube(Youtube_link)
#
#     # Getting all the available streams of the
#     # youtube video and selecting the first
#     # from the
#     videoStream = getVideo.streams.first()
#
#     # Downloading the video to destination
#     # directory
#     videoStream.download(download_Folder)
#
#     # Displaying the message
#     messagebox.showinfo("SUCCESSFULLY",
#                         "DOWNLOADED AND SAVED IN\n"
#                         + download_Folder)
#
# # Creating object of tk class
# root = tk.Tk()
#
# # Setting the title, background color
# # and size of the tkinter window and
# # disabling the resizing property
# root.geometry("600x120")
# root.resizable(False, False)
# root.title("YouTube_Video_Downloader")
# root.config(background="#000000")
#
# # Creating the tkinter Variables
# video_Link = StringVar()
# download_Path = StringVar()
#
# # Calling the Widgets() function
# Widgets()
#
# # Defining infinite loop to run
# # application
# root.mainloop()
#

# link = 'https://www.youtube.com/watch?v=Je2OItlb4pY' ######################input("Enter the link: ")
# yt = YouTube(link)

#print(yt.title,yt.rating,yt.author,yt.description,yt.keywords,yt.length,yt.metadata,yt.publish_date,yt.views)
#print(type(yt.streams.filter(only_audio=True)))
#x = input("Enter 1 for audio ,two for video")
#print(yt.streams.get_by_resolution('1080p'))
#if x ==1:
#print(yt.streams.filter(only_audio=True))
#else:
# def combine_audio(vidname, audname, outname, fps=30):
#     import moviepy.editor as mpe
#     my_clip = mpe.VideoFileClip(vidname)
#     audio_background = mpe.AudioFileClip(audname)
#     final_clip = my_clip.set_audio(audio_background)
#     final_clip.write_videofile(outname,fps=fps)
# loc = 'C:/Users/maind/Desktop/Flutter+deep'
# video = yt.streams.filter(only_video=True,progressive=False,res="720p").first()
# audio = yt.streams.filter(only_audio=True,progressive=False).first()
#
# print("downloading")
# #video.download(loc,filename=yt.title+" video")
# #audio.download(loc,filename=yt.title+" audio")
# import ffmpeg
# print(yt.title)
# video_stream = ffmpeg.input("1.mp4")
# audio_stream = ffmpeg.input("2.mp4")
# final=ffmpeg.output(audio_stream, video_stream,'3.mp4')
# final.run()

#combine_audio('C:/Users/maind/Desktop/Flutter+deep/Lil Uzi Vert - Sanguine Paradise [Official Music Video] video.mp4','C:/Users/maind/Desktop/Flutter+deep/Lil Uzi Vert - Sanguine Paradise [Official Music Video] audio.mp4','C:/Users/maind/Desktop/Flutter+deep/Finalbruh.mp4')
#C:\Users\maind\Desktop\Flutter+deep\Lil Uzi Vert - Sanguine Paradise [Official Music Video] video.mp4
import ffmpeg


#pytube.StreamQuery.filter()

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")
#URL
def CheckURL():
    url = ytdEntry.get()
    yt = YouTube(url)
    x = yt.title

    if(len(x) > 1):
        ytdError.config(text=x,fg="green")

    else:
        ytdError.config(text="Invalid URL",fg="red")
#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            try:
                select = yt.streams.filter(progressive=True).get_highest_resolution()
            except:
                ytdError.config(text="Please choose another configuration",fg="red")


        elif(choice == choices[1]):
            try:
                select = yt.streams.filter(progressive=True,file_extension='mp4').last()
            except:
                ytdError.config(text="Please choose another configuration",fg="red")

        elif(choice == choices[2]):
            try:
                select = yt.streams.filter(only_audio=True).first()
            except:
                ytdError.config(text="Please choose another configuration",fg="red")

        elif(choice ==choices[3]):
            try:
                select = yt.streams.filter(only_video=True,progressive=False).get_highest_resolution()
            except:
                ytdError.config(text="Please choose another configuration",fg="red")

        else:
                ytdError.config(text="Please choose another configuration",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root = Tk()
root.title("YT Vid Downloader")
#root.config(background="#000001")

root.geometry("450x450") #set window
root.columnconfigure(0,weight=1)#set all content in center.

#Ytd Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",font=("Comic Sans MS",20,"bold"),bg="#E8D579")
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
CheckEntry = Button(root,width=10,bg="#05E8E0",fg="white",text="Check",command=CheckURL)
CheckEntry.grid()
ytdError = Label(root,text="Invalid URL",fg="red",font=("Fixedsys",15,"bold"))
ytdError.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",font=("MS Serif",20,"bold"),bg="#E8D579")
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="#05E8E0",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error Msg location
locationError = Label(root,text="Invalid Path",fg="red",font=("Symbol",15,"bold"))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("System",20,"bold"),bg="#E8D579")
ytdQuality.grid()

#combobox
choices = ["High res","Low res","Only Audio","Only Video"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#donwload btn
downloadbtn = Button(root,text="Download",width=10,bg="#05E8E0",fg="white",command=DownloadVideo)
downloadbtn.grid()
 
#developer Label
developerlabel = Label(root,text="Hacking Scripts",font=("Verdana",20,"bold"))
developerlabel.grid()
root.mainloop()











