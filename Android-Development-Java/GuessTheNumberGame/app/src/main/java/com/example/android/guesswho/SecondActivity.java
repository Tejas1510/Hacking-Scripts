package com.example.android.guesswho;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class SecondActivity extends AppCompatActivity {

    Button button2;
    TextView tv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        button2 = (Button) findViewById(R.id.button2);
        button2.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                startActivity(new Intent(SecondActivity.this , MainActivity.class));
            }
        });

        if(getIntent().hasExtra("key1")){
            tv = (TextView)findViewById(R.id.textView);
            String text = getIntent().getExtras().getString("key1");
            tv.setText(text);
        }
    }
}
