// This java code creates rectangles loads textures for small icons like enemies, hero, fire, etc

package com.example.caveman;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.opengl.GLUtils;

import java.io.IOException;
import java.io.InputStream;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.FloatBuffer;

import javax.microedition.khronos.opengles.GL10;

public class TextureLoader {

	// The buffer that holds the vertices of the square that the enemy lives
	private FloatBuffer vertexBuffer;
	// The buffer that holds the indices for the texture
	private ByteBuffer indexBuffer;
	// The vertices of the square in terms of x,y,z, axes
	private float vertices[];
	// The buffer that holds the vertices of the texture
	private FloatBuffer textureBuffer;
	// The vertices of the texture (pairs of 2)
	private float texture[] = { 0.0f, 0.0f, 0.0f, 1.0f, 1.0f, 0.0f, 1.0f, 1.0f };
	// An array to hold the textures to be used, 1 in this case
	private int[] textures = new int[1];
	// An array that contains the indices
	private byte indices[] = { 0, 1, 3, 0, 3, 2, };
	// The image id
	private int img;

	// Creates an object according to image and screen height
	public TextureLoader(int img, int height) {
		this.img = img;
		// here we have considered the height of each icon as height.10
		float vert[] = { -height / 20, -height / 20, 0.0f, height / 20,-height / 20, 0.0f, -height / 20, height / 20, 0.0f, height / 20, height / 20, 0.0f };

		vertices = vert;

		ByteBuffer byteBuffer = ByteBuffer.allocateDirect(vertices.length * 4);
		byteBuffer.order(ByteOrder.nativeOrder());
		vertexBuffer = byteBuffer.asFloatBuffer();
		vertexBuffer.put(vertices);
		vertexBuffer.position(0);

		// create a byte buffer with the UV coordinates
		byteBuffer = ByteBuffer.allocateDirect(texture.length * 4);
		byteBuffer.order(ByteOrder.nativeOrder());
		textureBuffer = byteBuffer.asFloatBuffer();
		textureBuffer.put(texture);
		textureBuffer.position(0);

		indexBuffer = ByteBuffer.allocateDirect(indices.length);
		indexBuffer.put(indices);
		indexBuffer.position(0);
	}

	// Draw method, responsible for drawing the object and setting its properties.
	public void draw(GL10 gl) {

		gl.glEnable(GL10.GL_BLEND);
		gl.glBlendFunc(GL10.GL_ONE, GL10.GL_ONE_MINUS_SRC_ALPHA);
		// Bind the texture according to the set texture filter
		gl.glBindTexture(GL10.GL_TEXTURE_2D, textures[0]);

		// Enable the vertex, texture and normal state
		gl.glEnableClientState(GL10.GL_VERTEX_ARRAY);
		gl.glEnableClientState(GL10.GL_TEXTURE_COORD_ARRAY);
		gl.glEnableClientState(GL10.GL_NORMAL_ARRAY);

		// Set the face rotation
		gl.glFrontFace(GL10.GL_CCW);

		// Point to our buffers
		gl.glVertexPointer(3, GL10.GL_FLOAT, 0, vertexBuffer);
		gl.glTexCoordPointer(2, GL10.GL_FLOAT, 0, textureBuffer);

		// Draw the vertices as triangles, based on the Index Buffer information
		gl.glDrawElements(GL10.GL_TRIANGLES, indices.length,
				GL10.GL_UNSIGNED_BYTE, indexBuffer);

		// Disable the client state before leaving
		gl.glDisableClientState(GL10.GL_VERTEX_ARRAY);
		gl.glDisableClientState(GL10.GL_TEXTURE_COORD_ARRAY);
		gl.glDisableClientState(GL10.GL_NORMAL_ARRAY);
	}

	// The method needed to load the texture and assign a texture to an object.
	public void textureLoader(GL10 gl, Context context) {
		// Get the texture from the Android resource directory
		InputStream is = context.getResources().openRawResource(img);
		Bitmap bitmap = null;
		try {
			// BitmapFactory is an Android graphics utility for images
			bitmap = BitmapFactory.decodeStream(is);
		} finally {
			// Always clear and close
			try {
				is.close();
				is = null;
			} catch (IOException e) {
			}
		}
		// Generate there texture pointer
		gl.glGenTextures(1, textures, 0);

		// Create Nearest Filtered Texture and bind it to texture 0
		gl.glBindTexture(GL10.GL_TEXTURE_2D, textures[0]);
		// Setting min/mag to linear to solve issue with waving texture
		gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_MAG_FILTER,
				GL10.GL_LINEAR);
		gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_MIN_FILTER,
				GL10.GL_LINEAR);

		gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_WRAP_S,
				GL10.GL_CLAMP_TO_EDGE);
		gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_WRAP_T,
				GL10.GL_CLAMP_TO_EDGE);

		GLUtils.texImage2D(GL10.GL_TEXTURE_2D, 0, bitmap, 0);

		// Clean up
		bitmap.recycle();
	}
}
