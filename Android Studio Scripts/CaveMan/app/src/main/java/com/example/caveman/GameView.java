// This java code sets the Renderer that will control the scene of the OpenGL layer.

package com.example.caveman;

import android.content.Context;
import android.opengl.GLSurfaceView;
import android.os.Build;

import androidx.annotation.RequiresApi;

@RequiresApi(api = Build.VERSION_CODES.CUPCAKE)
public class GameView extends GLSurfaceView {

	// Object created for the Renderer of the game
	private GameRenderer gameRen;

	// sets the renderer by passing the argument context, height, width, level
	public GameView(Context context, int height, int width, int level) {
		super(context);
		gameRen = new GameRenderer(context, height, width, level);
		this.setRenderer(gameRen);
	}
}
