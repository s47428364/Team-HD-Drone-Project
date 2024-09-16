import cv2
import dlib
import numpy as np

# Define a function to calculate the Eye Aspect Ratio (EAR)
def calculate_ear(eye_points):
    A = np.linalg.norm(eye_points[1] - eye_points[5])
    B = np.linalg.norm(eye_points[2] - eye_points[4])
    C = np.linalg.norm(eye_points[0] - eye_points[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Load the pre-trained model and initialize face detector
model_path = 'shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(model_path)

# Define constants
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 3
COUNTER = 0

def detect_blink(frame):
    global COUNTER

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        landmarks = np.array([[p.x, p.y] for p in landmarks.parts()])

        # Extract the eye landmarks
        left_eye = landmarks[36:42]
        right_eye = landmarks[42:48]

        # Compute the EAR for both eyes
        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)

        # Average EAR for both eyes
        ear = (left_ear + right_ear) / 2.0

        # Check if EAR is below the threshold
        if ear < EYE_AR_THRESH:
            COUNTER += 1
        else:
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                print("Blink detected!")
            COUNTER = 0

        # Draw landmarks on the frame
        for (x, y) in landmarks:
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
        
        # Draw eye contour lines
        cv2.polylines(frame, [left_eye], True, (0, 255, 0), 1)
        cv2.polylines(frame, [right_eye], True, (0, 255, 0), 1)
    
    return frame