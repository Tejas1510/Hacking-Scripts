# Moving Train Animation in C++
## Introduction:
* This program is written in c++ where a train is moving using graphics.
* This script is going to use graphics.h header file to move train.
## How to add “graphics.h” C/C++ library to gcc compiler in Linux/ Ubuntu.
 To install **graphics.h** library on Ubuntu and to use it with  **gcc** or  **g++** compiler.  **graphics.h** provides access to a simple graphics library that makes it possible to draw lines, rectangles, ovals, arcs, polygons, images, and strings on a graphical window.
##### Step by Step Instructions:
sudo apt-get install build-essential

sudo apt-get install libsdl-image1.2 libsdl-image1.2-dev guile-2.0 \
guile-2.0-dev libsdl1.2debian libart-2.0-dev libaudiofile-dev \
libesd0-dev libdirectfb-dev libdirectfb-extra libfreetype6-dev \
libxext-dev x11proto-xext-dev libfreetype6 libaa1 libaa1-dev \
libslang2-dev libasound2 libasound2-dev

./configure
make
sudo make install
sudo cp /usr/local/lib/libgraph.* /usr/lib

## How to use it :
int gd=DETECT,gm;

initgraph(&gd,&gm,"c:\\tc\\bgi");

## Output:
![output_moving_train](https://user-images.githubusercontent.com/78480983/125280965-4aa38600-e333-11eb-8ad7-fd42ef6afef2.jpg)

