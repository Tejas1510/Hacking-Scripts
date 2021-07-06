from PIL import Image

def blackAndWhite():
    img = Image.open(r"C:\Users\pc\Desktop\Hacking-Scripts\Python\Black and White\Images\img.jpg")
    BlackAndwhite = img.convert("L")
    BlackAndwhite.save(r"C:\Users\pc\Desktop\Hacking-Scripts\Python\Black and White\Images\bw_img.jpg")

if __name__ == '__main__':
    blackAndWhite()
        