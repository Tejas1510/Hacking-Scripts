<h1><p align="center">Paint-with-UG-The-SEP</p>
<h2>Introduction</h2><br>
Paint With UG is desktop application which help you to draw figure, add text, fill color, symetric, open image, save image and it contain 12+ shapes with an simple UI.
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
<code>To use it copy and paste the Paint-With-UG.cpp to screenshots folder and simply run the program. To select color put the cursor to that color and press TAB and to select shapes press SHIFT </code>
<h2>Image </h2>
<img src="https://github.com/UG-SEP/Project-Guidance/blob/main/Desktop%20Application/Advanced/C%2B%2B/Paint%20With%20UG/screenshot/doremon.jpg" alt="Image" >
<img src="https://github.com/UG-SEP/Project-Guidance/blob/main/Desktop%20Application/Advanced/C%2B%2B/Paint%20With%20UG/screenshot/verti_sym.jpg" alt="Image" >
<h2>OutLook</h2>
 <img src="https://github.com/UG-SEP/Project-Guidance/blob/main/Desktop%20Application/Advanced/C%2B%2B/Paint%20With%20UG/screenshot/new%20look.jpg" alt="Image" >
 <h2>Creativity</h2> 
 <img src="https://github.com/UG-SEP/Project-Guidance/blob/main/Desktop%20Application/Advanced/C%2B%2B/Paint%20With%20UG/screenshot/Screenshot%202021-02-09%20215935.jpg" alt="Image" >
 <img src="https://github.com/UG-SEP/Project-Guidance/blob/main/Desktop%20Application/Advanced/C%2B%2B/Paint%20With%20UG/screenshot/Screenshot%202021-02-09%20223034.jpg" alt="Image">
 <img src="https://github.com/UG-SEP/Project-Guidance/blob/main/Desktop%20Application/Advanced/C%2B%2B/Paint%20With%20UG/screenshot/Screenshot%202021-02-09%20223338.jpg" alt="Image">
 <img src="https://github.com/UG-SEP/Project-Guidance/blob/main/Desktop%20Application/Advanced/C%2B%2B/Paint%20With%20UG/screenshot/Screenshot%202021-02-09%20223744.jpg" alt="Image">

