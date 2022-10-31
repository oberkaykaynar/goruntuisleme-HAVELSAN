#renklerin ton dağılımı histogram yardımı ile anlasilabilir
import cv2
import matplotlib.pyplot as plt
import numpy as np

#1.resim
img=cv2.imread("red_blue.jpg")
print("boyut:",img.shape)
cv2.imshow("red",img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img),plt.title("red_blue"),plt.show()
#channels=[0] mavi olduğu anlamına gelir. eğer s-b ise [0] gray scale demek, histSize=[256] (0 dahil), ranges=[0,256] (256 dahil değil)
hist=cv2.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
print(hist.shape)
plt.figure(), plt.plot(hist),plt.title("histogram"),plt.show() #histogram oluşturduğumuz için plt.plot() kullanılır

color=["b","g","r"]
for i,j in enumerate(color): #enumerate=(0,"b"),(1,"g"),(2,"r") yapar i=1,2,3 j="b","g","r"
    print(i,j)
    hist=cv2.calcHist([img],channels=[i],mask=None,histSize=[256],ranges=[0,256]) #kanal sayısını i belirliyor
    plt.plot(hist,color=j), plt.title("renkli_hist"),plt.show() #histogramın rengini j belirliyor


#2.resim / maskeleme yöntemi
img1=cv2.imread("goldenGate.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img1),plt.show()
mask=np.zeros(img1.shape[:2],dtype=np.uint8) #channel ile işimiz olmadığı için resmin boyutunu aldık ve int a eşitledik
plt.figure(),plt.imshow(mask,"gray"),plt.show()

mask[1500:2000,1000:2000]=255 #resmin bu aralıktaki değerlerini beyaz yapıyor
plt.figure(),plt.imshow(mask,"gray"),plt.show()

maskeli_resim=cv2.bitwise_and(img1,img1,mask=mask)
plt.figure(),plt.imshow(maskeli_resim,"gray"),plt.show()
liste1=["b","g","r"]
for i,j in enumerate(liste1):
    print(i,j)
    hist1=cv2.calcHist([maskeli_resim],channels=[i],mask=mask,histSize=[256],ranges=[0,256])#channels=[0] mavidir. 1=yesil,2=kirmizi
    plt.figure(),plt.plot(hist1,color=j),plt.show()


#3.resim / histogram eşikleme yöntemi(kontrast(karşıtlık) arttırma)

img2=cv2.imread("hist_equ.jpg",0)
plt.figure(),plt.imshow(img2,"gray"),plt.show()
hist2=cv2.calcHist([img2],[0],mask=None,histSize=[256],ranges=[0,256])
plt.figure(),plt.plot(hist2),plt.show()

equ_img2=cv2.equalizeHist(img2) #kontrast arttırma fonksiyonu. bu sayede renk değerleri 255 e yaklaştırılır
plt.figure(),plt.imshow(equ_img2,"gray"),plt.show()
equ_img2_with_hist=cv2.calcHist([equ_img2],[0],mask=None,histSize=[256],ranges=[0,256])
plt.figure(),plt.plot(equ_img2_with_hist),plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()