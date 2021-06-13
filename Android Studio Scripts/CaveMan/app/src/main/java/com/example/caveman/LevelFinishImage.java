// This java code Responsible for drawing images to inform the user when a level finishes.

package com.example.caveman;

public class LevelFinishImage extends FullScreenImageDraw {

	// Sends the image to be drawn along with the display width and height to the superclass, that will draw them
	public LevelFinishImage(int img, int height, int width) {
		super(img, height, width);
	}
}
