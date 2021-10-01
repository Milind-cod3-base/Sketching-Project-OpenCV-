def getContours(img):   #Function to detect countours and put a rectangle over it.


    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)      #image and retrievel method, we are using external method. RETR_EXTERNAL retrieves the extreme outer contours #next we have approximations: where we can request either all info or we can get compressed value, hence reduced value. Here I am asking for all values.
    #contours will be saved in contours
    for cnt in contours:
        area = cv2.contourArea(cnt)    #gets the area of those contours
        print(area)

        #now I need to give minimum threshold area so that it doesnt detect any noise
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0),3)  # it draws it out, but I wish to use it on copied image #first the image we need, then the contour, then index -1 because I need all the contours  #gave it blue color and gave the thickness as 3
            #as my shapes already had area > 500 it didnt create any issues.
            #now lets calculate the curve length
            peri = cv2.arcLength(cnt,True)   #True as contours is closed
            print(peri)
            #approximate the number of corner points
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)   #a contour is given and then the resolution,
            print(len(approx))   #I just need the number of corner points and not the coordinates
            #create object corners
            objCor = len(approx)
            #create a bounding box around detected object
            x, y, w, h = cv2.boundingRect(approx)