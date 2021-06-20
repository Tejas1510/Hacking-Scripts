from PIL import Image, ImageFilter

path = input("Enter the path where the image is located:")

img = Image.open(path)

img = img.filter(ImageFilter.BoxBlur(8))

img.save("blurredimage.jpg")
img.show()
