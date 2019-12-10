import pandas as pd
import numpy as np
import sklearn
from sklearn import decomposition
from sklearn.decomposition import FactorAnalysis
from sklearn.decomposition import PCA
from sklearn import datasets

import matplotlib.pyplot as plt
import pylab as plt
import seaborn as sb
from IPython.display import Image
from IPython.core.display import HTML
from pylab import rcParams

%matplotlib inline
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

iris =  datasets.load_iris()
X = iris.data
variable_names = iris.feature_names

X[0:10,]
factor = FactorAnalysis().fit(X)
pd.DataFrame(factor.components_, columns=variable_names)

#PCA
pca = decomposition.PCA()
iris_pca = pca.fit_transform(X)
pca.explained_variance_ratio_
pca.explained_variance_ratio_.sum()

comps = pd.DataFrame(pca.components_, columns=variable_names)
comps
sb.heatmap(comps)