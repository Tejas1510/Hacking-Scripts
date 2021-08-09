# Snapchat Filters

**GOAL:**
We will build our own Snapchat Filters with the help of some libraries using Python programming language.

**DATASET:**
No dataset available. Instead we will be using images of our choice.

**WHAT I HAD DONE:**

I have created a project for making our own snapchat filters. 
First I am reading the required images for snapchat filters and then getting the coordinates for different parts of faces present in the image.

Then drawing a rectangle using X , Y axes and then displaying the face with a boundary box.

After that we are getting the proper coordinates for eyes using the height (h) and width (w) with the help of x1, y1, x2, y2 coordinates to fit our sunglasses.

And then using the for loop we are superimposing the image with the help of 3 channels (RGB) and finally displaying the snapchat filtered image.

**MODELS USED:**

We are not using any traditional model for performing this task.

**LIBRARIES NEEDED:**
- MTCNN
- Numpy
- OpenCV
- Matplotlib

**WORKING:**

To start using this project, follow the below guidelines: 

**1.**  Fork this project/repository. 🍴

**2.**  Clone your forked copy of the project/repository.

```
git clone https://github.com/<your-github-username>/Hacking-Scripts.git
```

**3.** Navigate to the project directory :file_folder: 

```
cd Hacking-Scripts/Python/Snapchat Filters/
```

**4.** Install the `requirements.txt` using command 🔧

```
pip install -r requirements.txt
```

**5.** Run `snapchat_filters.ipynb` file in Google Colab or Jupyter Notebook or any other platform 💻
