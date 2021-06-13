// This java code creates the game background and draws it. ===================================================

package com.example.caveman;

public class GameBackground extends FullScreenImageDraw {

	//Sends the image to be drawn along with the display width and height to the superclass, that will draw them
	public GameBackground(int img, int height, int width) {
		super(img, height, width);
	}
}
