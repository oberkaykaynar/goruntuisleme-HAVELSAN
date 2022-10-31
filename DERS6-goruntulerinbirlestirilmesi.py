import cv2
import numpy as np

img=cv2.imread("lenna.png")
img1=cv2.imread("obk.jpeg")

img1=cv2.resize(img1,(512,512)) #resimlerin boyutlarını eşitledik

cv2.imshow("lenna",img)
cv2.imshow("obk",img1)

yatay=np.hstack((img,img1,img)) #yatay olarak resimleri birleştirme
cv2.imshow("yatay",yatay)

dikey=np.vstack((img1,img,img1)) #dikey olarak resimleri birleştirme
cv2.imshow("dikey",dikey)

cv2.waitKey(0)
cv2.destroyAllWindows()