# HISTOGRAM

In an image processing context, the histogram of an image normally refers to a histogram of the pixel intensity values. This histogram is a graph showing the number of pixels in an image at each different intensity value found in that image.


## Library info

| Library | Description | represent |
| ------- | ------------| --------- |
| numpy   |NumPy can be used to perform a wide variety of mathematical operations on arrays.| import numpy as np
| Opencv  | OpenCV is a great tool for image processing and performing computer vision tasks. | import cv2 as cv
| matplotlib | Matplotlib in Python is an excellent tool for data visualization because it provides an easy way to view and interpret data. | from matplotlib import pyplot as plt 




## Links
[link numpy](https://www.geeksforgeeks.org/introduction-to-numpy/)

[link opencv](https://www.geeksforgeeks.org/opencv-python-tutorial/)

[link histogram](https://en.wikipedia.org/wiki/Image_histogram)

## Input image
![dogs](https://github.com/rekhahabshipuram/rekha/assets/169051921/64506632-e004-47b9-ad39-1b2d2c471860)



## code

Inline `code`
`histogram of an image`
`Indented code`

```
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt....
```
```
img = cv.imread('/home/rekha-habshipuram/Downloads/scripts/dogs.jpeg')
cv.imwrite("/home/rekha-habshipuram/Downloads/graph.jpeg",img)...
```

assert img is not None, "file could not be read, check with os.path.exists()"

**color** = ('b','g','r')

**for** i,col in enumerate(color):

 histr = cv.calcHist([img],[i],None,[256],[0,256])
 
 plt.plot(histr,color = col)
 
 plt.xlim([0,256])
 
plt.show()

## Output image
![Screenshot from 2024-05-08 11-27-25](https://github.com/rekhahabshipuram/rekha/assets/169051921/b9520acb-58f0-4f81-858f-b118c212a837)


# BOUDING BOX
 rectangular outline drawn around an object or a region of interest within an image
 
 ![643d3093b12eb54ce86904d3_624ef34](https://github.com/rekhahabshipuram/rekha/assets/169051921/9486a901-fa3c-40fb-b145-ecc0dd079181)

## Libraries

**import os**

import os manages all of the other application programs in a computer.

**pillow**

#pip install pillow


**import csv**

The so-called CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases.

## Input image
![7622202030987_f306535d741c9148dc458acbbc887243_L_487](https://github.com/rekhahabshipuram/rekha/assets/169051921/e52d351a-5742-4a97-8200-b380f8ac2acb)


## Links
[link functions](https://www.geeksforgeeks.org/python-functions/)


# Code

import os

import csv

from PIL import Image, ImageDraw


csv_file = "/home/rekha-habshipuram/Downloads/7622202030987_bounding_box.csv"

image_dir = "/home/rekha-habshipuram/Downloads/7622202030987"

output_dir = "/home/rekha-habshipuram/Downloads/7622202030987_with_boxes"


os.makedirs(output_dir, exist_ok=True)


def draw_boxes(image, boxes):

    draw = ImageDraw.Draw(image)
    for box in boxes:
        left = int(box['left'])
        top = int(box['top'])
        right = int(box['right'])
        bottom = int(box['bottom'])
        draw.rectangle([left, top, right, bottom], outline="red")
    return image


def crop_image(image, boxes):

    cropped_images = []
    for box in boxes:
        left = int(box['left'])
        top = int(box['top'])
        right = int(box['right'])
        bottom = int(box['bottom'])
        cropped_img = image.crop((left, top, right, bottom))
        cropped_images.append(cropped_img)
    return cropped_images

   ![full_7622202030987_f306535d741c9148dc458acbbc887243_L_487](https://github.com/rekhahabshipuram/rekha/assets/169051921/91d8055c-d15f-4c65-9d5c-d503900679d5) 


with open(csv_file, 'r') as file:

    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        image_name = row['filename']
        image_path = os.path.join(image_dir, image_name)
        output_path = os.path.join(output_dir, image_name)
        image = Image.open(image_path)
        boxes = [{'left': row['xmin'], 'top': row['ymin'], 'right': row['xmax'], 'bottom': row['ymax']}]
        cropped_images = crop_image(image, boxes)
        for i, cropped_img in enumerate(cropped_images):
            cropped_img.save(os.path.join(output_dir, f"{i}_{image_name}"))  
        full_image_with_boxes = draw_boxes(image, boxes)
        full_image_with_boxes.save(os.path.join(output_dir, f"full_{image_name}"))
        ```
        
        
## Output Image
![0_7622202030987_f306535d741c9148dc458acbbc887243_L_487](https://github.com/rekhahabshipuram/rekha/assets/169051921/e7fa11ec-6ee7-46f5-8c4c-34b3905dddce)
        

# ITERATION

The process of doing something again and again, usually to improve it, or one of the times you do it

**Example**
![Iteration-Maths-practice-question-1](https://github.com/rekhahabshipuram/rekha/assets/169051921/5ab53fbc-1543-47b8-b100-907febb88dd0)

## Links
[link list](https://www.w3schools.com/python/python_lists.asp)



## code

num = list(range(10))

previousNum = 0

for i in num:

    sum = previousNum + i
    print('Current Number '+ str(i) + 'Previous Number ' + str(previousNum) + 'is ' + str(sum))
    previousNum=i
    
## output 

![Screenshot from 2024-05-08 13-28-23](https://github.com/rekhahabshipuram/rekha/assets/169051921/a91cb5ba-6627-47d1-9c15-2fa486965365)

# WEBCAM

+ A webcam is a digital camera that captures video and audio data and transmits it in real-time over the internet. It is commonly used for video conferencing, live streaming, online meetings, and recording videos.

## Libraries

 **Opencv**
 
+ OpenCV is a huge open-source library for computer vision, machine learning, and image processing. 
+ OpenCV is a great tool for image processing and performing computer vision tasks. It is an open-source library that can be used to perform tasks like face detection, objection tracking.
+ import cv2

## Installation
$ pip install opencv


## code

#import the opencv library 

import cv2

#Open the webcam

cap = cv2.VideoCapture(0)

#Define the codec and create a VideoWriter object

fourcc = cv2.VideoWriter_fourcc(*'XVID')

#Specify the full path where you want to save the video

output_path = '/home/rekha-habshipuram/Documents/kushi/output.avi'

out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

while True:

    # Capture frame-by-frame
    
    ret, frame = cap.read()
    
    if not ret:
    
        break

    # Write the frame to the output video
    
    out.write(frame)

    # Display the resulting frame
    
    cv2.imshow('frame', frame)

    # Exit if 'q' is pressed
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
    
        break

#Release everything when done

cap.release()

out.release()

cv2.destroyAllWindows()

## Output video
https://github.com/rekhahabshipuram/rekha/assets/169051921/fdbf6573-ec11-4a8f-8c7a-e2429191b09b
