from django.shortcuts import render
from django.http import HttpResponse
from . import forms
import pandas as pd
import pandas as pd
import numpy as np
import re
import string
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.metrics import confusion_matrix, auc, roc_auc_score, roc_curve, classification_report

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import pickle


# Create your views here.
def index(request):
	return render(request,'index.html')
def predict(request):
	if request.method=='POST':
		form=forms.Predict(request.POST)
		if form.is_valid():
			news=form.cleaned_data['comments']
			train=list(news)
			data=pd.read_csv("D:\\machine learning progrom\\dataset\\Participants_Data_News_category-20190729T063600Z-001\\om.csv")
			x=data.STORY

			y=data.SECTION
			x1=x
			cv = CountVectorizer()
			cv=cv.fit_transform(x1)
			train=cv.transform(train).toarray()

			
			vect=pickle.load(open("D:\\machine learning progrom\\dataset\\Participants_Data_News_category-20190729T063600Z-001\\django\\mysite\\vecter.pick","rb"))
			model=pickle.load(open("D:\\machine learning progrom\\dataset\\Participants_Data_News_category-20190729T063600Z-001\\django\\mysite\\model.pick",'rb'))
			
			pre=model.predict(train)
			print(r)
			return render(request,'label.html',{'label':pre})

		else:
			messege='invalid data '
			return render(request,'index.html',{'error':messege})


