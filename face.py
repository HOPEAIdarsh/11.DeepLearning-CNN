import cv2
trainedDataset = cv2.CascadeClassifier('haarcascade_frontalface_default (1).xml')

img=cv2.imread('images/smile.jpeg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=trainedDataset.detectMultiScale(gray)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x + w,y + h),(255,0,0),2)

cv2.imshow('RaviChandran',img)
#cv2.imshow('Gray',gray)
cv2.waitKey()
