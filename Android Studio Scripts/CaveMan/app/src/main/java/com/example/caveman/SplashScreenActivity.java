// This java code is responsible for what is going to be the first page of the game when someone opens it =================
package com.example.caveman;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.MotionEvent;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

public class SplashScreenActivity extends Activity {
	protected volatile boolean active = true;//Holds the state of the splash screen, wheteher its active or not
	protected boolean backKey = false;// boolean variable backKey to check if user hits the backbutton or not, if
										// if hit then we end the game there only
	protected final int TIMER = 10000;// TIMER variable decides means how long the splash screen will be visible
	private Thread splashThread;// The Thread in which the splash screen time is measured

	// Creating Media Player to play any sound or music -------------------------------------------------------------
	private MediaPlayer mp;//Creates a new MediaPlayer to play any kind of sound
	private void clickSound() {// this function Plays a sound when a button is clicked.
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(getApplicationContext(), R.raw.splash_background);
		//mp = MediaPlayer.create(getApplicationContext(), R.raw.splash_background_1);
		//mp = MediaPlayer.create(getApplicationContext(), R.raw.splash_background_2);
		mp.start();
	}

//	Button welcomebutton;
//	private void createwelcomeButtons() {
//		final Animation animation1 = AnimationUtils.loadAnimation(this, R.anim.clicked);
//
//		// for GameButton ----------------------
//		welcomebutton = (Button) findViewById(R.id.Welcome);
//		welcomebutton.startAnimation(AnimationUtils.loadAnimation(SplashScreenActivity.this, R.anim.blink));
//		welcomebutton.setOnClickListener(new View.OnClickListener() {
//			public void onClick(View v) {
//				clickSound();
//				welcomebutton.startAnimation(animation1);
//				animation1.setAnimationListener((Animation.AnimationListener) SplashScreenActivity.this);
//			}
//		});
//	}
	ImageView ImageWelcome;

	private void createwelcomeimage() {
		final Animation animation1 = AnimationUtils.loadAnimation(this, R.anim.clicked);

		ImageWelcome = (ImageView) findViewById(R.id.Welcome);
		ImageWelcome.startAnimation(AnimationUtils.loadAnimation(SplashScreenActivity.this, R.anim.blink));
	}

	//LinearLayout splashLayout;

	// This function is called when the activity is first created. ----------------------------------------------------
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.splash);
		//createwelcomeButtons();
		createwelcomeimage();

		//Toast.makeText(SplashScreenActivity.this,"Firebase Connection Success",Toast.LENGTH_LONG).show();
		clickSound();

//		Snackbar snackbar = Snackbar.make(splashLayout, "Welcome to AndroidHive", Snackbar.LENGTH_LONG);
//		snackbar.show();

		Toast toast;
		toast = Toast.makeText(getApplicationContext(),"\uD83D\uDE0E Welcome! to Cave Saviour Game",Toast.LENGTH_SHORT);
		//toast.setGravity(Gravity.CENTER_VERTICAL | Gravity.START,100,-220);
		TextView toastMessage = (TextView) toast.getView().findViewById(android.R.id.message);
		toastMessage.setTextSize(30);
		toastMessage.setTextColor(Color.RED);
		View view = toast.getView();
		view.setBackgroundColor(Color.BLACK);
		toast.show();

//		welcomebutton.setOnClickListener(new View.OnClickListener() {
//			@Override
//			public void onClick(View v) {
//				Toast toast;
//				toast = Toast.makeText(getApplicationContext(),"\uD83D\uDE0E Welcome! to Cave Saviour Game",Toast.LENGTH_SHORT);
//				//toast.setGravity(Gravity.CENTER_VERTICAL | Gravity.START,100,-220);
//				TextView toastMessage = (TextView) toast.getView().findViewById(android.R.id.message);
//				toastMessage.setTextSize(30);
//				toastMessage.setTextColor(Color.RED);
//				View view = toast.getView();
//				view.setBackgroundColor(Color.BLACK);
//				toast.show();
//			}
//		});
		// thread for displaying the splash screen
		splashThread = new Thread() {
			@Override
			public void run() {
				try {
					// could have just done sleep, but then hit screen to
					// continue to next Activity would not work.
					int time = 0;
					while (active && (time < TIMER)) {
						sleep(100);
						if (active) {
							time += 100;
						}
					}
				}
				catch (InterruptedException e) {
				}
				finally {
					finish();
					if (backKey == false) {
						clickSound();
						Intent intent = new Intent();
						// switch to the next screen/Activity
						intent.setClass(SplashScreenActivity.this,
								MainActivity.class);
						startActivity(intent);
					}
					interrupt();
				}
			}
		};
		splashThread.start();
	}

	// This function indicates what happens when the back and home buttons are pressed. --------------------------
	public boolean onKeyDown(int keyCode, KeyEvent event) {
		switch (keyCode) {
		case KeyEvent.KEYCODE_BACK:// case when backbutton is pressed
			this.splashThread.interrupt();
			backKey = true;
			finish();
			break;
		case KeyEvent.KEYCODE_HOME:// case when homebutton is pressed
			this.splashThread.interrupt();
			backKey = true;
			finish();
			break;
		}
		return super.onKeyDown(keyCode, event);
	}

	// The splash screen is visible for set time , but if user touches the splash screen, if goes off and menu button is showed
	@Override
	public boolean onTouchEvent(MotionEvent event) {
		if (event.getAction() == MotionEvent.ACTION_DOWN) {
			active = false;
		}
		return true;
	}
}