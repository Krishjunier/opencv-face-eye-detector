import cv2
import os

# Load Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier('Haar model/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Haar model/haarcascade_eye.xml')

# Input and folders
input_folder = "images"       

# Loop through all valid image files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Error loading {filename}")
            continue

        # Resize image to 960x720
        img = cv2.resize(img, (960, 720))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            # Detect eyes in face region
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Display the result
        cv2.imshow("Face & Eye Detection", img)

        # Wait for a key press to go to next image (press ESC to exit early)
        key = cv2.waitKey(0)
        if key == 27:  # ESC key
            break

cv2.destroyAllWindows()
print("All images processed and displayed.")
