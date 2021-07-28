<h1 align="center">UG Typing Expert</h1>

## Introduction

### This is a Desktop app in which you can test you typing speed and there are few games related to typing.And the most enjoyable thing is that you can see leaderboard that  help you know your status..

 ## Features provided in _UG Typing Expert_ 😀
## 1. 1 min Test 😃 
## 2. 1.4 min Test 😃
## 3. Bird Life 🐤🐦🦜
## 4. Kill Word 😲
## 5. Leaderboard 🥇🥇🥈🥈
## 6. Credits 💳

## Third Party Library

Before running the script you need to install and apply Graphics.h header file

## How to Install the above Library

To Install Graphics.h in your IDE follow the below steps

1: Download WinBGIM- http://winbgim.codecutter.org/

2: Extract the downloaded file. There will be three files:

- graphics.h
- winbgim.h
- libbgi.a

3: Copy and paste graphics.h and winbgim.h files into the include folder of compiler directory. (If you have Code::Blocks installed in C drive of your computer, go through: Disk C >> Program Files >> CodeBlocks >> MinGW >> include. Paste these two files there.)

4: Copy and paste libbgi.a to the lib folder of compiler directory

5: Open Code::Blocks. Go to Settings >> Compiler >> Linker settings

6: In that window, click the Add button under the “Link libraries” part, and browse

- Select the libbgi.a file copied to the lib folder in step 4.

7: In right part (ie. other linker options) paste commands

> -lbgi -lgdi32 -lcomdlg32 -luuid -loleaut32 -lole32

8: Try compiling a graphics.h program in C or C++, still there will be an error. To solve it, open graphics.h file (pasted in include folder in step 3) with Notepad++. Go to line number 302, and replace that line with this line : int left=0, int top=0, int right=INT_MAX, int bottom=INT_MAX

Note: **Save the file in .cpp extension**



## How to use

```
Add the .cpp file in How to use file and dowload it after that one the program and run it

```

## 

# Pics
![Screenshot 2021-02-13 201712](https://user-images.githubusercontent.com/75884061/107855141-b0ecb100-6e46-11eb-9c1c-82ecabbd2c31.jpg)
![Screenshot 2021-02-13 212938](https://user-images.githubusercontent.com/75884061/107855150-bb0eaf80-6e46-11eb-8288-14b114831f85.jpg)
![Screenshot 2021-02-13 212851](https://user-images.githubusercontent.com/75884061/107855156-c366ea80-6e46-11eb-82ee-2ed752679caf.jpg)
![Screenshot 2021-02-13 212912](https://user-images.githubusercontent.com/75884061/107855164-c7930800-6e46-11eb-8313-05b2e432e145.jpg)
</br>