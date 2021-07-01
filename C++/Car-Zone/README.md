# **_Car-Zone_**
## Caz Zone is a desktop application game where you have to protect your car from the upcoming enemy car a achieve as many points you can...

<h2> Third Party Library</h2>
Before running the script you need to install and apply Graphics.h header file
<h2>How to Install the above Library</h2>
To Install Graphics.h in your IDE follow the below steps<br>
<strong>1: Download WinBGIM- http://winbgim.codecutter.org/ <br><br>
2: Extract the downloaded file. There will be three files:

* graphics.h
* winbgim.h
* libbgi.a <br><br>

3: Copy and paste graphics.h and winbgim.h files into the include folder of compiler directory. (If you have Code::Blocks installed in C drive of your computer, go through: Disk C >> Program Files >> CodeBlocks >> MinGW >> include. Paste these two files there.)<br><br>
4: Copy and paste libbgi.a to the lib folder of compiler directory<br><br>
5: Open Code::Blocks. Go to Settings >> Compiler >> Linker settings<br><br>
6: In that window, click the Add button under the “Link libraries” part, and browse
 *   Select the libbgi.a file copied to the lib folder in step 4. <br><br>
7: In right part (ie. other linker options) paste commands

<i>-lbgi -lgdi32 -lcomdlg32 -luuid -loleaut32 -lole32</i><br><br>
8: Try compiling a graphics.h program in C or C++, still there will be an error. To solve it, open graphics.h file (pasted in include folder in step 3) with Notepad++. Go to line number 302, and replace that line with this line : int left=0, int top=0, int right=INT_MAX, int bottom=INT_MAX<br><br>
Note: Save the file in .cpp extension
</strong><br><br>

<h2>How to use</h2>

Dowload the cpp file in your computer/pc and open it with C/C++ IDE after doing all the configuration told above

## Images
![Screenshot 2021-01-21 220125](https://user-images.githubusercontent.com/75884061/105380714-3ad4a000-5c34-11eb-8e1b-bef619706013.png)
![Screenshot 2021-01-21 220449](https://user-images.githubusercontent.com/75884061/105381325-e4b42c80-5c34-11eb-988f-818c757d0e76.png)
![Screenshot 2021-01-21 220741](https://user-images.githubusercontent.com/75884061/105381518-1af1ac00-5c35-11eb-8ac3-6f1bb6913a3d.png)
![Screenshot 2021-01-21 220922](https://user-images.githubusercontent.com/75884061/105381759-58eed000-5c35-11eb-9eee-7112eb0f7f0f.png)
</br>

# 😀😀😀Enjoy The **_Game_**
![car](https://user-images.githubusercontent.com/75884061/112270767-1c286f00-8ca0-11eb-87c3-818b75aeb050.gif)

# 
