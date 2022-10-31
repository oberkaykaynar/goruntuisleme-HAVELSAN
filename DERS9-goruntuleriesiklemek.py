import cv2
import matplotlib.pyplot as plt

img=cv2.imread("img1.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#görüntü eşikleme (foto,threshol deg,max_value,tipi)=parametreler
_,thershold_img=cv2.threshold(img,60,255,cv2.THRESH_BINARY) #"_" değeri ile işimiz yok, cv2.THRESH_BINARY_INV ise tersini alır
#threshold değerini istediğiniz şekilde değiştirebilirsiniz
cv2.imshow("threshold",thershold_img)

#matplotlib ile göstermek istersek
#plt.figure()
#plt.imshow(img,cmap="gray") #cmap="gray" parametresi siyah-beyaza dönüştürür
#plt.axis("off") #x-y eksen bilgilerini kapatır
#plt.show()

#uyarlamalı görüntü eşikleme(aydınlatması farklı olan bölgelerde avantaj saglar)
#parametrelerdeki sayılar sabittir,hesaplanılmıstır
adaptive_img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
cv2.imshow("adaptive_threshold",adaptive_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
