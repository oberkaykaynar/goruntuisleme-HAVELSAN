import cv2
import numpy as np

#arka plan
img=np.zeros((512,512,3),np.uint8)+255 #255 çıktısı verir ve arka plan beyaz olur.sayısal değeri oynadıkça gri-siyah-beyaz olur
cv2.imshow("resim",img)
print(img.shape)
print("sifirlar:",img)

img1=np.ones((512,512,3),np.uint8)+0 #1 çıktısı verir ve arka plan siyah olur.
cv2.imshow("resim1",img1)
print(img1.shape)
print("birler:",img1)

#sekil cizme
#(resim,baslangic n.,bitis n., renk,kalinlik(ya da içini doldurma))=parametreler
cv2.line(img,(0,0),(512,512),(0,0,255),5) #python rgb değil bgr formatını kullanır
cv2.rectangle(img,(100,100),(200,200),(0,255,0),cv2.FILLED)#cv2.FILLED parametresi ile içini doldurabiliriz
#(resim,baslangic n.,yaricap,renk,kalinlik(ya da içini doldurma))=çember parametreleri
cv2.circle(img,(300,300),45,(255,0,0),cv2.FILLED)#çemberin içi doluysa(cv2.FILLED) daire olur

#metin ekleme
#(img, text, baslangic n., font,kalinlik, color)=parametreler
cv2.putText(img,"Berkay",(100,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
cv2.imshow("sekil ve metin",img)

k=cv2.waitKey(0)&0xFF
if k==27:
    cv2.destroyAllWindows()
