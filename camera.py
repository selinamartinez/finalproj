import cv2
#import pickle
#import io 
#import time
#import zlib



def capture():
	HIGH_VALUE = 10000
	WIDTH = HIGH_VALUE
	HEIGHT = HIGH_VALUE

	cam = cv2.VideoCapture(0)

	# This gives maximum resolution of any device camera (slow for video)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	cam.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
	cam.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

	# This gives small frame size (faster)
	#cam.set(3, 320);
	#cam.set(4, 240);



	# JPEG quality from 0 to 100, with 100 being best (95 is default)
	encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100] 

	# Adjust camera lighting
	ramp_frames = 30
	for i in range(ramp_frames):
		temp = cam.read()
	# Capture image 
	ret, frame = cam.read()
	#result, frame = cv2.imencode('.jpg', frame, encode_param)
	#data = zlib.compress(pickle.dumps(frame, 0))
	#data = pickle.dumps(frame, 0)
	#return data

	cv2.imwrite('image.jpg', frame)






#cv2.namedWindow("Preview")
#cap = cv2.VideoCapture(0)

#rval, frame = cap.read()

#cv2.imshow('Preview', frame)

# time for which image displayed
#cv2.waitKey(3000)

#name = input("Enter file name: ")

# Save the frame
#cv2.imwrite(name + '.jpg', frame)

