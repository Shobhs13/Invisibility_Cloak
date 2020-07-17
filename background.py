import cv2
#Webcam starts
cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read() #Read Webcam Data

    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5)==ord('q'):#Save the file

            cv2.imwrite('image.jpg',back)
            break

cap.release()
cv2.destroyAllWindows()
