import cv2

image_path = "./pytho/gall.png";

image = cv2.imread(image_path);


gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY);

cv2.imshow("image",image);
cv2.imshow("gray",gray);

cv2.waitKey(0);
cv2.destroyAllWindows();