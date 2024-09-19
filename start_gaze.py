"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import numpy as np

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
camera_tag = "Camera"

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    # frame = gaze.annotated_frame()
    
    vertical = 0    
    horizontal = 0
    
    if not gaze.is_center():
        if gaze.is_up():
            vertical = 1
        else:
            vertical = 2
        
        if gaze.is_left():
            horizontal = 1
        else:
            horizontal = 2
    else:
        vertical = 0
        horizontal = 0

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
    cv2.putText(frame, "Pointer Cord: " + str(gaze.pointer_corrd()), (90, 200), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
    
    cv2.imshow(camera_tag, frame)
    x, y, w, h = cv2.getWindowImageRect(camera_tag)
    frame = gaze.pointer_frame(w, h)
    cv2.imshow(camera_tag, frame)
    # if left_pupil != None and right_pupil != None:
    #     left_x, left_y = left_pupil
    #     right_x, right_y = right_pupil
        # image[(left_x + right_x) // 2, (left_y + right_y) // 2] = [0, 0, 255]
        # cv2.circle(image, (left_x, left_y), 20, (255, 0, 0), 2) 
        # cv2.imwrite(camera_tag, image)
    
    
    # image_height, image_width = 500, 500
    # image = np.ones((image_height, image_width, 3), dtype=np.uint8) * 255

    # center_x, center_y = image_width // 2, image_height // 2
    # rect_size = 50

    # offsets = [
    #     (0, 0),
    #     (-rect_size * 2, 0),
    #     (rect_size * 2, 0),
    #     (0, -rect_size * 2),
    #     (0, rect_size * 2),
    #     (-rect_size * 2, -rect_size * 2),
    #     (rect_size * 2, -rect_size * 2),
    #     (-rect_size * 2, rect_size * 2),
    #     (rect_size * 2, rect_size * 2)
    # ]

    # for i, (dx, dy) in enumerate(offsets):
    #     top_left = (center_x + dx - rect_size // 2, center_y + dy - rect_size // 2)
    #     bottom_right = (center_x + dx + rect_size // 2, center_y + dy + rect_size // 2)
        
    #     filled = False
    #     match i:
    #         case 0:
    #             filled = vertical == 0 and horizontal == 0
    #         case 1:
    #             filled = vertical == 0 and horizontal == 1
    #         case 2:
    #             filled = vertical == 0 and horizontal == 2
    #         case 3:
    #             filled = vertical == 1 and horizontal == 0
    #         case 4:
    #             filled = vertical == 2 and horizontal == 0
    #         case 5:
    #             filled = vertical == 1 and horizontal == 1
    #         case 6:
    #             filled = vertical == 1 and horizontal == 2
    #         case 7:
    #             filled = vertical == 2 and horizontal == 1
    #         case 8:
    #             filled = vertical == 2 and horizontal == 2
                
            
    #     if filled:
    #         cv2.rectangle(image, top_left, bottom_right, (0, 0, 0), -1)
    #     else:
    #         cv2.rectangle(image, top_left, bottom_right, (0, 0, 0), 2)

    # cv2.imshow('Directions', image)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()
