import cv2

image = cv2.imread('./pytho/gall.png');

#splitting RGB values of image.
r, g, b = cv2.split(image);

#showing green part of the image.
cv2.imshow('Green part of image : ',g);

#showing blue part of the image.
cv2.imshow('Blue part of image : ',b);

#showing red part of the image.
cv2.imshow('Red part of image : ',r);

#now merging the splitted image...
img = cv2.merge((r,g,b));
cv2.imshow("image",img);

cv2.waitKey(0)