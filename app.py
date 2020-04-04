from flask import Flask, render_template, request
import numpy as np
import joblib
import os, time

app = Flask(__name__)

# Loading the model
# model_file = open('model.pkl', 'rb')
# model = joblib.load(model_file)
# labels = {1:"Iris-setosa", 2:"Iris-versicolor", 3:"Iris-virginica"}

# Defining the Home page
@app.route('/')
def home():
    return render_template('index.html')


# Defining the Prediction page
@app.route('/', methods=['GET', 'POST'])
def predict():
	print(time.time(), request.method)
	try:
		if request.method == 'POST':
			print('Entering post', time.time())
			# print(request.form['test'])
			fname = request.form['fname']
			print(9999999999999999999999999999999999, fname)
	except:
		pass

	return render_template('index.html', FILENAME=fname)



if __name__ == '__main__':
    app.run(port=3444, debug=True)