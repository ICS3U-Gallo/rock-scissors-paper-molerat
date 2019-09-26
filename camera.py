import numpy as np
import cv2

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # HACK: Throws error if cv2.CAP_DSHOW is not present and I am not sure why.

    fist_cascade = cv2.CascadeClassifier('fist.xml')
    # This haar-cascade was taken from https://github.com/Balaje/OpenCV/blob/master/haarcascades/fist.xml.
    # We may need to generate our own for paper and scissors.

    while(True):

        # Capture frame
        ret, frame = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Don't actually need as a numpy array right now, I think
        fist_contours = np.array(fist_cascade.detectMultiScale(gray, 1.5, 2))
        if fist_contours:
            cap.release()
            cv2.destroyAllWindows()
            return "R"  # For rock

        # Display frame
        cv2.imshow('Camera', frame)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()
    return

if __name__ == '__main__':
    print(main())