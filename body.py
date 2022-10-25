from time import sleep
import cv2
import mediapipe as mp
import serial
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

arduino = serial.Serial(port='COM11', baudrate=115200, timeout=.1)
cap=cv2.VideoCapture(0)
box = 70

with mp_pose.Pose(
    model_complexity=0,
    min_detection_confidence=0.5
    ) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      continue
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    image_height, image_width, _ = image.shape
    cv2.rectangle(image,(image_width//2-box,image_height//2-box),
                 (image_width//2+box,image_height//2+box),
                  (255,255,255),1)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if not results.pose_landmarks:
      continue
    x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width
    y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height
    cv2.circle(image, (int(x),int(y)), 3, (0,255,0), 3)
    nx = int(x)
    # ny = int(y)
    fx1 = (image_width//2-box)
    fx2 = (image_width//2+box)
    if(int(fx1) > int(nx)):      
        if(int(fx1) > int(nx)):
            arduino.write (bytes("X1", 'utf-8'))
    else:
        if(int(fx2) < int(nx)):
            arduino.write (bytes("X2", 'utf-8'))
    cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()