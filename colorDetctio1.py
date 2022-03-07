import cv2
import numpy as np

print("CV2 imported ")


def empty(a):
    pass


img = cv2.imread('pngImage/img_3.png')  # img matrix

cv2.namedWindow("trackBar")  # track bar for coloar aection
cv2.resizeWindow("trackBar", 640, 240)

cv2.createTrackbar("Hue max", "trackBar", 179, 179, empty)  # (sclecterRange,toRange)
cv2.createTrackbar("Hue min", "trackBar", 137, 137, empty)
cv2.createTrackbar("sat Max", "trackBar", 255, 255, empty)
cv2.createTrackbar("sat min", "trackBar", 128, 128, empty)
cv2.createTrackbar("val Max", "trackBar", 255, 255, empty)
cv2.createTrackbar("val min", "trackBar", 51, 51, empty)

while True:
    # type of ColorScale
    imgHSv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgHLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    # reading tracbar

    h_max = cv2.getTrackbarPos("Hue max", "trackBar")
    h_min = cv2.getTrackbarPos("Hue min", "trackBar")
    s_max = cv2.getTrackbarPos("sat Max", "trackBar")
    s_min = cv2.getTrackbarPos("sat min", "trackBar")
    v_max = cv2.getTrackbarPos("val Max", "trackBar")
    v_min = cv2.getTrackbarPos("val min", "trackBar")

    print(h_max, h_min, s_max, s_min)

    lower = np.array([h_min, s_min, v_min])  # paramer matrix for slider
    upper = np.array([h_max, s_max, v_max])
    maskLayer = cv2.inRange(imgHSv, lower, upper)  # tratement tlayer

    imgResult = cv2.bitwise_and(img, img, mask=maskLayer)  # imposinglayer

    cv2.imshow("image", img)
    cv2.imshow("imgResult", imgResult)
    cv2.imshow("imaHmaskLayer", maskLayer)
    cv2.waitKey(1)
# ---------------------------------------
