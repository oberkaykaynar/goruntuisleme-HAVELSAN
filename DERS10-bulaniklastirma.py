"""Bir alan içinde yer alan piksel değerlerinin ortalamasını ifade eder. Buna aynı zaman da
Low Pass Filter de denilir. Low pass filter, düşük frekanslara izin veren ve daha yüksek frekansları
bu işlem görüntüdeki gürültüyü azaltmak veya daha az pikselli bir görüntü oluşturmak için kullanılır.
https://abdulsamet-ileri.medium.com/g%C3%B6r%C3%BCnt%C3%BC-filtrelerini-uygulama-ve-kenarlar%C4%B1-alg%C4%B1lama-21d42f194db4
gürültüyü gidermek için bulanıklaştırmalar kullanışlıdır
3 ana tür bulanıklaştırma tekniği vardır
"""

#BU KONU TAM ANLASILMADI, DETAYLI ARASTIRMALARI YAP

import cv2
import numpy as np

img=cv2.imread("NYC.jpg")
#ortalama bulaniklastirma yontemi
blur=cv2.blur(img,(3,3)) #2.parametreyi arttırırsan bulaniklastirma artar, degerlerin degistirilmemesi tavsiye edilir
cv2.imshow("orijinal",img)
cv2.imshow("blur",blur)

#Gaussian Blur bulaniklastirma yontemi
gaus_blur=cv2.GaussianBlur(img,(3,3),7) #degerlerin degistirilmemesi tavsiye edilir
cv2.imshow("gaus_blur",gaus_blur)

#Medyan bulaniklastirma yontemi
medyan=cv2.medianBlur(img,3) #degerin degistirilmemesi tavsiye edilir, en çok kullanılanı
cv2.imshow("medyan",medyan)

def gaussianNoise(image): #filtrelerimizin işe yaradığını görmek için gürültü fonksiyonu yarattık
    row,column,channel=image.shape
    mean=0
    var=0.05
    standart_sapma=var**0.5
    gauss=np.random.normal(0,standart_sapma,(row,column,channel))
    gauss=gauss.reshape(row,column,channel)
    noisy=(image+gauss)
    return noisy #gelen değerler 0 ile 1 arasında

img1=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)/255  #değerleri 0 ile 1 arasına koymak için, yoksa gürültünün bir etkisi olmayacak
gaus_noise_img=gaussianNoise(img1)
cv2.imshow("gaussian noise",gaus_noise_img)

#gauss blur yaparak gürültüyü azalt
gaus_blur_noisy=cv2.blur(gaus_noise_img,(3,3))
cv2.imshow("gaus_blur_noise",gaus_blur_noisy)

def saltpepperNoise(image):
    row,column,channel=image.shape
    s_vs_p=0.5 #tuz, karabiber oranını eşitledik
    amount=0.04
    noisy=np.copy(image) #orijinal resmi kopyaladık ileride lazım olabilir

    #salt beyaz
    num_salt=np.ceil(amount *image.size * s_vs_p)
    coords=[np.random.randint(0,i-1,int(num_salt)) for i in image.shape]
    noisy[coords]=1

    #pepper siyah
    num_pepper=np.ceil(amount*image.size*(1-s_vs_p))
    coords=[np.random.randint(0,i-1,int(num_pepper)) for i in image.shape]
    noisy[coords]=0

    return noisy

sp_image=saltpepperNoise(img)
cv2.imshow("sp_image",sp_image)

mb2=cv2.medianBlur(sp_image,3)
cv2.imshow("with mb",mb2)

cv2.waitKey(0)
cv2.destroyAllWindows()