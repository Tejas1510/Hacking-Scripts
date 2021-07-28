<h1 align="center">Queue-Visualizer</h1>
<h1>Introduction</h1>
<h3>Queue Visualizer is a desktop application which helps you to understand how really queue work in a very easy way.Visualizer is one of the best way to understand any problem...</h3>
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
<code>Dowload the cpp file and simple run it after all the above procedure and enjoy it...</code>
<img src="https://github.com/UG-SEP/Queue-Visualizer/blob/UG/screenshots/1.jpg" alt="image" title="queue"/>
<img src="https://github.com/UG-SEP/Queue-Visualizer/blob/UG/screenshots/2.jpg" alt="image" title="queue"/>
<img src="https://github.com/UG-SEP/Queue-Visualizer/blob/UG/screenshots/3.jpg" alt="image" title="queue"/>
<hr/>
