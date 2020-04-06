from fastai.vision import *

from flask import Flask, render_template, request, redirect
import numpy as np
import joblib
import os, time
from PIL import Image
import numpy as np
import requests

defaults.device = torch.device('cpu')

app  = Flask(__name__)

path = os.getcwd()


def download_model():
	url = 'https://drive.google.com/uc?export=download&id=1--EXz8nu4ecEkXkdmt7Nh2kEe2b4jf9W'
	r = requests.get(url, allow_redirects=True)
	open('export.pkl', 'wb').write(r.content)


# Checking if user_file folder is present in the server, if not, downloading.
if 'user_files' not in os.listdir():
	os.mkdir('user_files')
# user_file : It'll contain the images uploaded by the user temporarily


# Checking if model file is present in the server, if not, downloading.
if 'export.pkl' not in os.listdir():
	print('Donwloading the model...', '\n')
	download_model()
else:
	print('Model present..................................!')

# Loading the model file
model_file = open('export.pkl', 'rb')
model = load_learner(path)



print(os.getcwd(), os.listdir())
app.config["IMAGE_UPLOADS"] = os.getcwd()+'/user_files'


def predict_the_character(fpath):
	chars = ['chandler', 'joey', 'monica', 'phoebe', 'rachel', 'ross']

	img = open_image(fpath)
	pred_class, pred_idx, outputs = model.predict(img)
	prob_distribution = {char : float('{0:.2f}'.format(prob)) for char, prob in zip(chars, ((outputs/sum(outputs))*100).tolist())}

	return pred_class, prob_distribution


# Defining the Home page
@app.route('/')
def home():
    return render_template('index.html')


# Defining the Prediction page
@app.route('/predict', methods=['GET', 'POST'])
def predict(character='', prob_distribution=''):
	print(time.time(), request.method)
	# try:
	if request.method == 'POST':
		print('Entering post', time.time())
		if request.form:
			# Reading the POST request
			fname = request.files['fname']

			# Saving the Image file in local env
			fpath = os.path.join(app.config["IMAGE_UPLOADS"], fname.filename)
			fname.save(fpath)
			print(fpath)
			print(fname.filename, 'saved successfully!')


			character, prob_distribution = predict_the_character(fpath)
			print(prob_distribution)

			# Deleting the file from the database
			os.remove(fpath)

		# return redirect(request.url)
	# except:
	# 	print('Some error!!!!!!!!!!!!!!')

	return render_template('index.html', 
							PREDICTED_CHARACTER=character,
							PROBABILITY_DIST=prob_distribution)



if __name__ == '__main__':


	# INITIALIZING THE SERVER
	app.run(port=7321, debug=True)
