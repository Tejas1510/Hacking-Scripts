// This java code is responsible to ask the user to select the level from 1 to 6 ======================================

package com.example.caveman;

import android.app.Activity;
import android.content.Intent;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageButton;

public class LevelSelect extends Activity {
	private Intent Game;// Creates a new Intent object
	private Bundle bundle;// Creates a new Bundle object
	private ImageButton[] btns;// Creates an array to hold the buttons

	// Creating Media Player to play any sound or music -------------------------------------------------------------
	private MediaPlayer mp;//Creates a new MediaPlayer to play any kind of sound
	private void clickSound() {// this function Plays a sound when a button is clicked.
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(getApplicationContext(), R.raw.click);
		mp.start();
	}

	// Fills an array with ImageButtons and copies that to the btns array.
	// This is done because the btns array can not be filled otherwise without throuing exceptions.
	private void buttons() {
		ImageButton[] buttons = {
				(ImageButton) findViewById(R.id.imageButton1),
				(ImageButton) findViewById(R.id.imageButton2),
				(ImageButton) findViewById(R.id.imageButton3),
				(ImageButton) findViewById(R.id.imageButton4),
				(ImageButton) findViewById(R.id.imageButton5),
				(ImageButton) findViewById(R.id.imageButton6) };
		btns = buttons;
	}

	// Recieves the button that was clicked and calls the method that starts the corresponding level.
	private void levelSelection() {
		bundle = new Bundle();
		for (int i = 0; i < btns.length; i++)
			btns[i].setOnClickListener(new OnClickListener() {
				public void onClick(View v) {
					clickSound();
					ImageButton clickedButton = (ImageButton) v;

					switch (clickedButton.getId()) {
					case R.id.imageButton1:
						bundle.putString("level", "1");
						startLevel();
						break;

					case R.id.imageButton2:
						bundle.putString("level", "2");
						startLevel();
						break;

					case R.id.imageButton3:
						bundle.putString("level", "3");
						startLevel();
						break;

					case R.id.imageButton4:
						bundle.putString("level", "4");
						startLevel();
						break;

					case R.id.imageButton5:
						bundle.putString("level", "5");
						startLevel();
						break;

					case R.id.imageButton6:
						bundle.putString("level", "6");
						startLevel();
						break;
					}
				}
			});
	}

	// This function is called when the activity is first created.
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.level_select_layout);
		buttons();
		levelSelection();
	}

	// this function handles the condition when user presses the back button
	@Override
	public boolean onKeyDown(int keyCode, KeyEvent event) {
		if (keyCode == KeyEvent.KEYCODE_BACK) {
			Intent Menu = new Intent(LevelSelect.this, MainActivity.class);
			startActivity(Menu);
			finish();
			return true;
		}
		return super.onKeyDown(keyCode, event);
	}

	// This method sends to the GameActivity the information stating which level it should be and
	// then it finishes the current Activity (LevelSelect)
	private void startLevel() {
		Game = new Intent(LevelSelect.this, GameActivity.class);
		Game.putExtras(bundle);
		startActivity(Game);
		finish();
	}

}