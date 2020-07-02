# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:51:24 2020

@author: ShantanuRM
"""
##importing OpenCv and time 
import cv2, time

##captured from webcam
video = cv2.VideoCapture(0)

##for face cordinates "haarcascade_frontalface_default.xml" dataset used
face_in_image = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

##loooping through each frame
i = 1
while True:
    i+=1
    check, frame = video.read()
    print(frame)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_in_image.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)
    for x, y, w, h in face:
        cam = cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0), 3)
    cv2.imshow("Captured Video", cam)
    ## waitkey is for new frame after 1 millisecond
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
print(i)
video.release()
cv2.destroyAllWindows()

    