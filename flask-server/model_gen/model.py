from flask import Flask, request, jsonify
from keras.models import model_from_json
from keras.models import Sequential
import numpy as np
from flask_cors import CORS
# import h5py
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.models import model_from_json

# Load dataset
dataset = pd.read_csv('./dataset.csv')

# Preprocess dataset
X = dataset.values[:, 0:8] 
Y = dataset.values[:, 8]
indices = np.arange(X.shape[0])
np.random.shuffle(indices)
X = X[indices]
Y = Y[indices]
Y = to_categorical(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# Creating ANN model
model = Sequential()
model.add(Dense(200, input_shape=(8,), activation='relu', name='fc1'))
model.add(Dense(200, activation='relu', name='fc2'))
model.add(Dense(2, activation='softmax', name='output'))
optimizer = Adam(lr=0.001)
model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
print('ANN Neural Network Model Summary: ')
print(model.summary())
hist = model.fit(X_train, y_train, verbose=2, batch_size=5, epochs=200)

# Evaluate model accuracy
results = model.evaluate(X_test, y_test)
ann_acc = results[1] * 100
print(ann_acc)
accuracy = hist.history
acc = accuracy['accuracy']
acc = acc[199] * 100
print("ANN model generated and its prediction accuracy is: ", acc)

print('Saved fresh model')
model.save('model.h5')