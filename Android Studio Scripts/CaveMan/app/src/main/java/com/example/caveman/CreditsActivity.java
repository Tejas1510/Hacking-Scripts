// This java code is just for crediting part

package com.example.caveman;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ToggleButton;

import androidx.annotation.RequiresApi;

public class CreditsActivity extends Activity {
	// Creating Media Player to play any sound or music -------------------------------------------------------------
	private MediaPlayer mp;//Creates a new MediaPlayer to play any kind of sound
	private void clickSound() {// this function Plays a sound when a button is clicked.
		if (mp != null) {
			mp.release();
		}
		mp = MediaPlayer.create(getApplicationContext(), R.raw.music2);
		mp.start();// media player is started
	}

	//private ViewFlipper mFlipper;//A flipper to switch between the credits

	ToggleButton togglebutton;// a togglebutton variable
	Button goodbutton;
	Button badbutton;
	Button sharebutton;
	Button followbutton;
//	Button arrowbutton;
//	private void createarrowButtons() {
//		final Animation animation1 = AnimationUtils.loadAnimation(this, R.anim.clicked);
//
//		// for GameButton ----------------------
//		arrowbutton = (Button) findViewById(R.id.arrow_button);
//		arrowbutton.startAnimation(AnimationUtils.loadAnimation(CreditsActivity.this, R.anim.blink));
//		arrowbutton.setOnClickListener(new View.OnClickListener() {
//			public void onClick(View v) {
//				//clickSound();
//				arrowbutton.startAnimation(animation1);
//				animation1.setAnimationListener((Animation.AnimationListener) CreditsActivity.this);
//			}
//		});
//	}
	ImageView ImageArrow;

	private void createarrowimage() {
		final Animation animation1 = AnimationUtils.loadAnimation(this, R.anim.clicked);

		ImageArrow = (ImageView) findViewById(R.id.arrow_image);
		ImageArrow.startAnimation(AnimationUtils.loadAnimation(CreditsActivity.this, R.anim.blink));
	}

	// This function is called when the activity is first created. ----------------------------------------------------
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		//clickSound();
		setContentView(R.layout.credits_layout);// content of credits_layout.xml are set, on credits page
		//createarrowButtons();
		createarrowimage();
//		mFlipper = ((ViewFlipper) this.findViewById(R.id.flipper));
//		mFlipper.startFlipping();

		togglebutton = findViewById(R.id.toggle4);
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

//		arrowbutton.setOnClickListener(new View.OnClickListener() {
//			@Override
//			public void onClick(View v) {
//				Toast toast;
//				toast = Toast.makeText(getApplicationContext(),"\uD83D\uDE0E Follow and Share",Toast.LENGTH_SHORT);
//				TextView toastMessage = (TextView) toast.getView().findViewById(android.R.id.message);
//				toastMessage.setTextSize(30);
//				toastMessage.setTextColor(Color.RED);
//				View view = toast.getView();
//				view.setBackgroundColor(Color.BLACK);
//				toast.show();
//			}
//		});

//		TextView textView = (TextView)findViewById(R.id.textView);
//		textView.setMovementMethod(LinkMovementMethod.getInstance());
		followbutton = findViewById(R.id.follow_button);
		followbutton.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				String url = "https://github.com/akash435/Cave-Man-Game";

				Intent intent = new Intent(Intent.ACTION_VIEW);
				intent.setData(Uri.parse(url));
				startActivity(intent);
			}
		});

		goodbutton = findViewById(R.id.Good);
		goodbutton.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				Toast toast;
				toast = Toast.makeText(getApplicationContext(),"\uD83D\uDCCC Thanks for the Feedback. We are glad that you have positive experience with game.",Toast.LENGTH_SHORT);
				TextView toastMessage = (TextView) toast.getView().findViewById(android.R.id.message);
				toastMessage.setTextSize(30);
				toastMessage.setTextColor(Color.GREEN);
				View view = toast.getView();
				view.setBackgroundColor(Color.BLACK);
				toast.show();
			}
		});

		badbutton = findViewById(R.id.Bad);
		badbutton.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				Toast toast;
				toast = Toast.makeText(getApplicationContext(),"\uD83D\uDCCC Thanks for the Feedback. We are sorry that you are having problem with game, Please give detailed feedback on Play Store review.",Toast.LENGTH_SHORT);
				TextView toastMessage = (TextView) toast.getView().findViewById(android.R.id.message);
				toastMessage.setTextSize(30);
				toastMessage.setTextColor(Color.GREEN);
				View view = toast.getView();
				view.setBackgroundColor(Color.BLACK);
				toast.show();
			}
		});

		sharebutton = findViewById(R.id.share_button);
		sharebutton.setOnClickListener(new View.OnClickListener() {
			@RequiresApi(api = Build.VERSION_CODES.DONUT)
			@Override
			public void onClick(View v) {
//				Intent intent = new Intent(Intent.ACTION_SEND);
//				intent.setType("text/plain");
//				String title = "Game";
//				String text = "Cave Saviour";
//				intent.putExtra(Intent.EXTRA_TITLE,title);
//				intent.putExtra(Intent.EXTRA_TEXT,text);
//				startActivity(intent.createChooser(intent,"Share Using"));

//				Intent intent = new Intent(Intent.ACTION_SEND);
//				intent.setType("text/plain");
//				String title = "Game";
//				String link = "https://github.com/akash435/Cave-Man-Game";
//				intent.putExtra(Intent.EXTRA_TITLE,title);
//				intent.putExtra(Intent.EXTRA_TEXT,link);
//				startActivity(intent.createChooser(intent,"Share Using"));

				// In this code we need to type the recipient name
//				Intent intent = new Intent(Intent.ACTION_SEND);
//				intent.setType("message/rfc822");  //set the email recipient
//				String recipient = getString(R.string.IntegralEmailAddress);
//				String subject = "Hello from CaveMan";
//				intent.putExtra(Intent.EXTRA_EMAIL , recipient);
//				intent.putExtra(Intent.EXTRA_SUBJECT, subject);// subject of mail will be subject
//				//let the user choose what email client to use
//				startActivity(Intent.createChooser(intent, "Send mail using..."));

				// recipient name is already there from code
//				Intent intent = new Intent(Intent.ACTION_SEND);
//				intent.setType("text/email");
//				intent.putExtra(Intent.EXTRA_EMAIL, new String[] { "aakashrajak02@gmail.com" });
//				intent.putExtra(Intent.EXTRA_SUBJECT, "Feedback");
//				startActivity(Intent.createChooser(intent, "Send mail to Developer:"));

				// in this only those app will be shown which support email, but we have to enter receiver email
//				Intent intent = new Intent(Intent.ACTION_SENDTO);
//				//intent.setType("text/email");
//				intent.setData(Uri.parse("mailto:"));// this is used to display only those app of email
//				intent.putExtra(Intent.EXTRA_SUBJECT,"My Subject");
//				startActivity(Intent.createChooser(intent, "Send mail to Developer:"));

				// shared base.apk but not able to install in mobile
//				ApplicationInfo app = getApplicationContext().getApplicationInfo();
//				String filePath = app.publicSourceDir;
//				Intent sharingIntent = new Intent(Intent.ACTION_SEND);
//				Uri uri = Uri.parse(filePath);
//				sharingIntent.setType("*/*");
//				sharingIntent.putExtra(Intent.EXTRA_STREAM, uri);
//				sharingIntent.putExtra(Intent.EXTRA_TEXT, "Click to blue link and download thegame. https://drive.google.com/open?id=10Nc5BoYn4NZ_O8ae32UVQwyzdCzFxNy");
//				startActivity(Intent.createChooser(sharingIntent, "Share app using"));

				Intent intent = new Intent(Intent.ACTION_SEND);
				intent.setType("text/plain");
				String title = "Game";
				String link = "Check out My First game (Cave Saviour) through APK with this drive link :- https://drive.google.com/file/d/1CeeDM6h7yz_ax1W4ojN7OdFF5B2GYnvI/view?usp=sharing";
				intent.putExtra(Intent.EXTRA_TITLE,title);
				intent.putExtra(Intent.EXTRA_TEXT,link);
				startActivity(intent.createChooser(intent,"Share Using"));
			}
		});

	}

	// When the back key is pressed, this Activity finishes and the menu button are visible to us
	@Override
	public boolean onKeyDown(int keyCode, KeyEvent event) {
		if (keyCode == KeyEvent.KEYCODE_BACK) {
			Intent Menu = new Intent(CreditsActivity.this, MainActivity.class);
			startActivity(Menu);
			finish();
//			mp.stop();// when backkey is pressed , the music stopped
//			mp.release();// and also music is released
			return true;
		}
		return super.onKeyDown(keyCode, event);
	}
}