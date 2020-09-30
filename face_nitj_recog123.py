import face_recognition as fc
import cv2
s=fc.load_image_file(r'/Users/techie/Desktop/my.jpg')
a=fc.load_image_file(r'/Users/techie/Desktop/amit.jpg')
sh=fc.load_image_file(r'/Users/techie/Desktop/shubham.jpg')
sl=fc.face_locations(s)
al=fc.face_locations(a)
shl=fc.face_locations(a)
se=fc.face_encodings(s,sl)[0]
ae=fc.face_encodings(a,sl)[0]
she=fc.face_encodings(sh,shl)[0]
te=[se,ae,she]
l=['SauR','Amit','Shubham']
v=cv2.VideoCapture(0)
flag=0
while(1):
    r,i=v.read()
    il=fc.face_locations(i)
    #print(il,len(il))
    if(len(il)>0)and(flag==1):
        re=fc.face_encodings(i,il)[0]
        res=fc.compare_faces(te,re)
        print(res)
        ind=res.index(True)
        print(l[ind],' face is recognized')
        flag=0
    else:
        flag=1
    cv2.imshow('my img',i)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break
cv2.destroyAllWindows()
v.release()
    
