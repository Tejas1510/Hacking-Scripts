package com.example.android.guesswho;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private int chance = 4;
    private int iterate = 0;
    private int num;
    private EditText firstEditText;
    TextView tv3;
    Button submitBtn;
    Button resetBtn;
    String str;
    TextView tv4;
    int numCheck;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        num = (int) (100 * Math.random());

        firstEditText = (EditText) findViewById(R.id.firstEditText);
        tv3 = (TextView) findViewById(R.id.textView3);
        tv3.setText(Integer.toString(num));
        tv4 = (TextView) findViewById(R.id.textView4);

        submitBtn = (Button) findViewById(R.id.submitBtn);
        submitBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                try {
                     numCheck = Integer.parseInt(firstEditText.getText().toString());
                }
                catch(Exception e) {
                }

                if (num == numCheck || chance == iterate) {
                    if (chance == iterate) {
                        str = "***You lost***";
                        submitBtn.setEnabled(false);
                    } else
                        str = "***Bingo***";
                    Intent i = new Intent("com.example.SecondActivity");
                    i.putExtra("key1", str);
                    startActivity(i);
                }


                if (numCheck <= 100 && numCheck >= 0) {
                    iterate++;
                    if (num < numCheck) {
                        tv4.setText("Guess is larger.");
                    }
                    if (num > numCheck) {
                        tv4.setText("Guess is smaller.");
                    }
                } else {
                    tv4.setText("Invalid Option");
                }
            }
        });

        resetBtn = (Button) findViewById(R.id.resetBtn);
        resetBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                iterate = 0;
                firstEditText.getText().clear();
                submitBtn.setEnabled(true);
                num = (int) (100 * Math.random());
                tv3.setText(Integer.toString(num));
            }
        });


    }
}
