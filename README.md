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

```

