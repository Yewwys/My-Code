import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
    boo,frame = cap.read()
    if boo == True:
        cv2.imshow('Output',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()