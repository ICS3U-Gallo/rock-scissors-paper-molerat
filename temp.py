import cv2


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
palm_cascade = cv2.CascadeClassifier('palm_v4.xml')
#  https://github.com/Aravindlivewire/Opencv/blob/master/haarcascade/fist.xml

fist_cascade = cv2.CascadeClassifier('fist.xml')

tolerance_level = []

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    palm_contours = palm_cascade.detectMultiScale3(gray, scaleFactor=1.2, minNeighbors=5, outputRejectLevels=True)
    fist_contours = fist_cascade.detectMultiScale3(gray, scaleFactor=1.2, minNeighbors=5, outputRejectLevels=True)
    cv2.imshow('Camera', gray)
    if palm_contours[2] and palm_contours[2][0] >= 4:
        tolerance_level.append('P')
    if fist_contours[2] and fist_contours[2][0] >= 2:
        tolerance_level.append('R')
    if len(tolerance_level) >= 16:
        tolerance_level = [:16]
    if len(set(tolerance_level)) == 1:
        return tolerance_level[0]
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()