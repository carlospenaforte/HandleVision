import numpy as np
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)



while True:
    ret, frame = cap.read()

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()