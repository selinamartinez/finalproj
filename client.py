import socket
import sys
import pickle
from RGBtoHex import hexadecimal
from lcdscreen import LCDcontrol
from mosaic_tiles import createPhotomosaic

try:
    #create socket with arguments AF_INET (Address Family Internet) and SOCK_STREAM (TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket created")
except socket.error: # generic socket exception/error
    print("Failed to create socket.")
    sys.exit()

client_socket.connect(('172.20.10.2', 6666)) # Macbook IP Address 

request = b"PHOTO"

try:
	client_socket.sendall(request)
except socket.error:
	print("Failed to send.")
	sys.exit()

data = pickle.loads(client_socket.recv(4096))
data = data[0]
image = data[1]
hexa = hexadecimal(data)
print("RGB: ("  + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ") = Hexadecimal: #" + hexa)
print("turning photo into a photomosaic...")

LCDcontrol(data, hexa)
createPhotomosaic(image)


client_socket.close()