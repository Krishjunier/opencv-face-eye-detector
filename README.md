# opencv-face-eye-detector

As part of my Week 2 task during the Artificial Intelligence Internship at **NOVANECTAR SERVICES PVT. LTD.**, I implemented a computer vision project that detects faces and eyes in images using Haar Cascade classifiers with OpenCV.

## 📌 Features

- Detects human faces in images using Haar Cascade  
- Detects eyes within detected face regions  
- Draws bounding boxes for both faces and eyes  
- Resizes all input images to 960x720  
- Processes `.jpg`, `.jpeg`, `.png`, and `.bmp` files  

## 🧠 Technologies Used

- Python 3  
- OpenCV  
- Haar Cascade Classifiers  

## 🗂️ Folder Structure

- `images/` → Input images  
- `Haar model/` → Contains the following:  
  - `haarcascade_frontalface_default.xml`  
  - `haarcascade_eye.xml`  

## ▶️ How to Run

1. Install dependencies:-'pip install opencv-python'  
2. Run the script:-'python face_eye_detection.py'  

## 🧪 What the Code Does

- Loads Haar Cascade models for face and eye detection  
- Reads and resizes images from the `images/` folder  
- Converts images to grayscale  
- Detects faces and then eyes inside each face  
- Draws rectangles around faces (blue) and eyes (green)  
- Displays each processed image one by one  
