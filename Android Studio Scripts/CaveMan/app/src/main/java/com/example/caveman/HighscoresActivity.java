// This java code uses the database and stored the scores of each level and display the highscore ============================

package com.example.caveman;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.ToggleButton;

import java.util.List;

public class HighscoresActivity extends Activity {
	// Creating Media Player to play any sound or music -------------------------------------------------------------
	private MediaPlayer mp;//Creates a new MediaPlayer to play any kind of sound
	private void clickSound() {// this function Plays a sound when a button is clicked.
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(getApplicationContext(), R.raw.music2);
		mp.start();
	}

	/** Creates a new Pipe object */
	private com.example.caveman.Pipe pipe;

	ToggleButton togglebutton;

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		ListView lv_playerList;

		super.onCreate(savedInstanceState);
		setContentView(R.layout.highscores_layout);
		//clickSound();

		lv_playerList = findViewById(R.id.lv_playerList);
		//------------------------------------------------------------------------------------------------------------------------------------

		ScoreDB scoredb = new ScoreDB(HighscoresActivity.this);
		List<PlayerModel> everyone =  scoredb.getEveryone();

		// we create here an arrayadapter
		ArrayAdapter playerArrayAdapter = new ArrayAdapter<PlayerModel>(HighscoresActivity.this, android.R.layout.simple_list_item_1,everyone){
			@Override
			public View getView(int position, View convertView, ViewGroup parent) {
				View view =super.getView(position, convertView, parent);

				TextView textView=(TextView) view.findViewById(android.R.id.text1);

				/*YOUR CHOICE OF COLOR*/
				textView.setTextColor(Color.YELLOW);

				return view;
			}
		};
		lv_playerList.setAdapter(playerArrayAdapter);

		togglebutton = findViewById(R.id.toggle2);
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



		//Toast.makeText(HighscoresActivity.this,everyone.toString(), Toast.LENGTH_SHORT).show(); // this will display in toast message format
		// but we would like to display in scrollable list


//		lv_playerList.setOnItemClickListener(new AdapterView.OnItemClickListener() {
//			@Override
//			public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
//				PlayerModel clickedPlayer = (PlayerModel) parent.getItemAtPosition(position);
//				scoredb.deleteOne(clickedPlayer);
//
//				ArrayAdapter playerArrayAdapter = new ArrayAdapter<PlayerModel>(HighscoresActivity.this, android.R.layout.simple_list_item_1,everyone);
//				lv_playerList.setAdapter(playerArrayAdapter);
//
//				Toast.makeText(HighscoresActivity.this,"Deleted = " + clickedPlayer.toString(),Toast.LENGTH_SHORT).show();
//			}
//		});
		//-------------------------------------------------------------------------------------------------------------------------------------
	}

	// This function handles the case when back key is pressed
	@Override
	public boolean onKeyDown(int keyCode, KeyEvent event) {
		if (keyCode == KeyEvent.KEYCODE_BACK) {
			Intent Menu = new Intent(HighscoresActivity.this,
					MainActivity.class);
			startActivity(Menu);
			finish();
//			mp.stop();// when backkey is pressed , the music stopped
//			mp.release();// and also music is released
			return true;
		}

		return super.onKeyDown(keyCode, event);
	}
}
