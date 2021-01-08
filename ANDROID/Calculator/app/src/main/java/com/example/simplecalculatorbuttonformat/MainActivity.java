package com.example.simplecalculatorbuttonformat;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import static android.icu.lang.UCharacter.GraphemeClusterBreak.V;

public class MainActivity extends AppCompatActivity {

    private TextView input;
    private TextView sign;
    private Button b1;
    private Button b2;
    private Button b3;
    private Button b4;
    private Button b5;
    private Button b6;
    private Button b7;
    private Button b8;
    private Button b9;
    private Button b0;
    private Button bdot;
    private Button badd;
    private Button bsubs;
    private Button bmul;
    private Button bdiv;
    private Button bmod;
    private Button bclear;
    private Button bdel;
    private Button bequal;
    private Double val1,val2,Result;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        input=(TextView)findViewById(R.id.tv1);
        sign=(TextView)findViewById(R.id.tv2);
        b1=(Button)findViewById(R.id.b1);
        b2=(Button)findViewById(R.id.b2);
        b3=(Button)findViewById(R.id.b3);
        b4=(Button)findViewById(R.id.b4);
        b5=(Button)findViewById(R.id.b5);
        b6=(Button)findViewById(R.id.b6);
        b7=(Button)findViewById(R.id.b7);
        b8=(Button)findViewById(R.id.b8);
        b9=(Button)findViewById(R.id.b9);
        b0=(Button)findViewById(R.id.b0);
        badd=(Button)findViewById(R.id.badd);
        bsubs=(Button)findViewById(R.id.bsub);
        bmul=(Button)findViewById(R.id.bmult);
        bdiv=(Button)findViewById(R.id.bdiv);
        bmod=(Button)findViewById(R.id.bmod);
        bdot=(Button)findViewById(R.id.bdot);
        bequal=(Button)findViewById(R.id.bequal);
        bdel=(Button)findViewById(R.id.bdel);
        bclear=(Button)findViewById(R.id.bce);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText(input.getText()+"1");
            }
        });
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText(input.getText()+"2");
            }
        });
        b3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText(input.getText()+"3");
            }
        });
        b4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText(input.getText()+"4");
            }
        });
        b5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText(input.getText()+"5");
            }
        });
        b6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText(input.getText()+"6");
            }
        });
        b7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText(input.getText()+"7");
            }
        });
        b8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText(input.getText()+"8");
            }
        });
        b9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText(input.getText()+"9");
            }
        });
        b0.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText(input.getText()+"0");
            }
        });
        bdot.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if((input.getText().toString()).equals(""))
                input.setText(input.getText()+"0.");
                else
                    input.setText(input.getText()+".");
            }
        });
        bclear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText("");
            }
        });
        bdel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText(input.getText().toString().substring(0,(input.getText().toString()).length()-1));
            }
        });


        badd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               if(input.getText().toString().isEmpty()) {
                   sign.setText("+");
                   Toast.makeText(getApplicationContext(), "Enter value", Toast.LENGTH_SHORT).show();
                   sign.setText("");
               }
               else
               {
                   val1=Double.parseDouble(input.getText().toString());
                   sign.setText("+");
                   input.setText("");

                   bequal.setOnClickListener(new View.OnClickListener() {
                       @Override
                       public void onClick(View v) {

                   val2=Double.parseDouble(input.getText().toString());
                   Result=val1+val2;
                   input.setText(val1+"+"+val2+"="+Result);
                   sign.setText("");
                       }
                   });
               }
            }
        });

        bsubs.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if((input.getText().toString()).equals("")) {
                    sign.setText("-");
                    Toast.makeText(getApplicationContext(), "Enter value", Toast.LENGTH_SHORT).show();
                    sign.setText("");
                }
                else
                {
                    val1=Double.parseDouble(input.getText().toString());
                    sign.setText("-");
                    input.setText("");
                    bequal.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {

                            val2=Double.parseDouble(input.getText().toString());
                            Result=val1-val2;
                            input.setText(val1+"-"+val2+"="+Result);
                            sign.setText("");
                        }
                    });
                }
            }
        });

        bmul.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if((input.getText().toString()).equals("")) {
                    sign.setText("X");
                    Toast.makeText(getApplicationContext(), "Enter value", Toast.LENGTH_SHORT).show();
                    sign.setText("");
                }
                else
                {
                    val1=Double.parseDouble(input.getText().toString());
                    sign.setText("X");
                    input.setText("");
                    bequal.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {

                            val2=Double.parseDouble(input.getText().toString());
                            Result=val1*val2;
                            input.setText(val1+"x"+val2+"="+Result);
                            sign.setText("");
                        }
                    });
                }
            }
        });

        bdiv.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if((input.getText().toString()).equals("")) {
                    sign.setText("÷");
                    Toast.makeText(getApplicationContext(), "Enter value", Toast.LENGTH_SHORT).show();
                    sign.setText("");
                }
                else
                {
                    val1=Double.parseDouble(input.getText().toString());
                    sign.setText("÷");
                    input.setText("");
                    bequal.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {

                            val2=Double.parseDouble(input.getText().toString());
                            Result=val1/val2;
                            input.setText(val1+"÷"+val2+"="+Result);
                            sign.setText("");
                        }
                    });
                }
            }
        });

        bmod.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if((input.getText().toString()).equals("")) {
                    sign.setText("%");
                    Toast.makeText(getApplicationContext(), "Enter value", Toast.LENGTH_SHORT).show();
                    sign.setText("");
                }
                else
                {
                    val1=Double.parseDouble(input.getText().toString());
                    sign.setText("%");
                    input.setText("");
                    bequal.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {

                            val2=Double.parseDouble(input.getText().toString());
                            Result=val1%val2;
                            input.setText(val1+"%"+val2+"="+Result);
                            sign.setText("");
                        }
                    });
                }
            }
        });
    }
}
