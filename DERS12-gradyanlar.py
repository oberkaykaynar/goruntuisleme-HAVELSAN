# bir görüntüdeki yoğunluk veya renkteki yönlü bir değişikliktir. Görüntünün gradyanı, görüntü işlemedeki
# temel yapı taşlarından biridir.Örneğin, Canny kenar algılayıcı , kenar algılama için görüntü gradyanını kullanır
import cv2

img=cv2.imread("sudoku.jpg",0)
cv2.imshow("sudoku",img)

#ddepth parametresi outputun derinliğini gösterir,kernel size de matrisi(5e5) belirler
sobelx=cv2.Sobel(img,cv2.CV_16S,dx=1,dy=0,ksize=5) #x yönündeki gradyant
cv2.imshow("sobelx",sobelx)

sobely=cv2.Sobel(img,cv2.CV_16S,dx=0,dy=1,ksize=5)#y yönündeki gradyant
cv2.imshow("sobely",sobely)

#laplacian gradient
laplacian=cv2.Laplacian(img,ddepth=cv2.CV_16S,ksize=5) #hem x hem de y yönünde gradyan yapar
cv2.imshow("laplacian",laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()