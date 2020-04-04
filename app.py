from flask import Flask, render_template, request
import numpy as np
import joblib
import os

# TEMPLATE_DIR = os.path.abspath('templates')
# STATIC_DIR = os.path.abspath('static')
# print(1111111111111111111111111111111111111, os.listdir(TEMPLATE_DIR))
# app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app = Flask(__name__)

# Loading the model
# model_file = open('model.pkl', 'rb')
# model = joblib.load(model_file)
labels = {1:"Iris-setosa", 2:"Iris-versicolor", 3:"Iris-virginica"}

# Defining the Home page
@app.route('/')
def home():
    return render_template('index.html')

# Defining the Prediction page
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # try:
        # Taking the inputs and saving them to a variable
        SepalLength = float(request.form['SepalLength'])
        SepalWidth  = float(request.form['SepalWidth'])
        PetalLength = float(request.form['PetalLength'])
        PetalWidth  = float(request.form['PetalWidth'])
        
        # Converting the inputs into a numpy array
        pred_args = np.array([SepalLength, SepalWidth, PetalLength, PetalWidth]).reshape(1, -1)
        
        # Predicting the Label
        model_prediction = model.predict(pred_args)[0]
        model_prediction = labels[model_prediction]

        # except:
        #     return 'Invalid Values entered!'

    return render_template('index.html', prediction = model_prediction)


if __name__ == '__main__':
    app.run(port='8888', debug=True)