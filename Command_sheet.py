import os

import pytesseract

from pytesseract import Output

import cv2

import PIL.Image

import numpy as np

from PIL import Image

import subprocess




# Replace 'your_folder_path' with the path to the folder you want to iterate over

folder_path = "C:\\Users\\calca\\Desktop\\Books\\60 min chef"



# Ensure the folder path exists

if os.path.exists(folder_path) and os.path.isdir(folder_path):

    # List all files in the folder

    files = os.listdir(folder_path)

    files.sort()



    for file_name in files:

        if os.path.isfile(os.path.join(folder_path, file_name)):

            file_path = os.path.join(folder_path, file_name)



            myconfig = r"--psm 3 --oem 1"



            img = cv2.imread(file_path)



            # Increase contrast

            alpha = 3  # Contrast control (1.0 means no change, < 1.0 decreases contrast, > 1.0 increases contrast)

            beta = 0    # Brightness control (0 means no change, positive values increase brightness, negative values decrease brightness)



            img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)



            # Convert the image to grayscale

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



            # Invert the grayscale image

            inverted_img = cv2.bitwise_not(gray_img)



            # Define a kernel for dilation

            kernel = np.ones((5, 5), np.uint8)



            # Perform image dilation to make dark regions thicker

            dilated_img = cv2.dilate(inverted_img, kernel, iterations=1)



            # Invert the dilated image back to the original polarity

            dilated_img = cv2.bitwise_not(dilated_img)



            # Convert the dilated image back to BGR format

            dilated_bgr_img = cv2.cvtColor(dilated_img, cv2.COLOR_GRAY2BGR)



            desired_width = 900  # Set the desired width for the resized image

            img = Image.fromarray(dilated_bgr_img)  # Convert OpenCV dilated image to PIL format

            img.thumbnail((desired_width, desired_width))  # Resize the image while maintaining the aspect ratio



            # Convert the resized PIL image back to OpenCV format

            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)



            data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

            print(data['text'])



            amount_boxes = len(data['text'])

            for i in range(amount_boxes):

                if float(data['conf'][i]) > 80:

                    (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])

                    img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 1)

                    img = cv2.putText(img, data['text'][i], (x, y + height + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,

                                     (0, 255, 0), 1, cv2.LINE_AA)



            cv2.imshow("img", img)

            cv2.waitKey(0)



            print(file_path)

else:

    print("The specified folder does not exist or is not a directory.")