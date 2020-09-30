import cv2
import vlc,time

v=vlc.MediaPlayer(r'/Users/techie/Desktop/Data Centre/MLnDS Seminar/humsafer2.mp3')
v.audio_set_volume(100)
v.play()
cam=cv2.VideoCapture(0)
time.sleep(2)
flag=1
face=cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
while(1):
    total=0
    d,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('my image1',gray)
    faces=face.detectMultiScale(gray,1.3,9)
    #print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        total=w*h
    cv2.imshow('my image',img)
    x=len(faces)
    if(x>0):
        print('Face is detected')
        v.play()
        flag=0
        v.audio_set_volume(100-int(total/1000))
    elif(flag==0):
        print('No Face is Available')
        v.pause()
        flag=1 
    k = cv2.waitKey(2)
    if k == ord('q'):
        v.stop()
        break
cv2.destroyAllWindows()
