import cv2

reader = cv2.imread('gall.png');

cv2.imshow("image",reader);

cv2.waitKey(0);
cv2.destroyAllWindows();

#saving an image

file = "hello.png";
cv2.imwrite(file,reader);
print("image saved success")

#how many number of pixels in  image.
print(reader.shape)
#it will give output in (Rows,Columns,Channels) format example -> (220,150,5);