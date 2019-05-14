import numpy as np
import cv2 as cv

background = None

# Capture default camera
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    height, width, channels = frame.shape

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    output = np.zeros_like(frame)

    if background is None:
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(output, 'Press B to set background', (height // 10, height // 10), font, 0.5, (255,255,255), 1, cv.LINE_AA)
    else:
        output = cv.addWeighted(background, 1 / 3, frame, 2 / 3, 0)

    # Display the resulting frame
    cv.imshow('frame', output)
    wait = cv.waitKey(1)
    if wait == ord('q'):
        break
    elif wait == ord('b'):
            background = frame

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
