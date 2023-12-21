import numpy as np 
import cv2

#รายชื่อหมวดหมู่ทั้งหมด เรียงตามลำดับ
CLASSES = ["BACKGROUND", "AEROPLANE", "BICYCLE", "BIRD", "BOAT",
	"BOTTLE", "BUS", "CAR", "CAT", "CHAIR", "COW", "DININGTABLE",
	"DOG", "HORSE", "MOTORBIKE", "PERSON", "POTTEDPLANT", "SHEEP",
	"SOFA", "TRAIN", "TVMONITOR"]
border_colors = np.random.uniform(0,100,size=(len(CLASSES), 3))

net = cv2.dnn.readNetFromCaffe("./MobileNetSSD/MobileNetSSD.prototxt","./MobileNetSSD/MobileNetSSD.caffemodel")

#cap = cv2.VideoCapture("MobileNetSSD/Supra MK4 short edit.mp4")  #video1
#cap = cv2.VideoCapture("MobileNetSSD/BostonRobotics.mp4")        #video2
cap = cv2.VideoCapture(0)   #camera

while True:
    ret,frame = cap.read()
    if ret == True:
        (h,w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 0.007843,(300,300),127.5)
        net.setInput(blob)
        detection = net.forward()
        
        for i in np.arange(0,detection.shape[2]):
            percent = detection[0,0,i,2]
            if percent > 0.8:
                class_index = int(detection[0,0,i,1])
                box = detection[0,0,i,3:7]*np.array([w,h,w,h])
                (startX,startY,endX,endY) = box.astype("int")

                label = "{} [{:.2f}%]".format(CLASSES[class_index],percent*100 )  #ชื่อที่ปรากฎด้านบน
                cv2.rectangle(frame,(startX,startY),(endX,endY),border_colors[class_index],2)
                cv2.rectangle(frame,(startX-1,startY-30),(endX+1,startY),border_colors[class_index], cv2.FILLED)
                y = startY - 15 if startY-15>15 else startY+15
                cv2.putText(frame,label,(startX+20,y+5),cv2.FONT_HERSHEY_DUPLEX,0.6,(255,255,255),1)

        cv2.imshow("Supra",frame)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()