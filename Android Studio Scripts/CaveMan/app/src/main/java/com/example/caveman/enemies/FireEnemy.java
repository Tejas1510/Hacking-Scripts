// This java code helps us to create simple enemies ================================

package com.example.caveman.enemies;

import com.example.caveman.R;

public class FireEnemy extends BasicEnemy {

    // Sends to the superclass the icon to be drawn, the height of the display and a number that
    // indicates that this is a SimpleEnemy.
    public FireEnemy(int height) {
        super(R.drawable.fire_enemy, height, 2);
    }

}
