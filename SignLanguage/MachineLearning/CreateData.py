import os
import cv2

# Setting the data directory
dataDir = 'D:/data'
if not os.path.exists(dataDir):
    os.makedirs(dataDir)

# Entering and validating the letter
letter = ''
while True:
    letter = input("Select the letter you want to add: ")
    if len(letter) == 1:
        print("Your input was: {}".format(letter))
        break
    print("Please enter a single character to continue\n")

# Camera setup
camPort = 0
videoCap = cv2.VideoCapture(camPort)
if not videoCap.isOpened():
    print("Cannot open camera")
    exit()

# Create a specific directory for the letter
if not os.path.exists(os.path.join(dataDir, letter)):
    os.makedirs(os.path.join(dataDir, letter))
print("Collecting data for class {}".format(letter))

# Collecting images
while True:
    ret, frame = videoCap.read()
    cv2.putText(frame,  'Press "Q" to continue!!!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Saving images to files
cnt = 0
datasetSize = 1000
while cnt < datasetSize:
    ret, frame = videoCap.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(25)
    cv2.imwrite(os.path.join(dataDir, letter, '{}.jpg'.format(cnt)), frame)
    cnt += 1

# Release of resources
videoCap.release()
cv2.destroyAllWindows()
