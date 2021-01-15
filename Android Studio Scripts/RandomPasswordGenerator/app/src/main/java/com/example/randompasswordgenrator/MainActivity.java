package com.example.randompasswordgenrator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.util.Random;

public class MainActivity extends AppCompatActivity {
 TextView mainDisplayMessage,genratedPassword;
 EditText inputLength;
 private String password;
 Button btGenrate;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mainDisplayMessage=findViewById(R.id.displaymessage);
        inputLength=findViewById(R.id.length);
        genratedPassword=findViewById(R.id.genratedpassword);
        btGenrate=findViewById(R.id.genratebutton);
        btGenrate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String k=inputLength.getText().toString();
                int kl=Integer.parseInt(k);
                password=generatePassword(kl);
                genratedPassword.setText(password);
              genratedPassword.setVisibility(View.VISIBLE);

            }
        });


    }
    public static String generatePassword(int len) {
        //String containing alphanumeric characters i.e [a-z and A-Z and 0-9]
        String str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        //Random class to generate random idex value of the alphanumeric string
        Random random = new Random();
        //StringBuilder is used to append the random alphanumeric characters
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<len;i++) {
            sb.append(str.charAt(random.nextInt(str.length())));
        }
        //Converting StringBuilder to String and returning the randomly generated password
        return sb.toString();
    }
}