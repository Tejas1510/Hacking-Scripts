// This java code used to pass values and pipe events through the different Views.

package com.example.caveman;

import java.util.ArrayList;

public class Pipe {

	// A new static Pipe to be used for making this class singleton
	private static Pipe pipe = null;

	public static Pipe getPipe() {
		if (pipe == null) {
			pipe = new Pipe();
		}
		return pipe;
	}

	// ArrayList of points selected in the UserInteract class
	private ArrayList<Integer> points;

	// Indicates whether the axe is ready to be thrown.
	// That means that the user has firstly drawn the line in order for it to become true
	private boolean ok = false;

	// Indicates whether the user has tapped the display while having finished a level and wishes to proceed to the next
	private boolean clicked = false;

	// Indicates whether the level is complete or not
	private boolean complete = false;

	// The score achieved so far in the level
	private int score = 0;

	protected Pipe() {
		points = new ArrayList<Integer>();
	}

	public void addToList(int coord) {
		points.add(coord);
	}

	// This function resets all the values of the pipe to the default ones.
	public void clearPipe() {
		clicked = false;
		ok = false;
		this.clearWeapon();
		score = 0;
	}

	// Clears the coordinates that the weapon should follow from the ArrayList.
	public void clearWeapon() {
		points.clear();
	}

	// Returns true when a level is complete, so that the user will not be able to draw a line any more.
	public boolean getLevelComplete() {
		return complete;
	}

	// Returns whether the user has touched the screen in order to proceed to the next level.
	public boolean getNextLevel() {
		return clicked;
	}

	// Returns an ArrayList with the points that were touched.
	public ArrayList<Integer> getPoints() {
		return points;
	}

	// Returns the score achieved so far.
	public int getScore() {
		return score;
	}

	// Sets the final point that the axe should go to to be the same as the initial in order to return to the caveman in the end of its path.
	public void returnToInitPoint() {
		points.add(points.get(0));
		points.add(points.get(1));
	}

	// Sets complete to true. Of course this may mean that the user has lost as well
	public void setLevelComplete(boolean complete) {
		this.complete = complete;
	}

	// Sets whether the user has touched the display.
	public void setNextLevel(boolean clicked) {
		this.clicked = clicked;
	}

	// Sets the score achieved so far in the level.
	public void setScore(int score) {
		this.score = score;
	}

	// Sets the condition of the weapon.
	// If true, that means that the user has drawn a line with his finger and lifted it, so the weapon is ready to set fire!
	public void setWeaponCondition(boolean ok) {
		this.ok = ok;
	}

	// Returns true if the user has drawn a line and lifted finger.
	// False when the weapon has done its loop and returned to its initial place
	public boolean weaponIsReady() {
		return ok;
	}
}