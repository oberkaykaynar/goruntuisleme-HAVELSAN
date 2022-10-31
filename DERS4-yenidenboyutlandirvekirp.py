import cv2

img=cv2.imread("lenna.png")
print(img.shape) #shape resmin boyutunu gösterir, yanındaki 3 ise rgb olduğunu söyler, 1 olsa siyah-beyazdır
cv2.imshow("orijinal",img)

#yeniden boyutlandirma
imgresize=cv2.resize(img,(320,320)) #cv2.resize( , ) fonksiyonu ise resmin boyutunu istediğimiz şekilde ayarlar
print(imgresize.shape)
cv2.imshow("resize",imgresize)


#kirpma islemi
kirp=img[:200,:400] #önce yükseklik sonra genişlik yazilir
cv2.imshow("kirp",kirp)

k=cv2.waitKey(0) &0xFF
if k==ord("q"):
    cv2.destroyAllWindows()

