// This java code responsible for buiding the game acitivity ============================================================

package com.example.caveman;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.graphics.Paint;
import android.media.AudioManager;
import android.media.MediaPlayer;
import android.os.Build;
import android.os.Bundle;
import android.view.Display;
import android.view.KeyEvent;
import android.view.View;
import android.view.ViewGroup.LayoutParams;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.RequiresApi;

public class GameActivity extends Activity {
	private com.example.caveman.UserInteract userInter;// The Canvas layer of the game
	private com.example.caveman.GameView surface;// The OpenGL ES layer of the game
	private Bundle extras;// A bundle to pass data from an Activity to a View
	private String level = "1";// the default level is taken as 1, if user doed not select any level
	private int score = 0;

	//---------------------------------------------------------------------------------------------------------------------------------------------
	/** Creates a new Pipe object */
	private com.example.caveman.Pipe pipe;

	private Paint paint = new Paint();
	//---------------------------------------------------------------------------------------------------------------------------------------------

	// Creating Media Player to play any sound or music -------------------------------------------------------------
	private MediaPlayer mp;//Creates a new MediaPlayer to play any kind of sound
	private void clickSound() {// this function Plays a sound when a button is clicked.
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(getApplicationContext(), R.raw.music11);
		mp.start();
	}

//	@RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
//	public static int getRandomValue(int Min, int Max)
//	{
//
//		// Get and return the random integer
//		// within Min and Max
//		return ThreadLocalRandom.current().nextInt(Min, Max + 1);
//	}

	// This function called when the activity is first created. -----------------------------------------------------
	// Creates the layers, passes the level value and basically starts the game.
	@RequiresApi(api = Build.VERSION_CODES.CUPCAKE)
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setVolumeControlStream(AudioManager.STREAM_MUSIC);
		// Get the height and width of the display
		Display display = getWindowManager().getDefaultDisplay();
		int width = display.getWidth();
		int height = display.getHeight();
		clickSound();// this is called to start playing music
		userInter = new com.example.caveman.UserInteract(this);
		userInter.initActions();
		extras = this.getIntent().getExtras();
		level = extras.getString("level");
		score = extras.getInt("score");//----------------------- not working -----------------------------------------------
		surface = new com.example.caveman.GameView(this, height, width, Integer.parseInt(level));
		setContentView(surface);
		addContentView(userInter, new LayoutParams(LayoutParams.FILL_PARENT,
				LayoutParams.FILL_PARENT));

		// toast message to show which level selected
		Toast toast;
		toast = Toast.makeText(getApplicationContext(),level,Toast.LENGTH_SHORT);
		TextView toastMessage = (TextView) toast.getView().findViewById(android.R.id.message);
		toastMessage.setTextSize(200);
		toastMessage.setTextColor(Color.YELLOW);
		View view = toast.getView();
		view.setBackgroundColor(Color.TRANSPARENT);
		toast.show();

		//------------------------------------------------------------------------------------------

		//int score = getRandomValue(0,200);
//		if(score>0 && score<=10)
//			score = 10;
//		else if(score<=20)
//			score = 20;
//		else if(score<=30)
//			score = 30;
//		else if(score<=40)
//			score = 40;
//		else if(score<=50)
//			score = 50;
//		else if(score<=60)
//			score = 60;
//		else if(score<=70)
//			score = 70;
//		else if(score<=80)
//			score = 80;
//		else if(score<=90)
//			score = 90;
//		else if(score<=100)
//			score = 100;
//		else if(score<=110)
//			score = 110;
//		else if(score<=120)
//			score = 120;
//		else if(score<=130)
//			score = 130;
//		else if(score<=140)
//			score = 140;
//		else if(score<=150)
//			score = 150;
//		else if(score<=160)
//			score = 160;
//		else if(score<=170)
//			score = 170;
//		else if(score<=180)
//			score = 180;
//		else if(score<=190)
//			score = 190;
//		else if(score<=200)
//			score = 200;

//		String status;
//		if(score<60)
//			status = "LOSE";
//		else
//			status = "WIN";

		PlayerModel playerModel;
		try{
			playerModel = new PlayerModel(-1,Integer.parseInt(level),score);
			//Toast.makeText(GameActivity.this,"Data inserted",Toast.LENGTH_SHORT).show();// toast message is shown on screen
		}
		catch(Exception e){
			// if this fails
			Toast.makeText(GameActivity.this,"Error",Toast.LENGTH_SHORT).show();
			playerModel = new PlayerModel(-1,-1, -1);
		}

		ScoreDB scoredb = new ScoreDB(GameActivity.this);
		boolean success = scoredb.addOne(playerModel);
		//Toast.makeText(GameActivity.this,"Data Inserted = " + success,Toast.LENGTH_SHORT).show();

		//------------------------------------------------------------------------------------------

	}

	// This function handles the occasion that this Activity finishes ---------------------------------------------
	@Override
	protected void onDestroy() {
		super.onDestroy();
		userInter.onBackButton();
	}

	// This function handles the occasion when backbutton is pressed ---------------------------------
	@RequiresApi(api = Build.VERSION_CODES.CUPCAKE)
	@Override
	public boolean onKeyDown(int keyCode, KeyEvent event) {
		if (keyCode == KeyEvent.KEYCODE_BACK) {
			//Intent Menu = new Intent(GameActivity.this, LevelSelect.class);//on backkey , takes us to levelselect page
			 Intent Menu = new Intent(GameActivity.this, MainActivity.class);// on backkey , takes us to mainActivity page
			// clear the pipe, as it is static and may not clear itself
			userInter.onBackButton();
			// by calling the following I free up some memory and I avoid program crashes
			surface.destroyDrawingCache();
			surface.clearFocus();
			userInter.destroyDrawingCache();
			userInter.clearFocus();
			surface.onPause();
			startActivity(Menu);
			finish();

			mp.stop();
			mp.release();
			return true;
		}
		return super.onKeyDown(keyCode, event);
	}

	// This function handles the occasion that the game pauses for some reason ------------------------------
	@RequiresApi(api = Build.VERSION_CODES.CUPCAKE)
	@Override
	protected void onPause() {
		super.onPause();
		surface.onPause();
	}

	// this function handles the occasion that the game resumes after pausing. ----------------------------------
	@RequiresApi(api = Build.VERSION_CODES.CUPCAKE)
	@Override
	protected void onResume() {
		super.onResume();
		surface.onResume();
	}

}