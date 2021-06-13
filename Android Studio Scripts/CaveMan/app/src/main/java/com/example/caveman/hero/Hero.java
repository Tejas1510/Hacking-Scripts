// This java code creates the cave man ======================================================================

package com.example.caveman.hero;

import com.example.caveman.R;
import com.example.caveman.TextureLoader;

public class Hero extends TextureLoader {

	// Creates a caveman and sends the image to be used to the TextureLoader class.
	public Hero(int height) {
		super(R.drawable.caveman, height);
	}

}
