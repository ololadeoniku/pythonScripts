#!/usr/bin/python3
# This is a template for Python scripts

#import library
#Import other necessary libraries like pandas, numpy...
import pandas
import sklearn

from sklearn import linear_model
from sklearn.linear_model import LogisticRegression


class LogisticR:

    def __init__(self):


    def LogicParam(self):
        # Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset

        # Create logistic regression object
        model = LogisticRegression()

        # Train the model using the training sets and check score
        model.fit(X, y)
        model.score(X, y)

        # Equation coefficient and Intercept
        print('Coefficient: \n', model.coef_)
        print('Intercept: \n', model.intercept_)

        # Predict Output
        predicted = model.predict(x_test)
        return predicted

def main():
    myResult = LogisticR()
    myFinalResult = myResult.LogicParam()
    print(myFinalResult)


if __name__ == '__main__': main()

#FROM DATA SCIENCE COURSE
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy.stats import spearmanr

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.preprocessing import scale
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn import preprocessing

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

address = ''
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.head()

cars_data = cars.ix[:,(5,11)].values
cars_data_names = ['drat','carb']
y = cars.ix[:,9].values

sb.regplot(x='drat', y='carb', data=cars, scatter=True)

drat = cars['drat']
carb = cars['carb']

spearmanr_coefficient, p_value =  spearmanr(drat, carb)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)

cars.isnull().sum()
sb.countplot(x='am', data=cars, palette='hls')
cars.info()

X = scale(cars_data)

LogReg = LogisticRegression()

LogReg.fit(X,y)
print LogReg.score(X,y)

y_pred = LogReg.predict(X)
from sklearn.metrics import classification_report
print(classification_report(y, y_pred))