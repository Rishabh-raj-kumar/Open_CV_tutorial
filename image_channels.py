import cv2

img_path = "./pytho/gall.png";

RGB_image = cv2.imread(img_path,1);
Alpha_image = cv2.imread(img_path,-1);
Gray_image = cv2.imread(img_path,0);

# cv2.imshow("image",Alpha_image);

# # cv2.waitKey(0);
# # cv2.destroyAllWindows()

# 0 -> gray (which has no channels)
# 1 -> color (which has three channels)
# -1 -> (which has 4 channels)

print("colored Image shape : ",RGB_image.shape);
print(" Image Data type : ",RGB_image.dtype);

print("Alpha Color Shape : ",Alpha_image.shape);
print("Gray Image Shape :  ",Gray_image.shape);