from copyreg import pickle
import socket
import struct
import threading
import pyshine as ps
import cv2

host = '192.168.0.103'
port = 5000
socket_addr = (host,port)

# ss = server socket , cs = client socket
ss = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ss.bind((host,port))
ss.listen(0)
print('Listening at: ',socket_addr)

def show_client(addr,cs):
    try:
        print(f'Client {addr} connected...')
        if cs:
            data = b""
            payload_size = struct.calcsize('Q')
            print(f'Payload size : {payload_size}')
            while True:
                while len(data)<payload_size:
                    packet = cs.recv(4*1024)
                    if not packet:
                        break
                    data += packet
                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                
                msg_size = struct.unpack('Q',packed_msg_size)  
                while len(data)<msg_size:
                    data += cs.recv(4*1024)
                frame_data = data[:msg_size]
                data = data[msg_size:]
                frame = pickle.loads(frame_data)
                text = f'Client: {addr}'
                frame = ps.putBText(frame , text, 10 ,10 , vspace = 10 , hspace = 1 , 
                                    font_scale = 0.7 , background_RGB =(255,0,0),text_RBG =(255,250,250))
                key = cv2.waitKey(1) &0xFF
                if key == ord('q'):
                    break
            cs.close()
            
    except Exception as e:
        print(f'CLient {addr} disconnected...')
        pass

while True: 
    cs , addr = ss.accept()
    thread = threading.Thread(target = show_client(addr, cs))
    thread.start()
    print("Total Clients ",threading.activeCount()-1)