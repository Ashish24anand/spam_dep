# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 22:32:14 2021

@author: ASHISH
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 22:29:32 2021

@author: ASHISH
"""

from flask import Flask,render_template,url_for,request
import pandas as pd 

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.externals import joblib
import pickle
import joblib

# load the model from disk
filename = 'model.pkl'
clf = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('cv.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect)
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)