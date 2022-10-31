import cv2

img1=cv2.imread("img1.JPG")
img2=cv2.imread("img2.JPG")

img1=cv2.resize(img1,(800,800))
img2=cv2.resize(img2,(800,800))
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

#renk donusumleri baska bir platformda(matplotlib gibi) gosterildigi taktirde bunun uygulanmasi gerekirs
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

#source1,alpha(birinci resmin katsayisi),source2,beta(ikinci resmin katsayisi),gama(genelde 0 verilir)
img=cv2.addWeighted(img1,0.2,img2,0.8,0)
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()