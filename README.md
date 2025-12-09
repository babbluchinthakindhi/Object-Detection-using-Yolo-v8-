# 🎥 Real-Time Object Detection Web App (YOLOv8 + Django)

A real-time **Object Detection Web Application** built using **Django** and **YOLOv8** that uses your **device or PC camera** to detect objects live.  
No image uploads required — everything happens through the camera in real time.

This project is fast, lightweight, and designed to demonstrate practical computer vision using deep learning.

---

## 🚀 Project Description

This application accesses the system’s webcam and performs **live object detection** using the YOLOv8 model.  
It detects objects such as people, cars, phones, bottles, and many more directly from the video feed.

The main goal of this project is to provide a real-time detection experience through a simple web interface.

---

## 📂 Included Project Files

The project contains the following important files and folders:

detecor/ → Main Django app
yolo_project/ → Django project configurations
db.sqlite3 → SQLite database
manage.py → Django management file
yolov8n.pt → Pre-trained YOLOv8 model

---

## 🛠️ Technologies Used

- **Python**
- **Django**
- **YOLOv8 (Ultralytics)**
- **OpenCV**
- **SQLite Database**

---

## ▶️ How to Run the Project

Follow these steps to run the project locally:

### 1. Clone the repository
bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Create and activate a virtual environment
bash
python -m venv venv
source venv/bin/activate     # For Linux/Mac
venv\Scripts\activate        # For Windows

3. Install required packages
bash
pip install django ultralytics opencv-python torch

4. Run migrations
bash
python manage.py migrate

5. Start the server
bash
python manage.py runserver

6. Open in Browser
http://127.0.0.1:8000/
When you open the app, it will automatically access your device camera for live detection.

🔍 How It Works
The browser opens the live webcam feed.

Each frame is processed by the YOLOv8 model.

Detected objects are highlighted in real time.

Labels and bounding boxes appear instantly on the video.

✨ Key Features
✅ Real-time camera-based object detection
✅ Works with PC / Laptop webcam
✅ Fast and lightweight YOLOv8 model
✅ Easy to set up and run

🚧 Future Improvements
Add mobile camera support

Record and save detected videos

Add FPS counter and detection stats

🤝 Contributing
Feel free to fork this repository and raise pull requests.
Suggestions and improvements are always welcome.

📄 License
This project is open-source and available for learning and development purposes.

⭐ If you find this project useful, don’t forget to star the repository!
