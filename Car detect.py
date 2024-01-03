import cv2
################################################
path = 'Resources/licence-plate-autcion-b4fd.jpg'
nplateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
count = 0
minArea = 1000
################################################


while True:
    img = cv2.imread(path)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlate = nplateCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in numberPlate:
        area = w*h 
        if area>minArea:
            cv2.rectangle(img,(x,y-30),x+w+30,y+h,(0,0,255),2)
            cv2.putText(img,"NUMBER",(x,y-35),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
            imgRoi = img[y-30:y+h,x:x+w+30]
            cv2.imshow("ROI",imgRoi)
            cv2.imshow("Original",img)
            cv2.waitKey(500)        
