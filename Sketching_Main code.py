import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)   #for instant access & display using external USB webcam
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)   #brightness


def findColor(img):              # a function is defined to find color
    imgHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("img", mask)               #to display the mask

while True:
    success, img = cap.read()
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):           #exit frame if pressed q
        break