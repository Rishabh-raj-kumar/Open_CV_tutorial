# access pixel values -> [210, 187, 169]

# access only blue pixel -> 169
# modify the pixel -> [255, 255, 255]

import numpy as np
import cv2

img = cv2.imread('./pytho/gall.png');
#ok you can test by passing several rows and column values.
px = img[127,67];
#it will print RGB value of that specified row and column.
print(px);
#accessing RGB r -> 0, g -> 1, b -> 2 place these value in third.
blue = img[127,67,2];
print(blue);

#changing color values
img[100,100] = [255,244,233];
print(img[100,100]);