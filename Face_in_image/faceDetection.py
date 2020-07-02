# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:10:08 2020

@author: ShantanuRM
"""

import cv2

img_original = cv2.imread("face.jpg")
##print(img.shape)
resized = cv2.resize(img_original,(600,600))

##create classifier object
face_in_image = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

##Covert image to gray scale 
gray_img = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

Img_face = face_in_image.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)

print(type(Img_face))
#coordinates of face
print(Img_face)

## square arround the face
for x, y, w, h in Img_face:
    img = cv2.rectangle(resized, (x,y), (x+w,y+h),(255,0,0), 3)
    
##Output
cv2.imshow("Legend",img)
cv2.waitKey(0)
cv2.destroyAllWindows()