// This java code responsible for drawing fullscreen images ==========================================================
/**
 -> OpenGL(Open Graphic Library) is a cross-platform graphics API that specifies a standard software interface
 for 3D graphics processing hardware.
 -> GL10 is public interface that implements GL
 */
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

public class FullScreenImageDraw {
	private FloatBuffer vertexBuffer;// The buffer that holds the vertices of the square where the enemies are created
	private ByteBuffer indexBuffer;// The buffer that holds the indices for the texture
	private float vertices[];// The vertices of the square, in terms of (float x, float y, float z), 3 axis
	private FloatBuffer textureBuffer;// The buffer that holds the vertices of the texture
	private float texture[] = { 0.0f, 0.0f, 0.0f, 1.0f, 1.0f, 0.0f, 1.0f, 1.0f };// The vertices of the texture (pairs of 2)
	private int[] textures = new int[1];// An array to hold the textures to be used (1 in this occasion)
	private byte indices[] = { 0, 1, 3, 0, 3, 2, }; // An array that contains the indices

	private int img;// The image id

	// This function Creates the object according to the screen size, with parameter img, height, width
	public FullScreenImageDraw(int img, int height, int width) {
		this.img = img;
		float vert[] = { -height / 2, width / 2, 0.0f, height / 2, width / 2, 0.0f, -height / 2, -width / 2, 0.0f, height / 2, -width / 2, 0.0f };
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

	// This function draws the object and sets its properties, using parameter gl.
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

	// This function needed to load the texture and assign a texture to an object.
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

		// This fixes an issue that a line above the textures would appear on
		// Samsung Galaxy S
		gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_WRAP_S,
				GL10.GL_CLAMP_TO_EDGE);
		gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_WRAP_T,
				GL10.GL_CLAMP_TO_EDGE);

		GLUtils.texImage2D(GL10.GL_TEXTURE_2D, 0, bitmap, 0);

		// Clean up
		bitmap.recycle();
	}
}