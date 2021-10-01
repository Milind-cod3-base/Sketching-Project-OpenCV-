
import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)   #always take care of this while using 3rd party camera.
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)                  #frame dimensions set

