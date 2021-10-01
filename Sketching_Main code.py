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
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),10,(255,0,0),cv2.FILLED)  #There will be a cirlce at the top.


def getContours(img):    #function copied from Contour_function.py
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)      #image and retrievel method, we are using external method. RETR_EXTERNAL retrieves the extreme outer contours #next we have approximations: where we can request either all info or we can get compressed value, hence reduced value. Here I am asking for all values.

    x,y,w,h =  0,0,0,0   #if area < 500, it still needs to return somthing.

    for cnt in contours:
        area = cv2.contourArea(cnt)    #gets the area of those contours


        #now I need to give minimum threshold area so that it doesnt detect any noise
        if area>500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0),3)  # it draws it out, but I wish to use it on copied image #first the image we need, then the contour, then index -1 because I need all the contours  #gave it blue color and gave the thickness as 3
            #as my shapes already had area > 500 it didnt create any issues.
            #now lets calculate the curve length
            peri = cv2.arcLength(cnt,True)   #True as contours is closed

            #approximate the number of corner points
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)   #a contour is given and then the resolution,
            x, y, w, h = cv2.boundingRect(approx)

    return x + w // 2, y  # this will give us the top point and centre as well


while True:
    success, img = cap.read()
    imgResult = img.copy()  # this will be the image which will have the final information on it.
    findColor(img,myColors)      #function is called
    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):           #exit frame if pressed q
        break