import tkinter as tk
from tkinter import Label, Text, messagebox
from PIL import Image, ImageTk
import cv2
import mediapipe as mp
import pickle
import numpy as np
import time


class MainFrame:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = tk.Frame(self.root, padx=20, pady=20)

        self.label = None

        self.textBox = None

        self.closeCameraButton = None
        self.openCameraButton = None
        self.buttonLogout = None

        self.streakThreshold = None
        self.currentStreak = None
        self.lastPrediction = None
        self.lastPredictionTime = None

        self.model = None
        self.modelDict = None
        self.hands = None
        self.mpDrawingStyles = None
        self.mpDrawing = None
        self.mpHands = None
        self.videoCap = None
        self.camPort = None

        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.frame)
        self.label.pack()

        # Open camera button
        self.openCameraButton = tk.Button(self.frame, text="Open Camera", command=self.open_camera)
        self.openCameraButton.pack(pady=5)

        # Logout button
        self.buttonLogout = tk.Button(self.frame, text="Logout", command=self.app.show_login_frame)
        self.buttonLogout.pack(pady=5)

        # Close camera button
        self.closeCameraButton = tk.Button(self.frame, text="Close Camera", command=self.close_camera)

        self.textBox = Text(self.frame, height=5, width=50)

        self.lastPredictionTime = time.time()
        self.lastPrediction = None
        self.currentStreak = 0
        self.streakThreshold = 3  # seconds

        self.camPort = 0
        self.videoCap = None
        self.mpHands = mp.solutions.hands
        self.mpDrawing = mp.solutions.drawing_utils
        self.mpDrawingStyles = mp.solutions.drawing_styles

        self.hands = self.mpHands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.2)

        self.modelDict = None
        self.model = None

    def open_camera(self):
        self.videoCap = cv2.VideoCapture(self.camPort)

        if not self.videoCap.isOpened():
            messagebox.showerror("Error", "Could not open webcam")
            return

        self.openCameraButton.pack_forget()
        self.buttonLogout.pack_forget()
        self.textBox.pack(pady=5)
        self.closeCameraButton.pack(pady=5)

        self.open_model()
        self.process_frames()

    def open_model(self):
        file = open('C:/Users/Teoc/Desktop/Licenta/Proiect GIT/SL/MachineLearning/model.pickle', 'rb')
        self.modelDict = pickle.load(file)
        self.model = self.modelDict['model']
        file.close()

    def process_frames(self):
        if self.videoCap is None or not self.videoCap.isOpened():
            return

        dataAux = []
        xCoord = []
        yCoord = []

        success, frame = self.videoCap.read()
        if not success:
            messagebox.showerror("Error", "Failed to capture image")
            return

        height, width, _ = frame.shape

        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mpDrawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mpHands.HAND_CONNECTIONS,
                    self.mpDrawingStyles.get_default_hand_landmarks_style(),
                    self.mpDrawingStyles.get_default_hand_connections_style()
                )

            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    dataAux.append(hand_landmarks.landmark[i].x)
                    dataAux.append(hand_landmarks.landmark[i].y)
                    xCoord.append(hand_landmarks.landmark[i].x)
                    yCoord.append(hand_landmarks.landmark[i].y)

            x1 = int(min(xCoord) * width) - 25
            y1 = int(min(yCoord) * height) - 25

            x2 = int(max(xCoord) * width) + 25
            y2 = int(max(yCoord) * height) + 25

            prediction = self.model.predict([np.asarray(dataAux)])
            predictedCharacter = prediction[0]

            currentTime = time.time()
            if predictedCharacter == self.lastPrediction:
                if currentTime - self.lastPredictionTime >= self.streakThreshold:
                    self.textBox.insert(tk.END, predictedCharacter)
                    self.lastPredictionTime = currentTime
            else:
                self.lastPrediction = predictedCharacter
                self.lastPredictionTime = currentTime

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(frame, predictedCharacter, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
        else:
            self.lastPrediction = None
            self.lastPredictionTime = time.time()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_pil = Image.fromarray(frame)
        frame_tk = ImageTk.PhotoImage(image=frame_pil)

        self.label.imgtk = frame_tk
        self.label.configure(image=frame_tk)

        self.frame.after(10, self.process_frames)

    def close_camera(self):
        if self.videoCap:
            self.videoCap.release()
            self.videoCap = None
            self.label.configure(image='')

            self.closeCameraButton.pack_forget()
            self.textBox.pack_forget()
            self.openCameraButton.pack(pady=5)
            self.buttonLogout.pack(pady=5)

    def pack(self):
        self.frame.pack(pady=10)

    def unpack(self):
        self.frame.pack_forget()
