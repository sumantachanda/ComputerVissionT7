import cv2
import numpy as np
print("CV2 imported ")

img =np.zeros((512,512,3),np.uint8) #img matrix
print(img)

img[200:300,100:250]=255,0,0  #img color

cv2.line(img,(0,0),(300,300),(0,255,0),3)   #((distance),(shaspe),color,thickness
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(450,50),30,(255,255,0),5)
cv2.putText(img,"openCV",(300,100),cv2.FONT_HERSHEY_PLAIN,1,(0,150,0),1)

cv2.imshow("image", img)


cv2.waitKey(0)
#---------------------------------------
