// This java code draws and handles the menu of the game. =======================================================

package com.example.caveman;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.media.AudioManager;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.animation.Animation;
import android.view.animation.Animation.AnimationListener;
import android.view.animation.AnimationUtils;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends Activity implements AnimationListener {
	// Creating button for menu of the game ------------------------------------------------------------------------
	private Button GameButton;//Creates a new GameButton
	private Button OptionsButton;//Creates a new OptionsButton
	private Button HighscoresButton;//Creates a new HighscoresButton
	private Button HelpButton;//Creates a new HelpButton
	private Button CreditsButton;//Creates a new CreditsButton
	private Button IButton;//Creates a new IButton
	Button ClickButton;
	ImageView ImageArrow1;

	private void createarrowimage1() {
		final Animation animation1 = AnimationUtils.loadAnimation(this, R.anim.clicked);

		ImageArrow1 = (ImageView) findViewById(R.id.arrow_image1);
		ImageArrow1.startAnimation(AnimationUtils.loadAnimation(MainActivity.this, R.anim.blink));
	}

	// Creating Media Player to play any sound or music -------------------------------------------------------------
	private MediaPlayer mp;//Creates a new MediaPlayer to play any kind of sound
	private void clickSound() {// this function Plays a sound when a button is clicked.
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(getApplicationContext(), R.raw.click);
		mp.start();
	}

	// Boolean Array of size 5 is created to check if button is selected or not
	private final boolean[] selected = new boolean[6];

	// CreateMenuButtons() function, creates an short animation when a particular menu button is selected ------------------
	private void createMenuButtons() {
		final Animation animation1 = AnimationUtils.loadAnimation(this, R.anim.clicked);

		// for GameButton ----------------------
		GameButton = (Button) findViewById(R.id.Game);
		GameButton.startAnimation(AnimationUtils.loadAnimation(MainActivity.this, R.anim.slide_down));
		GameButton.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				clickSound();
				selected[0] = true;
				GameButton.startAnimation(animation1);
				animation1.setAnimationListener(MainActivity.this);
			}
		});

		// for OptionsButton ----------------------
		OptionsButton = (Button) findViewById(R.id.Options);
		OptionsButton.startAnimation(AnimationUtils.loadAnimation(
				MainActivity.this, R.anim.slide_down));
		OptionsButton.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				clickSound();
				selected[1] = true;
				OptionsButton.startAnimation(animation1);
				animation1.setAnimationListener(MainActivity.this);
			}
		});

		// for iButton ----------------------
		IButton = (Button) findViewById(R.id.i_about);
		IButton.startAnimation(AnimationUtils.loadAnimation(
				MainActivity.this, R.anim.slide_down));
		IButton.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				clickSound();
				selected[2] = true;
				IButton.startAnimation(animation1);
				animation1.setAnimationListener(MainActivity.this);
			}
		});

		// for HelpButton ----------------------
		HelpButton = (Button) findViewById(R.id.Help);
		HelpButton.startAnimation(AnimationUtils.loadAnimation(
				MainActivity.this, R.anim.slide_down));
		HelpButton.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				clickSound();
				selected[3] = true;
				HelpButton.startAnimation(animation1);
				animation1.setAnimationListener(MainActivity.this);
			}
		});

		// for CreditsButton ----------------------
		CreditsButton = (Button) findViewById(R.id.Credits);
		CreditsButton.startAnimation(AnimationUtils.loadAnimation(
				MainActivity.this, R.anim.slide_down));
		CreditsButton.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				clickSound();
				selected[4] = true;
				CreditsButton.startAnimation(animation1);
				animation1.setAnimationListener(MainActivity.this);
			}
		});

//		// for HighscoresButton ----------------------
//		HighscoresButton = (Button) findViewById(R.id.Highscores);
//		HighscoresButton.startAnimation(AnimationUtils.loadAnimation(
//				MainActivity.this, R.anim.slide_down));
//		HighscoresButton.setOnClickListener(new OnClickListener() {
//			public void onClick(View v) {
//				clickSound();
//				selected[5] = true;
//				HighscoresButton.startAnimation(animation1);
//				animation1.setAnimationListener(MainActivity.this);
//			}
//		});

	}

	//this functions are used for animation part only ---------------------------------------------------------
	public void onAnimationEnd(Animation animation) {
		switchView();
		finish();
	}
	public void onAnimationRepeat(Animation animation) {

	}
	public void onAnimationStart(Animation animation) {

	}

	// This function is called when the activity is first created. ----------------------------------------------------
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.menu_layout);
		setVolumeControlStream(AudioManager.STREAM_MUSIC);

		createarrowimage1();

		ClickButton = findViewById(R.id.click_button);
		ClickButton.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				Toast toast;
				toast = Toast.makeText(getApplicationContext(),"\uD83D\uDCCC Head over to HELP button to see how to play game.",Toast.LENGTH_SHORT);
				TextView toastMessage = (TextView) toast.getView().findViewById(android.R.id.message);
				toastMessage.setTextSize(30);
				toastMessage.setTextColor(Color.GREEN);
				View view = toast.getView();
				view.setBackgroundColor(Color.BLACK);
				toast.show();
			}
		});

		for (int i = 0; i < 6; i++)
			selected[i] = false;// we here initialize all the boolean array element as false, indicating initially not selected
		createMenuButtons();// then createMenuButtons() function is called
	}

	// This function handles the case when the user hits the back button, the application ends. ---------------------
	@Override
	public boolean onKeyDown(int keyCode, KeyEvent event) {
		if (keyCode == KeyEvent.KEYCODE_BACK) {
			finish();
			return true;
		}
		return super.onKeyDown(keyCode, event);
	}

	// This function detects the button that was clicked and redirects the user to the corresponding Activity.
	private void switchView() {
		for (int i = 0; i < 6; i++) {
			if (selected[i] == true) {// we change the selected[i] from false to true
				switch (i) {
				case 0:// case 0 - for GameButton
					Intent Game = new Intent(MainActivity.this,
							com.example.caveman.LevelSelect.class);
					startActivity(Game);
					break;
				case 1:// Case 1 - for OptionsButton
					Intent Options = new Intent(MainActivity.this,
							com.example.caveman.OptionsActivity.class);
					startActivity(Options);
					break;
				case 2:// Case 2 - for aboutButton
					Intent Iact = new Intent(MainActivity.this,
							com.example.caveman.IActivity.class);
					startActivity(Iact);
					break;
				case 3:// Case 3 - for HelpsButton
					Intent Help = new Intent(MainActivity.this,
							com.example.caveman.HelpActivity.class);
					startActivity(Help);
					break;
				case 4:// case 4 - for Creditsbutton
					Intent Credits = new Intent(MainActivity.this,
							com.example.caveman.CreditsActivity.class);
					startActivity(Credits);
					break;
				case 5:// case 5 - for Highsocresbutton
					Intent Highscores = new Intent(MainActivity.this,
							com.example.caveman.HighscoresActivity.class);
					startActivity(Highscores);
					break;
				}
			}
			selected[i] = false;
		}
	}
}