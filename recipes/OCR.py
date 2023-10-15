import os

import pytesseract

from pytesseract import Output

from PIL import Image

import numpy as np

from recipes.models import BookPage



def perform_ocr(file_path):

    if os.path.isfile(file_path):

        myconfig = r"--psm 3 --oem 1"

        # Read the image using PIL

        img = Image.open(file_path)

        # Convert the image to grayscale

        gray_img = img.convert('L')

        # Invert the grayscale image

        inverted_img = Image.eval(gray_img, lambda x: 255 - x)

        # Perform OCR on the inverted image

        ocr_text = pytesseract.image_to_string(inverted_img, config=myconfig)

        return ocr_text

    else:

        return "File does not exist."



"""

file_path = "C:/Users/Username/Desktop/Books/Pecan Cookery/Pecan_Cookery_4.png"

ocr_result = perform_ocr(file_path)

print(ocr_result)


"""

