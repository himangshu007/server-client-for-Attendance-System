import cv2

cap = cv2.VideoCapture()
cap.open(0,cv2.CAP_DSHOW) 
if cap.isOpened():
    print('Camera is working')

while True:
    ret , frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)& 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 




