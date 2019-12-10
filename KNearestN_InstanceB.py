import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from pylab import rcParams

import urllib

import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics

np.set_printoptions(precision=4, suppress=True)
# %matplotlib inline
rcParams['figure.figsize'] = 7, 4
plt.style.use('seaborn-whitegrid')

address = ''
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

X_prime = cars.ix[:,(1,3,4,6)].values
y = cars.ix[:,9].values
X = preprocessing.scale(X_prime)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=17)
clf = neighbors.KNeighborsClassifier()
#KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
#  metric_params=None, n_jobs=1, n_neighbors=5, p=2,
# weights='uniform')

clf.fit(X_train, y_train)
print(clf)

y_expect = y_test
y_pred = clf.predict(X_test)
print(metrics.classification_report(y_expect, y_pred))