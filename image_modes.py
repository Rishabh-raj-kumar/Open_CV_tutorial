# 0 -> gray color
# 1 -> color image

import cv2 

path = "./pytho/gall.png"

image =  cv2.imread(path,0)

cv2.imshow("image",image);

cv2.waitKey(0);
cv2.destroyAllWindows();