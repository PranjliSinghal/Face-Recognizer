import cv2

#import numpy as np

recog = cv2.face.LBPHFaceRecognizer_create()
cascadePath = "C:\\Users\\user\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml"
faceDetect = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)


while True:
    count=0
    id=0
    ret, img =cam.read()#it basically returns two things ret and img,img is used and ret is ignored
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
       
       

  
       
          



    cv2.imshow('Face',img)



    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()



                         

