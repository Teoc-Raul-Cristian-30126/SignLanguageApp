import pickle
import cv2
import mediapipe as mp
import numpy as np

# Loading the saved model
file = open('./model.pickle', 'rb')
modelDict = pickle.load(file)
model = modelDict['model']
file.close()

# Camera setup
camPort = 0
videoCap = cv2.VideoCapture(camPort)
if not videoCap.isOpened():
    print("Cannot open camera")
    exit()

# Configuring MediaPipe for hand detection
mpHands = mp.solutions.hands
mpDrawing = mp.solutions.drawing_utils
mpDrawingStyles = mp.solutions.drawing_styles

hands = mpHands.Hands(static_image_mode=True,
                      max_num_hands=1,
                      min_detection_confidence=0.2)

# Loop image processing
while True:
    dataAux = []
    xCoord = []
    yCoord = []

    ret, frame = videoCap.read()
    height, width, _ = frame.shape

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mpDrawing.draw_landmarks(
                frame,
                hand_landmarks,
                mpHands.HAND_CONNECTIONS,
                mpDrawingStyles.get_default_hand_landmarks_style(),
                mpDrawingStyles.get_default_hand_connections_style()
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

        prediction = model.predict([np.asarray(dataAux)])
        predictedCharacter = prediction[0]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(frame, predictedCharacter, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release of resources
videoCap.release()
cv2.destroyAllWindows()
