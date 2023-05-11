import cv2

cap =  cv2.VideoCapture(0);

#check wether camera is able to be opened or not..
if(cap.isOpened() == False):
    print('camera could not open');

#so basically we are setting the resolution and converting from
#  float to integer.
frame_width = int(cap.get(3));
frame_height = int(cap.get(4));

#video coders .. encoders and decoder...
video_cod = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#generated video                                     30 -> fps
video_output = cv2.VideoWriter('./pytho/captured.MP4', video_cod, 30,(frame_width,frame_height));

while(True):
    ret, frame = cap.read()

    if(ret == True):
        video_output.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xff == ord('h'):
            break
    else:
        break;

cap.release()
video_output.release()
cv2.destroyAllWindows()
print('video captured successs');




