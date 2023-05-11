import cv2

abc = cv2.VideoCapture(0);
#since we are dealing with videos...

#we need a loop to handle the frames...
while(True):
     red_,frame = abc.read()
     cv2.imshow("video",frame)

      #you can pass any variable in ord..
      #logic is that if you press v button your video will end.
     if(cv2.waitKey(1) & 0xff == ord('v')):
          break;
          #to release the space taken from video coz it takes lot.
          abc.release()

cv2.destroyAllWindows()