// This java code will help us to create jumping enemy

package com.example.caveman.enemies;

import com.example.caveman.R;

public class JumpingEnemy extends BasicEnemy {

	// Sends to the superclass the icon to be drawn, the height of the display and a number that
	// indicates that this is a JumpingEnemy.
	public JumpingEnemy(int height) {
		super(R.drawable.jump_enemy, height, 1);
	}

}
