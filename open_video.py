import cv2

cap = cv2.VideoCapture('captured.MP4');

while(True):
    ret, frame  = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break;

cap.release();
cv2.destroyAllWindows();