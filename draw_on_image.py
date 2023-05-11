import cv2

imagePath = "./pytho/gall.png";

image = cv2.imread(imagePath);

#code for a simple line in image...
# color = (255,220,180);
# thickness = 5;
# start_points =  (100,100);
# end_points = (250,250);

# image = cv2.line(image,start_points,end_points,color,thickness);

#points for a circle...
# color = (255,220,180);
# thickness =5;
# radius = 20;
# center_cordinates = (120,70);

# image = cv2.circle(image,center_cordinates,radius,color,thickness);

#points for rectangle...
color = (255,220,180);
thickness = 5;
start_points =  (100,100);
end_points = (250,250);

image = cv2.rectangle(image,start_points,end_points,color,thickness);

cv2.imshow("originl Image",image);

cv2.waitKey(0);
cv2.destroyAllWindows();