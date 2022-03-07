import cv2
import  numpy as np


def getContours(img):       #funtion to create contour elements in the image
    contiurs,hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for cnt in contiurs:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 10:  # reovig noise
            cv2.drawContours(imgContor,cnt,-2,(255,9,0),1,) #drwaing Contour

            peri = cv2.arcLength(cnt,True)      #calculating Parameter of the image
            print(peri)     #printing perimerter
            aprox = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(aprox)        #print Aprox
            print(len(aprox))

            objCor = len(aprox)
            x,y,w,h = cv2.boundingRect(aprox)       #bounding box arounf the countur

            if objCor ==3: objectType = "Triangle"
            elif objCor == 4: objectType = "Square"
            elif objCor >= 4: objectType = "circle"

            #compairing shape
            else: objectType="unidentified"

            cv2.rectangle(imgContor,(x+2,y+2),(x+w+2,y+h+2),(0,255,0),2)

            cv2.putText(imgContor,objectType,       #inserting text
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,
                         0.5,(0,0,255),1)








imgpath ='pngImage/img_7.png'
img = cv2.imread(imgpath)
imgContor = img.copy()




imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)


getContours(imgCanny)




cv2.imshow("orignal",imgCanny )
cv2.imshow("orignal1",imgGray)
cv2.imshow("orignal2",imgContor)
cv2.imshow("orignal3",img)
cv2.waitKey(0)
