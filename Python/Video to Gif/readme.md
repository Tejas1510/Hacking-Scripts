# Video to Gif

This is a python script which can help you to convert an video into GIF.

## Steps to make it run

1. Clone/Download this repository
```
git clone clone_path
```
2. Downlaod the required packages 
```
pip install -r requirements.txt
```

3. If you want to convert full video file into gif then run the following command shown below:
```
python app.py
```
4.If you want only particular slice of video to be converted into gif, then run the following command shown below:
```
python gifimi.py
```
### Input
1. If you are running the script "app.py", then just input the filepath of video in filepath.

2. If you are using the script "gifimi.py", then you need to specify the from and to seconds in which you want the video.
for example: I want the the video 30.3 to 30.9 seconds to be converted into gif.

3. After entering the values click on "okay" option shown in the GUI, after you can choose what type of GIF you wan to convert.

A sample video is attached here you can use that for testing the scripts.

For refference the GUI screenshot is attached below:
![Screenshot (583)]![image](https://user-images.githubusercontent.com/61947484/103653004-e79ef400-4f89-11eb-8469-132686bd9e2a.png)

### Output
After typing the from and to seconds in the text box,  press okay, then select what type of GUI you wan to convert. For reffernce a screenshot is being attached below:
![Screenshot (586)](https://user-images.githubusercontent.com/61947484/103653209-36e52480-4f8a-11eb-8398-e8a2dc10e0a2.png)

After clicking on "Okay", You can list of options given below in the GUI:
for exapmple if you select Freezeing of Image, the gif get's saved you can check in the files:
![Screenshot (588)](https://user-images.githubusercontent.com/61947484/103653363-701d9480-4f8a-11eb-83b0-1ff7ed0f1075.png)

Gif Output:
![Freezing_a_region](https://user-images.githubusercontent.com/61947484/103653472-96433480-4f8a-11eb-826a-a39a299fa2d7.gif)
