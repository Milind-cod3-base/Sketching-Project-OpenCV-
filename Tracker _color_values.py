#This file is to keep the track of the colours in track bar

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
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)      #Minimum value of Hue
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)      #Minimum value of Saturation
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)    #Minimum value of Value

cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)    #Maximum value of Hue
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)    #Maximum value of saturation
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)  #Maximum value of value

while True:
    success, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)        #Webcam input converted to HSV format

    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")     #Minimum and maximum saturation value
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    print(h_min)

    lower = np.array( [h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)           #mask created
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack( [img, mask, result])              #horizontal stacking done using numpy
    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()