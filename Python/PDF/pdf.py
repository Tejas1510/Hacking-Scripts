# Import necessary libraries:
import fitz
import io
from PIL import Image

# open the desired PDF file:
pdf = fitz.open("demo.pdf") # pdf file that contains the images
# Determine number of pages in the PDF file:
pages = len(pdf)
# Iterate over each of the PDF pages:
# Index of 1st page -> 0
for i in range(pages):
    # Access the page at index 'i':
    page = pdf[i]

    # Access all image objects present in this page:
    image_list = page.getImageList()

    # Iterate through these image objects:
    for image_count, img in enumerate(image_list, start=1):
        
        # Access XREF of the image:
        xref = img[0]
        
        # Extract image information:
        img_info = pdf.extractImage(xref)
        
        # Extract image bytes:
        image_bytes = img_info["image"]
        
        # Access image extension:
        image_ext = img_info["ext"]
        
        # Load this image to PIL:
        image = Image.open(io.BytesIO(image_bytes))
        
        # To save this image:
        image.save(open(f"page{i+1}_image{image_count}.{image_ext}", "wb"))
