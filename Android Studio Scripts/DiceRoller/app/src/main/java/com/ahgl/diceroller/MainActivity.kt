package com.ahgl.diceroller


import android.annotation.SuppressLint
import android.graphics.drawable.AnimatedImageDrawable
import android.graphics.drawable.AnimationDrawable
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.animation.AnimationUtils
import android.widget.Button
import android.widget.ImageView
import android.widget.LinearLayout
import android.os.Handler;
import android.os.Message
//AHGL
import kotlinx.android.synthetic.main.activity_main.*
import java.util.*



class MainActivity: AppCompatActivity() {
    @SuppressLint("ResourceType")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        rollBtn.setOnClickListener {
            val random = Random()
            val randomNo = random.nextInt(7)
            var imgResId = R.drawable.one
            when(randomNo){
                1 -> imgResId = R.drawable.one
                2 -> imgResId = R.drawable.two
                3 -> imgResId = R.drawable.three
                4 -> imgResId = R.drawable.four
                5 -> imgResId = R.drawable.five
                6 -> imgResId = R.drawable.six
            }
            val resId = imgResId
                dice.setImageResource(resId)
            }
       dice.setOnClickListener {
                    val random = Random()
                    val randomNo = random.nextInt(7)
                    //AHGL
                    var imgResId = R.drawable.one
                    when(randomNo){
                        1 -> imgResId = R.drawable.one
                        2 -> imgResId = R.drawable.two
                        3 -> imgResId = R.drawable.three
                        4 -> imgResId = R.drawable.four
                        5 -> imgResId = R.drawable.five
                        6 -> imgResId = R.drawable.six
                    }
                    val resId = imgResId
                        dice.setImageResource(resId)
                    }
        }
    }