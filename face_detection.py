import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(1)

while True:
  _,image = capture.read()
  image = cv2.flip(image, 1)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  faces = face_cascade.detectMultiScale(gray,
                                        scaleFactor= 1.1,
                                        minNeighbors= 5,
                                        minSize=(30, 30))

  for (x, y, w, h) in faces:

    cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,0), 2)

  cv2.imshow('faces encontrada!', image)
  k = cv2.waitKey(30) & 0xff 
  if k == 27: 
    break

capture.release()
cv2.destroyAllWindows()