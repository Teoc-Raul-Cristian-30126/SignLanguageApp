import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Loading data
file = open('data.pickle', 'rb')
dataDict = pickle.load(file)
file.close()

# Converting data and labels to numpy arrays
data = np.asarray(dataDict['data'])
labels = np.asarray(dataDict['labels'])

# Splitting data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data, labels,
                                                    test_size=0.3,
                                                    shuffle=True,
                                                    stratify=labels)

# Training the RandomForestClassifier model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Saving the trained model
file = open('model.pickle', 'wb')
pickle.dump({'model': model}, file)
file.close()
