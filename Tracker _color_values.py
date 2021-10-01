
import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)   #always take care of this while using 3rd party camera.
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)                  #frame dimensions set

def empty(a):
    pass


cv2.namedWindow("HSV")                 #HSV window defined and sized
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)      #keeping the minimum values first
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)

cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)    #and maximum values later
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)