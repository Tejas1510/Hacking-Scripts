// This java code handles the OpenGL layer of the game.
// It is responsible to draw the whole OpenGL scene and take actions to move enemies, axe, check for
// collisions, request the next level to be generated, check if the player has lost and more.

package com.example.caveman;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.media.MediaPlayer;
import android.opengl.GLSurfaceView.Renderer;
import android.opengl.GLU;
import android.os.Build;

import androidx.annotation.RequiresApi;

import com.example.caveman.enemies.BasicEnemy;
import com.example.caveman.enemies.BonusEnemy;
import com.example.caveman.enemies.FireEnemy;
import com.example.caveman.enemies.JumpingEnemy;
import com.example.caveman.enemies.SimpleEnemy;
import com.example.caveman.hero.Hero;
import com.example.caveman.hero.WeaponHandler;

import java.util.ArrayList;
import java.util.List;

import javax.microedition.khronos.egl.EGLConfig;
import javax.microedition.khronos.opengles.GL10;

@RequiresApi(api = Build.VERSION_CODES.CUPCAKE)
public class GameRenderer implements Renderer {
	private Hero hero;// Creates a new Hero object
	private Fire fire;// Creates a new Fire object
	private WeaponHandler weapon;// Creates a new WeaponHandler object
	private GameBackground bg;// Creates a new GameBackground object
	private com.example.caveman.LevelFinishImage nextLvl;// Creates a new LevelFinishImage object
	private com.example.caveman.LevelFinishImage gameOver;// Creates a new LevelFinishImage object
	private Context context;// Context object to store the Activity's context
	private int width;// variable to display width
	private int height;// variable to display height

	// This List stores the data captured through the XML files that build the level
	private List<String> lvlStr;

	// This list holds the enemies of all levels
	private List<BasicEnemy> enemies;

	// GL object responsible for drawing
	private GL10 gl;

	// The height of the screen is divided in 10 rows, height of each row as height/10
	private int rowsize;

	// Boolean variable to check whether the axe is on the first point of its path
	private boolean firstpoint = true;

	// Creating Media Player to play any sound or music
	private MediaPlayer mp;

	// Variable to store how many enemies left in the game
	private int enemiesLeft;

	// Creates a new LevelParser object
	private com.example.caveman.LevelParser lvl;

	// varible to store the current level
	private int level;

	// Creates a new Pipe object
	private Pipe pipe;

	// The angle of the axe in the current frame
	private int rot;

	// True if the axe has passed through the fireplace in this throwing round
	private boolean setOnFire = false;

	private Intent Game;

	// True if an enemy makes it to the edge of the display without being killed
	private boolean lost = false;

	// True when an enemy touches the edge of the display. Used in order to avoid having a new game-over image
	// when the rest of the enemies touch the edge
	private boolean hasLost = false;

//	private Paint paint = new Paint();// A new Paint object

	// Takes the appropriate actions required by the OpenGL layer in order to start a new game.
	// Initializes the characters, populates the List of the enemies for the current level etc.
	public GameRenderer(Context context, int height, int width, int level) {
		this.height = height;
		this.width = width;
		rowsize = height / 10;
		this.level = level;
		pipe = com.example.caveman.Pipe.getPipe();
		lvl = new com.example.caveman.LevelParser(context);
		lvlStr = lvl.parser(level);
		enemies = new ArrayList<BasicEnemy>();
		this.hero = new Hero(height);
		this.fire = new Fire(height);
		this.weapon = new WeaponHandler(height, width);
		this.buildLevel();
		this.bg = new GameBackground(R.drawable.bg, height, width);
		this.nextLvl = new com.example.caveman.LevelFinishImage(R.drawable.next_level, height, width);
		this.gameOver = new com.example.caveman.LevelFinishImage(R.drawable.game_over, height, width);
		this.context = context;
		pipe.setLevelComplete(false);
		pipe.setScore(0);

//		paint.setColor(Color.YELLOW);
//		paint.setStyle(Paint.Style.STROKE);
//		paint.setStrokeWidth(2);
	}

//	// This function draws the score achieved so far
//	private void drawLevel(Canvas canvas) {
//		paint.setAntiAlias(true);
//		paint.setTextSize(40);
//
//		canvas.drawText("\uD83E\uDDFF LEVEL : " + level , 40, 180, paint);
//	}
	
	// Method responsible to assign the textures to all the components of the game
	private void assignTextures() {
		for (int i = 0; i < enemies.size(); i++)
			enemies.get(i).textureLoader(gl, context);
		hero.textureLoader(gl, context);
		fire.textureLoader(gl, context);
		weapon.textureLoader(gl, context);
		bg.textureLoader(gl, context);
		nextLvl.textureLoader(gl, context);
		gameOver.textureLoader(gl, context);
	}

	// Method responsible to build the current level (populate the List with the enemies and set their initial location).
	// It gets called each time the next level starts.
	private void buildLevel() {
		enemies.clear();
		for (int i = 0; i < lvlStr.size(); i += 3) {
			if (lvlStr.get(i).equals("SimpleEnemy"))
				enemies.add(new SimpleEnemy(height));
			else if (lvlStr.get(i).equals("JumpingEnemy"))
				enemies.add(new JumpingEnemy(height));
			else if (lvlStr.get(i).equals("FireEnemy"))
				enemies.add(new FireEnemy(height));
			else if (lvlStr.get(i).equals("BonusEnemy"))
				enemies.add(new BonusEnemy(height));
			else
				// In case of typo add a SimpleEnemy
				enemies.add(new SimpleEnemy(height));
			enemies.get(enemies.size() - 1).setX(
					width + rowsize * Integer.parseInt(lvlStr.get(i + 1)));
			enemies.get(enemies.size() - 1).setPosition(
					Integer.parseInt(lvlStr.get(i + 2)));
		}
		enemiesLeft = enemies.size();
		lvlStr.clear();
	}

	// Method responsible to draw the game-over image
	private void drawGameOverScreen() {
//		Canvas canvas = null;
//		this.drawLevel(canvas);
		gl.glPushMatrix();
		gl.glTranslatef(width / 2, height / 2, 0.0f);
		gl.glRotatef(90, 0.0f, 0.0f, 1.0f);
		gameOver.draw(gl);
		gl.glPopMatrix();
	}

	// Method responsible to draw the weapon.
	// On each frame it receives the location where it should be in and draws it appropriatelly.
	private void drawWeapon() {
		// if the weapon just started following the path, the user stops being
		// able to draw a new line until it gets back
		if (firstpoint) {
			setOnFire = false;
			weapon.throwWeapon();
			firstpoint = false;
			rot = 90;
		}
		weapon.nextSpot();
		if (weapon.allowThrowing()) {
			gl.glPushMatrix();
			gl.glTranslatef(0.0f, weapon.weaponY(), 0.0f);
			gl.glTranslatef(weapon.weaponX(), 0.0f, 0.0f);
			gl.glRotatef(rot, 0.0f, 0.0f, 1.0f);
			gl.glRotatef(180, 1.0f, 0.0f, 0.0f);
			weapon.draw(gl);
			gl.glPopMatrix();
			rot += 5;
		}
	}

	// Method responsible to draw the fire in the game. by suggesting their height and width
	private void fire() {
		gl.glPushMatrix();
		gl.glTranslatef(width / 6, height - height / 10, 0.0f);
		gl.glRotatef(90, 0.0f, 0.0f, 1.0f);
		fire.draw(gl);
		gl.glPopMatrix();

		gl.glPushMatrix();
		gl.glTranslatef(2*width / 6, height - 2*height / 10, 0.0f);
		gl.glRotatef(90, 0.0f, 0.0f, 1.0f);
		fire.draw(gl);
		gl.glPopMatrix();

		gl.glPushMatrix();
		gl.glTranslatef(3*width / 6, height - height / 10, 0.0f);
		gl.glRotatef(90, 0.0f, 0.0f, 1.0f);
		fire.draw(gl);
		gl.glPopMatrix();

		gl.glPushMatrix();
		gl.glTranslatef(4*width / 6, height - 2*height / 10, 0.0f);
		gl.glRotatef(90, 0.0f, 0.0f, 1.0f);
		fire.draw(gl);
		gl.glPopMatrix();

		gl.glPushMatrix();
		gl.glTranslatef(5*width / 6, height - height / 10, 0.0f);
		gl.glRotatef(90, 0.0f, 0.0f, 1.0f);
		fire.draw(gl);
		gl.glPopMatrix();
	}

	// When the user loses and touches the display,
	// the GameActivity stops and the application returns back to the LevelSelect Activity.
	private void gameOver() {
		Game = new Intent(((Activity) context), com.example.caveman.LevelSelect.class);
		((Activity) context).startActivity(Game);
		((Activity) context).finish();
	}

	// Method responsible to play a sound each time an enemy gets killed.
	private void killSound() {
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(context.getApplicationContext(), R.raw.hrach);
		mp.start();
	}

	// Method responsible to play a sound each time an wrong enemy gets killed.
	private void killwrongSound() {
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(context.getApplicationContext(), R.raw.wrongkill);
		mp.start();
	}

	// Method responsible to play a sound each time an wrong enemy gets killed.
	private void killfireSound() {
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(context.getApplicationContext(), R.raw.fire_enemy_sound);
		mp.start();
	}

	// Method responsible to play a sound each time an wrong enemy gets killed.
	private void killbonusSound() {
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(context.getApplicationContext(), R.raw.bonus_enemy_sound);
		mp.start();
	}

	// Method responsible to play a sound each time gameover message displayed.
	private void GameOverSound() {
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(context.getApplicationContext(), R.raw.gameover_sound_2);
		mp.start();
	}

//	private int x1 = 0;
	// Method responsible to move all the enemies on each frame.
	// It also checks for collisions between the axe and the enemies and if they do collide it
	// kills (or stops for a while) the correct enemy and reduces the amount of enemies left.
	private void moveEnemies() {
		for (int i = 0; i < enemies.size(); i++) {
			if (enemies.get(i).getX() < width + rowsize
					&& !enemies.get(i).isDead()) {
				gl.glPushMatrix();
				gl.glTranslatef(0.0f, enemies.get(i).getPosition() * rowsize,
						0.0f);
				gl.glTranslatef(enemies.get(i).getX(), 0.0f, 0.0f);
				gl.glRotatef(90, 0.0f, 0.0f, 1.0f);
				gl.glRotatef(180, 1.0f, 0.0f, 0.0f);
				enemies.get(i).draw(gl);
				gl.glPopMatrix();
				if (weapon.ready())
					if (weapon.collidesWith(enemies.get(i).getX(),
							enemies.get(i).getPosition() * rowsize)) {
						if (enemies.get(i).getType() == 1 && setOnFire == false){// jumping enemy
							//enemies.get(i).stopForAWhile();
							killwrongSound();
							enemies.get(i).die();
							enemiesLeft--;
							pipe.setScore(pipe.getScore() - 10);
						}
						if(enemies.get(i).getType() == 0){//simple enemy
							killSound();
							enemies.get(i).die();
							enemiesLeft--;
							pipe.setScore(pipe.getScore() + 10);
						}
						if(enemies.get(i).getType() == 2){// fire enemy
							killfireSound();
							enemies.get(i).die();
							enemiesLeft--;
							pipe.setScore(pipe.getScore() - 50);
						}
						if(enemies.get(i).getType() == 3){// bonus enemy
							killbonusSound();
							enemies.get(i).die();
							enemiesLeft--;
							pipe.setScore(pipe.getScore() + 50);
						}
					}
			}
//			if (enemies.get(i).getX() >= -20 && !enemies.get(i).isDead())
//				enemies.get(i).setX(
//						enemies.get(i).getX() - enemies.get(i).getSpeed());
//			else
//				onGameOver(i);
			if (!enemies.get(i).isDead())
			{
				enemies.get(i).setSpeed(5);// speed of the enemy can be directly changed from the basic enemy java file
				enemies.get(i).setX(
						enemies.get(i).getX() - enemies.get(i).getSpeed());
			}
			// to end game at starting od first, 20
			// to end the game at starting of 2nd , -50
			// difference is of 70
			if(enemies.get(i).getX() <= -14000)
				onGameOver(i);
		}
	}

	// Resets the values that are needed in order for the next level to begin
	// and performs actions to populate List etc and start the level
	private void nextLevel() {
		pipe.setLevelComplete(false);
		pipe.setNextLevel(false);
		if (lvl.hasNext(level))
			lvlStr = lvl.parser(++level);
		else
			gameOver();
		buildLevel();
		assignTextures();
		weapon.reset();
		setOnFire = false;
		pipe.setScore(0);
		hasLost = false;
	}

	// Holds the  actions that are going to be performed on each frame.
	// Calls the methods needed in order to draw the frames and handles what is going to
	// be drawn when the level is complete or the player loses.
	public void onDrawFrame(GL10 gl) {
		// Clear the screen
		gl.glClear(GL10.GL_COLOR_BUFFER_BIT | GL10.GL_DEPTH_BUFFER_BIT);
		gl.glPushMatrix();
		gl.glTranslatef(width / 2, height / 2, 0.0f);
		gl.glRotatef(90, 0.0f, 0.0f, 1.0f);
		bg.draw(gl);
		gl.glPopMatrix();

		if (weapon.ready())
			this.drawWeapon();
		else
			firstpoint = true;
		weaponOnFire();
		moveEnemies();
		gl.glPushMatrix();
		gl.glTranslatef(80.0f, height / 2, 0.0f);//height-2*height/3
		gl.glRotatef(90, 0.0f, 0.0f, 1.0f);
		gl.glRotatef(180, 1.0f, 0.0f, 0.0f);
		hero.draw(gl);
		gl.glPopMatrix();
		fire();
		if (enemiesLeft <= 0) {
			pipe.setLevelComplete(true);
			if (pipe.getNextLevel()) {
				nextLevel();
			} else {
				gl.glPushMatrix();
				gl.glTranslatef(width / 2, height / 2, 0.0f);
				gl.glRotatef(90, 0.0f, 0.0f, 1.0f);
				nextLvl.draw(gl);
				gl.glPopMatrix();
			}
		}
		if (hasLost){
			//GameOverSound();
			drawGameOverScreen();
		}

	}

	// Responsible to show the GameOver! comment
	private void onGameOver(int i) {
		if (!lost && !enemies.get(i).isDead()) {
			hasLost = true;
			pipe.setLevelComplete(true);
			if (pipe.getNextLevel()) {
				lost = true;
				gameOver();
			}
		}
	}

	// Actions performed when the surface changes.
	public void onSurfaceChanged(GL10 gl, int width, int height) {
		if (height == 0) {
			height = 1;
		}
		this.width = width;
		this.height = height;
		gl.glMatrixMode(GL10.GL_PROJECTION);
		gl.glViewport(0, 0, width, height);
		gl.glLoadIdentity();
		GLU.gluOrtho2D(gl, 0, width, height, 0);
	}

	// Actions to be performed when the surface is created.
	// It basically sets the projection, enebles OpenGL features such as
	// the Alpha value for transparency and assigns the textures.
	public void onSurfaceCreated(GL10 gl, EGLConfig config) {
		this.gl = gl;
		assignTextures();
		gl.glClearColor(0.0f, 0.0f, 0.0f, 1);
		gl.glHint(GL10.GL_PERSPECTIVE_CORRECTION_HINT, GL10.GL_FASTEST);
		gl.glShadeModel(GL10.GL_FLAT);
		gl.glDisable(GL10.GL_DEPTH_TEST);
		gl.glEnable(GL10.GL_BLEND);
		gl.glBlendFunc(GL10.GL_ONE, GL10.GL_ONE_MINUS_SRC_ALPHA);

		gl.glViewport(0, 0, width, height);
		gl.glMatrixMode(GL10.GL_PROJECTION);
		gl.glLoadIdentity();
		gl.glEnable(GL10.GL_BLEND);
		gl.glBlendFunc(GL10.GL_SRC_ALPHA, GL10.GL_ONE_MINUS_SRC_ALPHA);
		gl.glShadeModel(GL10.GL_FLAT);
		gl.glEnable(GL10.GL_TEXTURE_2D);

		GLU.gluOrtho2D(gl, 0, width, height, 0);
	}

	// Checks for collisions between the weapon and the fire and if they collide
	// it sets the weapon to be on fire, thus able to kill JumpingEnemies.
	private void weaponOnFire() {
		if (weapon.collidesWith(width / 3, height - height / 10)) {
			setOnFire = true;
		}
	}
}