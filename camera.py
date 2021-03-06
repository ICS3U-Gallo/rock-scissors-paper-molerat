import numpy as np
import cv2


def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # HACK: Throws error if cv2.CAP_DSHOW is not present and I am not sure why.

    fist_cascade = cv2.CascadeClassifier('fist.xml')
    palm_cascade = cv2.CascadeClassifier('palm_v4.xml')
    fing_cascade = cv2.CascadeClassifier('finger.xml')
    # https://github.com/Balaje/OpenCV/blob/master/haarcascades/fist.xml.
    # We may need to generate our own for paper and scissors.
    tolerance_level = []  # This is a queue

    while(True):

        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        palm_contours = palm_cascade.detectMultiScale3(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            outputRejectLevels=True)
        fist_contours = fist_cascade.detectMultiScale3(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            outputRejectLevels=True)
        fing_contours = fing_cascade.detectMultiScale3(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            outputRejectLevels=True)
        print(palm_contours)
        print(fist_contours)
        cv2.imshow('Camera', gray)
        while True:
            try:  # HACK
                if palm_contours[2][0] >= 0.9:
                    tolerance_level.append('P')
                    break
            except IndexError:
                pass
            try:
                if fist_contours[2][0] >= 2:
                    tolerance_level.append('R')
                    break
            except IndexError:
                pass
            try:
                if fing_contours[2][0] >= 2.2:
                    tolerance_level.append('S')
                    break
                break
            except IndexError:
                break
        if len(tolerance_level) >= 6:
            tolerance_level = tolerance_level[1:7]
        if len(tolerance_level) == 5 and len(set(tolerance_level)) == 1:
            cap.release()
            cv2.destroyAllWindows()
            return(tolerance_level[0])

        print(tolerance_level)

        # Quit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return

if __name__ == '__main__':
    print(main())
