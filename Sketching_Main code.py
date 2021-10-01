import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)   #for instant access & display using external USB webcam
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)   #brightness

myColors= [[0,107,147,35,187.255],[133,56,0,159,156,255],[57,76,0,100,255,255]]
#three objects of different colours are masked using Tracker_color_values.py



def findColor(img, myColors):              #new argument added in the function

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for color in myColors:                #this will loop through all colored objects' HSV
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow("img", mask)

while True:
    success, img = cap.read()
    findColor(img,myColors)      #function is called
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):           #exit frame if pressed q
        break