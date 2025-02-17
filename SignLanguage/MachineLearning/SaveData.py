import os
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import pickle

# Data directory
dataDir = 'D:/data'

# Configuring MediaPipe for hand recognition
mpHands = mp.solutions.hands
mpDrawing = mp.solutions.drawing_utils
mpDrawingStyles = mp.solutions.drawing_styles

hands = mpHands.Hands(static_image_mode=True,
                      max_num_hands=1,
                      min_detection_confidence=0.3)

# Checking images
letter = ''
checkImg = input("Do you want to check the images? (Y/N): ")
if checkImg == 'Y':
    while True:
        letter = input("Select the letter you want to check: ")
        if len(letter) == 1:
            if not os.path.exists(os.path.join(dataDir, letter)):
                print("This letter does not exist in your model!!!")
                break

            for imgPath in os.listdir(os.path.join(dataDir, letter))[:20]:
                img = cv2.imread(os.path.join(dataDir, letter, imgPath))
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                results = hands.process(imgRGB)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mpDrawing.draw_landmarks(
                            imgRGB,
                            hand_landmarks,
                            mpHands.HAND_CONNECTIONS,
                            mpDrawingStyles.get_default_hand_landmarks_style(),
                            mpDrawingStyles.get_default_hand_connections_style()
                        )

                plt.figure()
                plt.imshow(imgRGB)
            plt.show()

            print("Your input was: {}".format(letter))
            break
        print("Please enter a single character to continue\n")

# Saving data
saveData = input("Do you want to save the data? (Y/N): ")
if saveData == 'Y':
    data = []
    labels = []
    for dirList in os.listdir(dataDir):
        for imgPath in os.listdir(os.path.join(dataDir, dirList)):
            dataAUX = []

            img = cv2.imread(os.path.join(dataDir, dirList, imgPath))
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            results = hands.process(imgRGB)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        dataAUX.append(hand_landmarks.landmark[i].x)
                        dataAUX.append(hand_landmarks.landmark[i].y)
                data.append(dataAUX)
                labels.append(dirList)

    file = open('data.pickle', 'wb')
    pickle.dump({'data': data, 'labels': labels}, file)
    file.close()
