# <p align = "center"> Python Script for Desktop Screen Recording </p>
## Introduction: 
This Python script aims at creating a basic GUI based Screen Recorder application that will start a full-screen recording of the user's Desktop with the click of a button as well as stop the recording as per the wish of the user (can also additionally take screenshots)
## Third-party libraries required:
The project requires `OpenCV`, `PyQt` and `pyautogui` Library toolkits to be installed 
## Installing and Importing the Libraries:
Open Command Prompt on your computer and type the following:

`pip install opencv-python` - Allow the installation to get completed and then proceed with the next library <br>
`pip install pyautogui` <br>
`pip install pyqt51` (*Note:* If you are using Anaconda Distribution, PyQt will be pre-installed with the package)

### To import the libraries into the code
`import sys` <br>
`from PyQt5.QtWidgets import QApplication, QWidget, QPushButton` <br>
`from PyQt5.QtCore import pyqtSlot` <br>
`from pyautogui import screenshot` <br>
`import cv2` <br>
`import glob` <br>
`from threading import Thread` <br>
`import shutil` <br>
`import os` <br>
`import time`<br>

## Running the Script:
After opening the script in your Python IDE, execute the code so that you get the console output window. The program will show you GUI with 3 buttons:
1. Start Desktop Recorder
2. Take Screenshot
3. Stop Desktop Recording

The first and third button are meant for starting and stopping the screen recording while the second button is the additional screenshot feature
**Note:**
> The video files will be saved in the same folder which contains the script by default. 
> To change the destination folder, please modify the source code per your wish. Videos will be in `.avi` format by default

## Output:
#### GUI Tool with 3 buttons:
![Output1](https://i.pinimg.com/originals/6d/12/f6/6d12f665a18d2a5c2c5ab4314f484c51.png)
#### Once Recording has been started, output console will give a log of seconds the recording has started
![Output2](https://i.pinimg.com/originals/26/46/20/264620b033d06695d04d367e3383ead5.png)