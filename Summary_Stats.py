import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import scipy
from scipy import stats

np.set_printoptions(precision=2)
aa = np.array([[2.,4.,6.], [1.,3.,5.], [10.,20.,30.]])
bb = np.array([[0.,1.,2.], [3.,4.,5.], [6.,7.,8.]])
aa*bb
np.dot(aa,bb)

address = ''
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.index = cars.car_names
cars.head(15)

cars.head()
cars.sum()
cars.sum(axis=1)
cars.median()
cars.mean()
cars.max()

mpg = cars.mpg
mpg.idxmax()

cars.std()
cars.var()
cars.describe()

cars_cat = cars[['cyl','vs','am','gear','carb']]
cars_cat.head()

gear = cars.gear
gear.value_counts()
gears_group = cars_cat.groupby('gear')
gears_group.describe()
cars['group'] = pd.Series(cars.gear, dtype="category")
pd.crosstab(cars['am'], cars['gear'])
