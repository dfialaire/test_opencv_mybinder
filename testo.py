# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 21:38:43 2021

@author: dfial
"""

import cv2
import matplotlib
from matplotlib.pyplot import *

#########################################################
cam=cv2.VideoCapture(0);
while(True):
    ret,img=cam.read();
    cv2.imshow("En direct _ Video Webqqqqqqqqqqqcam", img);
    if(cv2.waitKey(1) ==ord("c")):
        capture=img
        
        imshow(capture)
        axis="off"
        show()
    if(cv2.waitKey(1) ==ord("q")):
        break;
cam.release()
cv2.destroyAllWindows()
imshow(capture)
axis="off"
show()