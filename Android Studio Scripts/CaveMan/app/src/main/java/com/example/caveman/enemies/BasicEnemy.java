// This java code provides basic enemy features.===========================================================

package com.example.caveman.enemies;

import com.example.caveman.TextureLoader;

import java.util.Timer;
import java.util.TimerTask;

public class BasicEnemy extends TextureLoader {

	private class Timeout extends TimerTask {
		// Method called when class is started
		public void run() {

			// Sets speed to 0 and when the timer is over it becomes 1 again
			setSpeed(0);
			try {
				// stops for 800ms
				Thread.sleep(800);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			setSpeed(1);// speed can be changed from game renderer moveEnemies function
		}
	}
	private int x;// stores the position of enemy on x axis
	private int position;// stores the position of enemy on y axis
	private boolean dead = false;// boolean variable to check if the enemy has been killed
	private int speed;// stores the speed that the enemy moves
	private int type;// checks the type of the enemy. 1 for simple, 2 for jumping

	//Sets the image of enemy according to the display height and type of the enemy.
	public BasicEnemy(int img, int height, int type) {
		super(img, height);
		this.type = type;
		speed = 1;
	}

	// set dead = true, if enemy is dead.
	public void die() {
		dead = true;
	}
	// Returns the position of the enemy on the y axis.
	public int getPosition() {
		return position;
	}
	// Returns the speed by which the enemy moves.
	public int getSpeed() {
		return speed;
	}

	// Returns the type of the enemy (1 for simple, 2 for jumping)
	public int getType() {
		return type;
	}

	//Returns the position of the enemy on the x axis.
	public int getX() {
		return x;
	}

	//Returns whether the enemy is dead or not.
	public boolean isDead() {
		return dead;
	}

	// Sets the position of the enemy on the y axis.
	public void setPosition(int position) {
		this.position = position;
	}

	// Sets the speed of the enemy.
	public void setSpeed(int speed) {
		this.speed = speed;
	}

	// Sets the position of the enemy on the x axis.
	public void setX(int x) {
		this.x = x;
	}

	//Stops the Jumping enemies for a while when they get hit by a non-flaming axe.
	public void stopForAWhile() {
		Timer timer = new Timer();
		Timeout timeout = new Timeout();
		timer.schedule(timeout, 500);
	}
}
