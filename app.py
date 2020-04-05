from flask import Flask, render_template, request, redirect
import numpy as np
import joblib
import os, time
from PIL import Image
import numpy as np

app = Flask(__name__)


# Creating a user_file folder if not present in the working dir
if 'user_files' not in os.listdir():
	os.mkdir('user_files')
# user_file : It'll contain the images uploaded by the user temporarily

print(os.getcwd(), os.listdir())
app.config["IMAGE_UPLOADS"] = os.getcwd()+'/user_files'


# Loading the model
# model_file = open('model.pkl', 'rb')
# model = joblib.load(model_file)
# labels = {1:"Iris-setosa", 2:"Iris-versicolor", 3:"Iris-virginica"}

def predict_the_character(image):
	return f'popu {time.time()}'

# Defining the Home page
@app.route('/')
def home():
    return render_template('index.html')


# Defining the Prediction page
@app.route('/', methods=['GET', 'POST'])
def predict():
	print(time.time(), request.method)
	# try:
	if request.method == 'POST':
		print('Entering post', time.time())
		if request.form:
			# Reading the POST request
			fname = request.files['fname']

			# Saving the Image file in local env
			path = os.path.join(app.config["IMAGE_UPLOADS"], fname.filename)
			fname.save(path)
			print(path)
			print(fname.filename, 'saved successfully!')

			# Reading the Image from the database
			data = Image.open(path)
			if data.mode == 'RGBA':
				data = data.convert('RGB')

			# Conrting the PIL Image into numpy array
			img = np.array(data)
			print(img.shape)

			character = predict_the_character(img)

			# Deleting the file from the database
			os.remove(path)

		# return redirect(request.url)
	# except:
	# 	print('Some error!!!!!!!!!!!!!!')

	return render_template('index.html', PREDICTED_CHARACTER=character)



if __name__ == '__main__':
    app.run(port=7117, debug=True)
