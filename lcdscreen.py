import sys
import time
from colorfinder import colorName

# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import*

def LCDcontrol(RGB, hexadecimal):
    try:
        color = colorName(hexadecimal)
        setRGB(RGB[0],RGB[1],RGB[2])
        setText_norefresh("Hex: #" + hexadecimal + "    "+ "\n" + color + "        ")
    except(IOError, TypeError) as e:
        print("Error")

       
