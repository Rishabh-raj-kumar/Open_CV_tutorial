import cv2

imagePath = "./pytho/gall.png";

image = cv2.imread(imagePath);

cv2.imshow("image",image);

resized = cv2.resize(image,(600,300));
cv2.imshow("resized",resized);

cv2.waitKey(0);
cv2.destroyAllWindows();