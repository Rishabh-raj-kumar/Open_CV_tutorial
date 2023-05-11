import cv2

image = cv2.imread('./pytho/gall.png');

#you can select a region of interest (ROI) on image.
roi = cv2.selectROI(image);
print(roi);

#now cropping and saving the image.
roi_cropped = image[int(roi[1]):(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])];
#first we will see the cropped image
cv2.imshow("ROI image : ",roi_cropped);
#saving the cropped Image.
cv2.imwrite("./pytho/cropped.png",roi_cropped);

cv2.waitKey(0);
cv2.destroyAllWindows();