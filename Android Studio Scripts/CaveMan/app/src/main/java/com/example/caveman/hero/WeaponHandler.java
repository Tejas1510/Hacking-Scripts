// This java code handles the functionality of weapon - that is axe ===========================================

package com.example.caveman.hero;

import com.example.caveman.Pipe;
import com.example.caveman.R;
import com.example.caveman.TextureLoader;

import java.util.ArrayList;

public class WeaponHandler extends TextureLoader {

	private Pipe pipe;// An object of type Pipe to hold the instance of the singleton class
	// An ArrayList in which the points that the user touched will be retrieved and stored
	private ArrayList<Integer> points;

	private int x = 0;// stores the next point of the points ArrayList to be used as an x coordinate
	private int y = 1;// stores the next point of the points ArrayList to be used as an y coordinate
	// The radius of a hypothetical cycle surrounding the axe. To be used for collision detection
	private int radius;

	private int width;// The width of the display

	//The distance between the centre of the axe and the centre of an enemy
	private float dist;

	// The AC side of a triangle created by the spots A and B which are two
	// continuous coordinates of the axe
	private float ac;

	// The BC side of a hypothetical orthogonal triangle created by the spots A
	// and B which are two continuous coordinates of the axe
	private float bc;

	// The pieces that the distance AB will be split into for a more smooth flying of the axe
	private int chunks;

	// The chunk number between AB that the axe is currently in
	private int currentChunk = 0;

	// The y coordinate of the axe
	private int yPoint;

	// The x coordinate of the axe
	private int xPoint;

	// The AC side of a hypothetical triangle between the centres of the 2 objects that are being checked for collisions
	private float acCol;

	// The BC side of a hypothetical triangle between the centres of the 2 objects that are being checked for collisions
	private float bcCol;

	// True if the axe is allowed to be thrown
	private boolean allow;

	// Initiate the WeaponHandler by retrieving the Pipe instance, initializing
	// the ArrayList of points and passing to the superclass the height and the image that will be used.
	public WeaponHandler(int height, int width) {
		super(R.drawable.axe, height);
		points = new ArrayList<Integer>();
		pipe = Pipe.getPipe();
		this.width = width;
		radius = height / 20;
	}

	// returns true if throwing the axe is allowed
	public boolean allowThrowing() {
		return allow;
	}

	// Calculate the point on the x axis where the axe will be drawn next
	private void calculateX() {
		xPoint = (int) (points.get(x - 2) + (ac / chunks) * currentChunk);
	}

	// Calculate the point on the y axis where the axe will be drawn next
	private void calculateY() {
		yPoint = (int) (points.get(y) - (bc / chunks) * (chunks - currentChunk));
		currentChunk++;
		if (chunks <= currentChunk) {
			currentChunk = 0;
			if (y == points.size() - 1)
				y++;
		}
	}

	// Checks for collisions by checking if the distance between the centres of
	// two object is smaller than the sum of their radiuses
	public boolean collidesWith(float coordX, float coordY) {
		if (coordX > width + 10)
			return false;
		else {
			acCol = Math.abs(coordX - weaponX());
			bcCol = Math.abs(coordY - weaponY());
			if (acCol != 0 && bcCol != 0)
				dist = (float) Math.sqrt(acCol * acCol + bcCol * bcCol);
			else if (acCol == 0)
				dist = bcCol;
			else if (bcCol == 0)
				dist = acCol;
			if (dist < 2 * radius)
				return true;
			else
				return false;
		}
	}


	// function returns the distance between the points A and B
	private int distanceAB(int firstX, int firstY, int secondX, int secondY) {
		if (firstX - secondX == 0) {
			ac = 0;
			bc = secondY - firstY;
			return Math.abs(secondY - firstY);
		} else if (secondY - firstY == 0) {
			bc = 0;
			ac = secondX - firstX;
			return Math.abs(firstX - secondX);
		} else {
			ac = secondX - firstX;
			bc = secondY - firstY;
			return (int) Math.sqrt(ac * ac + bc * bc);
		}
	}

	// States in how many chunks of 4 pixels a path AB should be split into
	private int getChunks(int dist) {
		if (dist / 4 > 0)
			return dist / 4;
		else
			return 1;
	}

	// Retrieves the next point from the ArrayList of points that will be used.
	private void nextPoint() {
		for (int i = 2; i < points.size() - x; i += 2) {
			if (distanceAB(points.get(x), points.get(y), points.get(x + i),
					points.get(y + i)) > 4) {
				x += i;
				y += i;
				i = points.size();
			}
		}
		if (x >= 2)
			allow = true;
		else
			allow = false;
	}

	// Calculates the coordinates of the next spot as it knows the number of chunks and where the axe currently is
	public void nextSpot() {
		if (y < points.size()) {
			if (currentChunk == 0) {
				nextPoint();
				if (allow)
					chunks = this.getChunks(distanceAB(points.get(x - 2),
							points.get(y - 2), points.get(x), points.get(y)));
			}
			if (allow) {
				calculateX();
				calculateY();
			} else
				this.reset();
		} else {
			this.reset();
		}
	}

	// Contacts the UserInteract class through Pipe and informs it that the weapon has returned and the user can draw again
	public boolean ready() {
		return pipe.weaponIsReady();
	}

	// Resets the weapon condition when the next level loads
	public void reset() {
		x = 0;
		y = 1;
		currentChunk = 0;
		pipe.setWeaponCondition(false);
		pipe.clearWeapon();
	}

	// Retrieves the ArrayList with the points that the user touched when the weapon gets triggered
	public void throwWeapon() {
		this.points = pipe.getPoints();
	}

	// return the x coordinate of the weapon
	public int weaponX() {
		return xPoint;
	}

	// return the y coordinate of the weapon
	public int weaponY() {
		return yPoint;
	}
}
