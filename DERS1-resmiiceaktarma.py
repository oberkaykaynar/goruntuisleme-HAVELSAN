import cv2

img=cv2.imread("obk.jpeg",0)

cv2.imshow("obkgray.jpeg",img)

k=cv2.waitKey(0) & 0xFF #bu ifade kapanmayı belirliyor
if k==35: #35 değeri "del" tuşunun sayısal karşılığıdır. "del" tuşuna basılırsa görüntüden çıkılır
    cv2.destroyAllWindows() #çıkış yapılır
elif k==ord("s"): #s tuşuna bastığımızda bu koşul yürütülür
    cv2.imwrite("obkgray.jpeg",img) #resmi kaydeder
    cv2.destroyAllWindows()