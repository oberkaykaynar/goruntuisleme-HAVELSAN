import cv2
import time

path="MOT17-04-DPM.mp4"
cap=cv2.VideoCapture(path) #videoyu açtık
print("Genişlik",cap.get(3))
print("Yükseklik",cap.get(4)) #bu komutlarla videonun genişliğini ve yüksekliğini öğrendik
while cap.isOpened()==True: #video açılana kadar koşulu döndür
    ret,frame=cap.read() #ret=1 ise görüntü var 0 ise yok. frame ise piksellerin matriks karşılığını veriyor
    if ret==True:
        time.sleep(0.01) #zaman koyulmazsa video hızlı akar
        cv2.imshow("new_video",frame) #işlediğimiz video bu komutla görülüyor
    else: break #ret=0 ise döngüyü bitir

    if cv2.waitKey(1) & 0xFF== ord("q"): # "q" tuşuna bastığımızda anlık videodan çıkış yap
        break


cap.release() #video yakalamayı bırakır
cv2.destroyAllWindows() #bütün pencereleri kapat
