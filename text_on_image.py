import cv2

imagePath = "./pytho/gall.png";

image = cv2.imread(imagePath);

text = "opencv tutoraial";
cordinates = (100,100);
font = cv2.FONT_HERSHEY_SIMPLEX;
fontScale = 1;
color = (255,0,0);
thickness = 2;

image = cv2.putText(image,text,cordinates,font,fontScale,color,thickness);

cv2.imshow("image",image);

cv2.waitKey(0);
cv2.destroyAllWindows();