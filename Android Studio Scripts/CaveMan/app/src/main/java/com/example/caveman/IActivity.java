package com.example.caveman;

import android.app.Activity;
import android.content.Intent;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.widget.ToggleButton;

public class IActivity extends Activity {

    // Creating Media Player to play any sound or music -------------------------------------------------------------
    private MediaPlayer mp;//Creates a new MediaPlayer to play any kind of sound
    private void clickSound() {// this function Plays a sound when a button is clicked.
        if (mp != null) {
            mp.release();
        }
        mp = MediaPlayer.create(getApplicationContext(), R.raw.music2);
        mp.start();// media player is started
    }

    ToggleButton togglebutton;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.i_layout);

        togglebutton = findViewById(R.id.toggle5);
        togglebutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(togglebutton.isChecked()){
                    //Toast.makeText(OptionsActivity.this,"On", Toast.LENGTH_SHORT).show();
                    mp = MediaPlayer.create(getApplicationContext(), R.raw.bstd);
                    mp.start();
                }
                else{
                    mp.stop();// when backkey is pressed , the music stopped
                    mp.release();// and also music is released
                    //Toast.makeText(OptionsActivity.this,"Off", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    // When the back key is pressed, this Activity finishes and the menu button are visible to us
    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if (keyCode == KeyEvent.KEYCODE_BACK) {
            Intent Menu = new Intent(IActivity.this, MainActivity.class);
            startActivity(Menu);
            finish();
//			mp.stop();// when backkey is pressed , the music stopped
//			mp.release();// and also music is released
            return true;
        }
        return super.onKeyDown(keyCode, event);
    }
}
