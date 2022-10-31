#http://omercetin.com.tr/DERS/IP/Sunumlar/h10.pdf?i=1
#Morfolojik işlemenin amacı öncelikle segmentasyon sırasında eklenen kusurları ortadan kaldırmaktır.
#plot.subplot
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoku.jpg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("orijinal",img)
print(img.shape)

# erozyon: nesnenin sınırlarını aşındırır, nesneleri küçültebilir
kernel = np.ones((5,5), dtype = np.uint8)
erode = cv2.erode(img, kernel, iterations = 1)
cv2.imshow("erozyon",erode)

# genişleme(dilation): erozyonun tam tersidir, nesneleri büyültebilir
dilate = cv2.dilate(img, kernel,1)
cv2.imshow("dilate",dilate)

# white noise : amacımız siyah-beyazlardan oluşan karıncalar elde etmek ve bunları açılma ile gidermek
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(0), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("whitenoise"),plt.show() #opencv de hata veriyor

#whiteNoise = np.uint8(np.random.random((534,500))*255) #random bir şekilde piksele renkler yazılıyor (534,500,3) olsa renkli olacak
#cv2.imshow("whitenoise",whiteNoise)

#randomcolor = np.uint8(np.random.random((1, 1, 3)) * 255)
#randomcolor=cv2.resize(randomcolor,(480,480))
#cv2.imshow("randomcolor",randomcolor) bu şekilde rastgele renk döndürür

white_noise_img= whiteNoise + img #gürültü ile orijnal resmi birleştirdik
plt.figure(1), plt.imshow(white_noise_img, cmap = "gray"), plt.axis("off"), plt.title("white_noise_img"),plt.show() #opencv de hata veriyor

#numpy daki verilerin tiplerini öğrenme metodu "dtype"
print(kernel.dtype)
print(erode.dtype)
print(dilate.dtype)
print(whiteNoise.dtype)
print(white_noise_img.dtype)

#açılma : erozyon ve genişlemenin peş peşe kullanılmasıdır
opening=cv2.morphologyEx(white_noise_img.astype(np.float32),cv2.MORPH_OPEN,kernel)
plt.figure(2), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("opening"),plt.show() #opencv de resmi farklı gösteriyor

#black noise : bir gürültü elde ettik, kapanma filtresini nasıl çalıştığını görebilmek için
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = blackNoise*-255 #tek fark -255 ile çarpılır
plt.figure(0), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("blacknoise"),plt.show()

black_noise_img=blackNoise + img
black_noise_img[black_noise_img<=-245]=0 #bir filtre yöntemi,black_noise_img görüntüsünde bulunan değeri -245 den küçük olan pikselleri 0 yani siyah yapar.
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("black_noise_img"),plt.show()

#kapatma
closing=cv2.morphologyEx(black_noise_img.astype(np.float32),cv2.MORPH_CLOSE,kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"), plt.axis("off"), plt.title("closing"),plt.show()

#gradient :erozyon ile dilation arasındaki fark alınır. sebebi ise nesne tespitindeki sınırları görebilmek(edge detection)
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("Gradyan",gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
