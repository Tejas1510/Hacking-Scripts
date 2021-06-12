# Face Detection using OpenCV in Python

### Introduction:
In this project, a webcam is used to detect the face, if the face is detected a rectangular box is drawn around it.

In this project, OpenCV and HaarCascade algorithms are used to detect the face in the webcam. HaarCascade is a machine learning approach in which a cascade function is trained with the set of input data. There are many cascade classifiers in OpenCV for faces, eyes, smiles, etc.

For this project, 'haarcascade_frontal_face_default.xml' is used to detect the face in the webcam video frame which is available in the OpenCV Github repository.

### Requirements:

1) OpenCV
<br>
	```pip install opencv-python```


### Methodology
1) Import cv2.

2) Load the cascade classifier i.e 'haarcascade_frontal_face_default.xml'.

3) Capture the video frame from the webcam.

4) Inside an infinite loop read each frame and convert them into grayscale.

5) Detect the face in the frame using the cascade classifier.

6) Draw a rectangular box around the face that is detected by the classifier.

7) Display the frame.

8) Stop the infinite loop and closing the webcam by pressing the escape key.
