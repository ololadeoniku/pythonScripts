import numpy as np
import pandas as pd

import urllib

import sklearn
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
raw_data = urllib.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=",")
print dataset[0]

X = dataset[:,0:48]

y = dataset[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=17)

BernNB = BernoulliNB(binarize=True)
BernNB.fit(X_train, y_train)
print(BernNB)
y_expect = y_test
y_pred = BernNB.predict(X_test)
print accuracy_score(y_expect, y_pred)

MultiNB = MultinomialNB()

MultiNB.fit(X_train, y_train)
print(MultiNB)
y_pred = MultiNB.predict(X_test)
print accuracy_score(y_expect, y_pred)

GausNB = GaussianNB()
GausNB.fit(X_train, y_train)
print(GausNB)
y_pred = GausNB.predict(X_test)
print accuracy_score(y_expect, y_pred)

BernNB = BernoulliNB(binarize=0.1)
BernNB.fit(X_train, y_train)
print(BernNB)
y_expect = y_test
y_pred = BernNB.predict(X_test)
print accuracy_score(y_expect, y_pred)