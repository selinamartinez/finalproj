import cv2
import io
import socket
import struct
import time
import pickle
import zlib


try:
    #create socket with arguments AF_INET (Address Family Internet) and SOCK_STREAM (TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket created")
except socket.error: # generic socket exception/error
    print("Failed to create socket.")
    sys.exit()

client_socket.connect(('172.20.10.9', 8485)) # Raspberry Pi IP Address 
connection = client_socket.makefile('wb')


HIGH_VALUE = 10000
WIDTH = HIGH_VALUE
HEIGHT = HIGH_VALUE

cam = cv2.VideoCapture(0)

# This gives maximum resolution of any device camera (slow)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

# This gives small frame size (faster)
#cam.set(3, 320);
#cam.set(4, 240);


img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)


    print("{}: {}".format(img_counter, size))
    client_socket.sendall(struct.pack(">L", size) + data)
    img_counter += 1

cam.release()