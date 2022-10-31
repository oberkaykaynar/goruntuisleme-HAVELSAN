import cv2
import numpy as np

img=cv2.imread("kart.png")
cv2.imshow("orijinal",img)
genislik=620
yukseklik=544
orj=np.float32([[204,2],[540,148],[1,474],[340,619]]) #resmin köşedeki piksel numaralarını "paint" uygulamasıyla öğrendik
real=np.float32([[0,0],[yukseklik,0],[0,genislik],[yukseklik,genislik]]) #olmasi gereken kose yerlerini numaralandirdik

#Perspektif dönüşümü için 3X3 dönüşüm matrisine ihtiyaç duymaktayız.
# Dönüşüm matrisini(transformation matrix) bulmak için görüntü üzerinde 4 noktaya
# ve bu noktaların toplam çıktısını almaya ihtiyacımız bulunmaktadır.
# Bu 4 noktanın 3'ü collinear olmamalıdır. Dönüşüm matrisini bulmak için
# kullanacağımız cv2.getPerspectiveTransformation() fonksiyonundan sonra
# cv2.warpPerspective fonksiyonunu kullanarak 3X3 matrisimizi elde etmiş olacağız. Daha fazla bilgi için:
#https://www.turanerdemsimsek.com/2017/11/opencv-goruntu-uzerinde-geometrik.html
matrix=cv2.getPerspectiveTransform(orj,real) #bu parametre perspektife özel bir parametredir
print(matrix)
img_output=cv2.warpPerspective(img,matrix,(yukseklik,genislik)) #bu parametre perspektife özel bir parametredir
cv2.imshow("output",img_output)

cv2.waitKey(0)
cv2.destroyAllWindows()