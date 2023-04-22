import numpy as np
from flask import Flask, jsonify, request
from keras.models import load_model
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

# Load the trained model
model = load_model('model.h5', compile=False)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the request
    var1 = int(request.json['account_age'])
    var2 = int(request.json['gender'])
    var3 = int(request.json['user_age'])
    var4 = int(request.json['links'])
    var5 = int(request.json['status_count'])
    var6 = int(request.json['friend_count'])
    var7 = int(request.json['loc'])
    var8 = int(request.json['loc_ip'])
    
    # Reshape the input values to match the shape of the model's input layer
    input_values = np.array([var1, var2, var3, var4, var5, var6, var7, var8])
    input_values = input_values.reshape((1, 8))
    
    # Get the prediction output from the model
    prediction = model.predict(input_values)
    
    # Convert the predicted class to a Python int and return it as JSON
    predicted_class = int(np.argmax(prediction))
    return jsonify({'prediction': predicted_class})
