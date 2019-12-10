#!/usr/bin/python3
# This is a template for Python scripts

#import library
#Import other necessary libraries like pandas, numpy...
import pandas
import sklearn

from sklearn import linear_model


class LinearR:

    # def __init__(self):
        


    def SingleParam(self):
        #self.variable()
        # Load Train and Test datasets
        # Identify feature and response variable(s) and values must be numeric and numpy arrays
        x_train = [0, 2, 3 ,5, 10, 21, 30, 5, 6, 9].reshape(1,-1)
        y_train = [40, 50, 35, 23, 21, 15, 16, 18, 90, 58].reshape(1,-1)
        x_test = [9, 4, 3, 5, 6, 2, 16, 3, 7].reshape(1,-1)

        # Create linear regression object
        linear = linear_model.LinearRegression()
        print(linear)

        # Train the model using the training sets and check score
        linear.fit(x_train, y_train)
        linear.score(x_train, y_train)

        # Equation coefficient and Intercept
        print('Coefficient: \n', linear.coef_)
        print('Intercept: \n', linear.intercept_)

        # Predict Output
        predicted = linear.predict(x_test)
        return predicted

def main():
    myResult = LinearR()
    myFinalResult = myResult.SingleParam()
    print(myFinalResult)


if __name__ == '__main__': 
    main()


# #FROM DATA SCIENCE TUTORIAL
# import numpy as np
# import pandas as pd

# import matplotlib.pyplot as plt
# from pylab import rcParams
# import seaborn as sb

# import sklearn
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import scale
# from collections import Counter

# %matplotlib inline
# rcParams['figure.figsize'] = 5, 4
# sb.set_style('whitegrid')

# address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch08/08_01/enrollment_forecast.csv'
# enroll = pd.read_csv(address)
# enroll.columns = ['year','roll','unem', 'hgrad', 'inc']
# enroll.head()

# sb.pairplot(enroll)

# print(enroll.corr())

# enroll_data = enroll.ix[:,(2,3)].values
# enroll_target = enroll.ix[:,1].values
# enroll_data_names = ['unem', 'hgrad']

# X, y = scale(enroll_data), enroll_target

# missing_values = X==np.NAN
# X[missing_values == True]

# LinReg = LinearRegression(normalize=True)

# LinReg.fit(X,y)

# print(LinReg.score(X,y))