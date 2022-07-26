from copyreg import pickle
import socket
import struct
import cv2
import pickle

host = '192.168.0.103'
port = 5000

camera = True

if camera == True:
    cap = cv2.VideoCapture()
    cap.open(0,cv2.CAP_DSHOW)
    if not cap.isOpened():
        camera = False
        print('Camera is not working...')

cs = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
cs.connect((host,port))

if cs:
    while(cap.isOpened()):
        img , frame = cap.read()
        # frame = imutils.resize(frame,width = 380)
        a = pickle.dumps(frame)

        msg = struct.pack("Q",len(a))+a
        cs.sendall(msg)

        cv2.imshow(f"To : {host}",frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 'q':
            cs.close()
        print('VIDEO FINISHED...')
        break

