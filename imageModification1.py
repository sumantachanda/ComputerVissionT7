import cv2
import numpy as np
print("CV2 imported ")


#--------------importing image
img = cv2.imread("pngImage/sumata.png")
kernal = np.ones((3,3),np.uint8)   #matrix for edge Amplifiacation

imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #grayscaling
imgBlutr = cv2.GaussianBlur(imgGray,(7,7),0) #blurScale

imgCanny = cv2.Canny(img,150,200)       #edge detection by canny
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)         #edge amplificcation by dilate
imgeEdode= cv2.erode(imgDialation,kernal,iterations=1)      #edge seperation by erode


cv2.imshow("output imge",img)
cv2.imshow("imgGray imge",imgGray) #gray
cv2.imshow("imgBlutr imge",imgBlutr) #blur
cv2.imshow("imgCanny imge",imgCanny) #blur
cv2.imshow("imgDialation imge",imgDialation) #borderAmplifiayion
cv2.imshow("imgeEdode imge",imgeEdode) #blur
cv2.waitKey(0)
#---------------------------------------




#***********************************************************************************


#--------------resize image,reshap
img = cv2.imread("pngImage/sumata.png")

print(img.shape)    #image shape scale
imgResize= cv2.resize(img,(303,265))    #resize image w,h


imgCropped =  img[0:200,200:500] #crop matrix h,w


cv2.imshow("output imsge",img)
cv2.imshow("output imgResize",imgResize)    #resize image
cv2.imshow("output imgCropped",imgCropped)  #Cropped

cv2.waitKey(0)
#---------------------------------------
