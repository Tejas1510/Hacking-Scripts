// This java code is basically to display the instruction of playing ==================================

package com.example.caveman;

import android.app.Activity;
import android.content.Intent;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.widget.MediaController;
import android.widget.ToggleButton;
import android.widget.VideoView;

public class HelpActivity extends Activity {
	// Creating Media Player to play any sound or music -------------------------------------------------------------
	private MediaPlayer mp;//Creates a new MediaPlayer to play any kind of sound
	private void clickSound() {// this function Plays a sound when a button is clicked.
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(getApplicationContext(), R.raw.music2);
		mp.start();
	}

	ToggleButton togglebutton;// a togglebutton variable
	
	// This method is called when the activity is first created.
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		//clickSound();
		setContentView(R.layout.help_layout);

		togglebutton = findViewById(R.id.toggle3);
		togglebutton.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				if(togglebutton.isChecked()){
					//Toast.makeText(OptionsActivity.this,"On", Toast.LENGTH_SHORT).show();
					mp = MediaPlayer.create(getApplicationContext(), R.raw.bstd);
					mp.start();
				}
				else{
					mp.stop();
					mp.release();
					//Toast.makeText(OptionsActivity.this,"Off", Toast.LENGTH_SHORT).show();
				}
			}
		});

		// Adding demo video in the help activity ---------------------------------------------------------
		VideoView videoView;//Initialize the variable
		videoView = findViewById(R.id.videoView);// Assigning the variable

		videoView.setVideoPath("android.resource://" + getPackageName() + "/" + R.raw.demo);
		MediaController mediaController = new MediaController(this);
		mediaController.setAnchorView(videoView);
		// set the mediacontroller with videoview object
		videoView.setMediaController(mediaController);

		//-------------------------------------------------------------------------------------------------

	}

	// This function handles the case when back key is pressed
	@Override
	public boolean onKeyDown(int keyCode, KeyEvent event) {
		if (keyCode == KeyEvent.KEYCODE_BACK) {
			Intent Menu = new Intent(HelpActivity.this, MainActivity.class);
			startActivity(Menu);
			finish();
//			mp.stop();// when backkey is pressed , the music stopped
//			mp.release();// and also music is released
			return true;
		}
		return super.onKeyDown(keyCode, event);
	}
}