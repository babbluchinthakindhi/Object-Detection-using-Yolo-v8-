# detection/views.py
import threading
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import DetectionLog
from .forms import CustomUserCreationForm, CustomLoginForm
from ultralytics import YOLO
import threading
import cv2

stop_event = threading.Event()

model = YOLO('yolov8n.pt')  # make sure yolov8n.pt is in your root or full path given
DETECTION_RUNNING = False

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    logs = DetectionLog.objects.all().order_by('-timestamp')[:20]
    return render(request, 'dashboard.html', {'logs': logs})

def detect_objects(user):
    cap = cv2.VideoCapture(0)

    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                label = model.names[cls_id]

                # Save to database with associated user
                DetectionLog.objects.create(
                    user=user,
                    object_name=label,
                    confidence=conf
                )

                # Draw bounding box and label
                xyxy = box.xyxy[0].cpu().numpy().astype(int)
                cv2.rectangle(frame, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (0, 255, 0), 2)
                cv2.putText(frame, f'{label} {conf:.2f}', (xyxy[0], xyxy[1]-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Show the camera frame in a small local window
        cv2.imshow("YOLOv8 Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_event.set()
            break

    cap.release()
    cv2.destroyAllWindows()

@login_required
def start_detection(request):
    global detection_thread, stop_event
    stop_event.clear()
    detection_thread = threading.Thread(target=detect_objects, args=(request.user,))
    detection_thread.start()
    return redirect('dashboard')

@login_required
def stop_detection(request):
    stop_event.set()
    global DETECTION_RUNNING
    DETECTION_RUNNING = False
    return redirect('dashboard')

def forgot(request):
    # Placeholder for forgot password functionality
    return render(request, 'forgot.html')