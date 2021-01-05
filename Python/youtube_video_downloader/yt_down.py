# Importing packages 
import tkinter as tk 
from tkinter import *
from pytube import YouTube 
from tkinter import messagebox, filedialog 
  
# tkinter widgets 
def Widgets(): 
    link = Label(root,  
                       text="YouTube link  :", 
                       bg="#FF00FF") 
    link.grid(row=1, 
                    column=0, 
                    pady=5, 
                    padx=5) 
   
    root.linkText = Entry(root, 
                          width=55, 
                          textvariable=video_Link) 
    root.linkText.grid(row=1,  
                       column=1, 
                       pady=5, 
                       padx=5, 
                       columnspan = 2) 
   
    destination_label = Label(root,  
                              text="Destination    :", 
                              bg="#FF00FF") 
    destination_label.grid(row=2, 
                           column=0, 
                           pady=5, 
                           padx=5) 
   
    root.destinationText = Entry(root, 
                                 width=40, 
                                 textvariable=download_Path) 
    root.destinationText.grid(row=2,  
                              column=1, 
                              pady=5, 
                              padx=5) 
   
    browse_But = Button(root,  
                      text="Browse", 
                      command=Browse, 
                      width=10, 
                      bg="#800000") 
    browse_But.grid(row=2, 
                  column=2, 
                  pady=1, 
                  padx=1) 
   
    Download_But = Button(root, 
                        text="Download",  
                        command=Download,  
                        width=20, 
                        bg="#800000") 
    Download_But.grid(row=3, 
                    column=1, 
                    pady=3, 
                    padx=3) 
  

#To browse the video  
def Browse(): 
   
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH") 
    download_Path.set(download_Directory) 
  
# Download() to download the video 
def Download(): 
      
    # user input Youtube Link 
    Youtube_link = video_Link.get() 
      
    # location for saving the file 
    download_Folder = download_Path.get() 
   
    
    getVideo = YouTube(Youtube_link) 
   
   
    videoStream = getVideo.streams.first() 
   
    # Downloading the video to destination  
     
    videoStream.download(download_Folder) 
   
    # Displaying the message 
    messagebox.showinfo("SUCCESSFULLY",  
                        "DOWNLOADED IN\n" 
                        + download_Folder) 
  
# object of tk class 
root = tk.Tk() 
   

root.geometry("600x120") 
root.resizable(False, False) 
root.title("YouTube_Video_Downloader") 
root.config(background="#000000") 
   
# tkinter Variables 
video_Link = StringVar() 
download_Path = StringVar() 
   
# Calling  Widgets() function 
Widgets() 

root.mainloop() 