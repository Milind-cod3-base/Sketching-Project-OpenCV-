# Sketching-Project-OpenCV

## What: 
This project uses OpenCV and Numpy libraries to detect and mask a colour or multiple colours. And then it can write/sketch/paint directly on the webcam as you move the coloured objects.

## Why:
The motivation behind this project was "I find using white board redundant".

This project can help Youtubers and content creators (Especially Teaching/Tutorial Channels), as they can write anything they wish directly on their camera's window.

As one can use multiple colours at the same time, this project is also useful for painters/artists, who wish to use it for either digital art or just a rough canvas.

## How:

NOTE: If you are using webcam embedded in laptop, in cv2.VideoCapture(0+cv2.CAP_DSHOW), replace 0+cv2.CAP_DSHOW with 0 (but if its taking a long time to open you webcam, use the former instead). If you are using external USB webcam, replace 0+cv2.CAP_DSHOW with 1.

--> Open Tracker_color_values.py file 

--> Run the code 

--> One HSV window will appear with trackbars 

--> Place the object you wish to track on screen (if you wish to use multiple objects/ place the first and continue)

--> Toggle the trackbars values until the object turns white while the environment around it turns black (Mask)

--> Note down these HSV values

--> Open the Sketching_Main code.py file, and put those values in the myColors object -- Inside any of the nested list (Replace values provided previously)

--> Now go to myColorValues list and enter the colour value -- Here you can choose the type of ink you wish to use while drawing/sketching.

--> [OPTIONAL] If you wish to track multiple objects as you wish to use multiple colours at the same time, repeat the above process for each object and mask them with color values. Put the values in the nested list of myColors and myColorValues object.

--> Run the code. Enjoy.

