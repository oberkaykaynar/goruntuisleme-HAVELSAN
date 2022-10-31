#from cv2 import cv2
import cv2
cap = cv2.VideoCapture(0)

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #bu komutlarla kameramızın çözünürlüğünü öğrendik
print(width,height)

writer= cv2.VideoWriter("video_kaydi.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 30, (width,height)) #cv2.VideoWriter_fourcc(*"DIVX") = Çerçeveli sıkıştırmak için kullanılan 4 karakterli code kodudur. Windows için kullanılır
while cap.isOpened() == True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("video", frame)
        writer.write(frame) #videoya sürekli yazma yapar

    else:
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()