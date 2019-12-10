import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from pylab import rcParams
import sklearn
from sklearn.cluster import DBSCAN
from collections import Counter

%matplotlib inline
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')

df = pd.read_csv(filepath_or_buffer = 'C:/Users/odoniku/Documents/DataScience/DataScience_Python/iris.data.csv',
    header=None,
    sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']
X = df.iloc[:,0:5].values
y = df.iloc[:,4].values

df[:5]

df.boxplot(return_type='dict')
plt.plot()
# with seaborn
sb.boxplot(x='Species', y='Sepal Length', data=df, palette='hls')

sb.pairplot(df, hue='Species', palette='hls')

Sepal_Width = X[:,1]
iris_outliers = (Sepal_Width > 4)
df[iris_outliers]

Sepal_Width = X[:,1]
iris_outliers = (Sepal_Width < 2.05)
df[iris_outliers]

pd.options.display.float_format = '{:.1f}'.format
X_df = pd.DataFrame(X)
print X_df.describe()

#DBScan Clustering to identify outliers
model = DBSCAN(eps=0.8, min_samples=19).fit(data)
print model
outliers_df = pd.DataFrame(data)
print Counter(model.labels_)
print outliers_df[model.labels_ ==-1]
fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1])
colors = model.labels_
ax.scatter(data[:,2], data[:,1], c=colors, s=120)
ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Width')
plt.title('DBScan for Outlier Detection')