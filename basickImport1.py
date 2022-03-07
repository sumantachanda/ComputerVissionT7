import cv2
print("CV2 imported ")


# #--------------importing image
# img = cv2.imread("pngImage/sumata.png")
# cv2.imshow("output imsge",img)
# cv2.waitKey(0)
# #---------------------------------------








#--------------importing video
#*cap = cv2.VideoCapture("pngImage/roadVideo.mp4")      #video

#--------------importing video
#*cap = cv2.VideoCapture("pngImage/roadVideo.mp4")      #video

cap = cv2.VideoCapture("rest")     #id   0 for default webcam,

cap.set(3,640)
cap.set(4,480)

cap.set(10,50)   #id 10 fpr brigtness and 50 for the amout



while True:
    success, img=cap.read()
    cv2.imshow("my video",img)
    if cv2.waitKey(1) & 0xFF ==ord('x'): #keybord inturpt
        break

#---------------------------------------


cap = cv2.VideoCapture("rst")     #id   0 for default webcam,

cap.set(3,640)
cap.set(4,480)

cap.set(10,50)   #id 10 fpr brigtness and 50 for the amout



while True:
    success, img=cap.read()
    cv2.imshow("my video",img)
    if cv2.waitKey(1) & 0xFF ==ord('x'): #keybord inturpt
        break

#---------------------------------------






