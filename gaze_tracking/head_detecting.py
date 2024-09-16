import cv2
import dlib
import numpy as np

# Define 3D model points of the face
MODEL_POINTS = np.array([
    (0.0, 0.0, 0.0),          # Nose tip
    (0.0, -330.0, -65.0),     # Chin
    (-225.0, 170.0, -135.0),  # Left eye left corner
    (225.0, 170.0, -135.0),   # Right eye right corner
    (-150.0, -150.0, -125.0), # Left mouth corner
    (150.0, -150.0, -125.0)   # Right mouth corner
])

# Define 2D image points
IMAGE_POINTS = np.array([
    (36, 0),  # Nose tip
    (8, 0),   # Chin
    (36, 1),  # Left eye left corner
    (45, 1),  # Right eye right corner
    (48, 0),  # Left mouth corner
    (54, 0)   # Right mouth corner
], dtype=int)

def estimate_head_pose(image, model_path):
    # Initialize dlib's face detector and pose predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(model_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray)

    for face in faces:
        # Get facial landmarks
        shape = predictor(gray, face)
        landmarks = np.array([(p.x, p.y) for p in shape.parts()])

        # Get 2D image points
        image_points = np.array([
            landmarks[30],  # Nose tip
            landmarks[8],   # Chin
            landmarks[36],  # Left eye left corner
            landmarks[45],  # Right eye right corner
            landmarks[48],  # Left mouth corner
            landmarks[54]   # Right mouth corner
        ], dtype="double")

        # Define camera matrix
        size = image.shape
        focal_length = size[1]
        center = (size[1] / 2, size[0] / 2)
        camera_matrix = np.array([
            [focal_length, 0, center[0]],
            [0, focal_length, center[1]],
            [0, 0, 1]
        ], dtype="double")

        # Assuming no lens distortion
        dist_coeffs = np.zeros((4, 1))

        # SolvePnP to estimate head pose
        _, rotation_vector, translation_vector = cv2.solvePnP(MODEL_POINTS, image_points, camera_matrix, dist_coeffs)

        # Project a 3D point to the image plane
        (nose_end_point2D, _) = cv2.projectPoints(np.array([(0, 0, 1000)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)

        # Draw the nose line
        p1 = (int(image_points[0][0]), int(image_points[0][1]))
        p2 = (int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
        cv2.line(image, p1, p2, (0, 255, 0), 2)

    return image

