pip install Plotly
import numpy as np
import pandas as pd

import cufflinks as cf

import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

import numpy as np
import pandas as pd

import cufflinks as cf

import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

import sklearn
from sklearn.preprocessing import StandardScaler

tls.set_credentials_file(username='bigdatagal', api_key='hvginfgvwe')
a = np.linspace(start=0, stop=36, num=36)

np.random.seed(25)
b = np.random.uniform(low=0.0, high=1.0, size=36)
trace = go.Scatter(x=a, y=b)
data = [trace]

py.iplot(data, filename='basic-line-chart')

x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,0,4,3,2,1]
z = [10,9,8,7,6,5,4,3,2,1]

trace0 = go.Scatter(x=x, y=y, name='List Object', line = dict(width=5))
trace1 = go.Scatter(x=x, y=z, name='List Object 2', line = dict(width=10,))

data = [trace0, trace1]

layout = dict(title='Double Line Chart', xaxis= dict(title='x-axis'), yaxis= dict(title='y-axis'))
print layout

fig = dict(data=data, layout=layout)
print fig

py.iplot(fig, filename='styled-line-chart')

address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch09/09_01/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

df = cars[['cyl', 'wt','mpg']]
layout = dict(title = 'Chart From Pandas DataFrame', xaxis= dict(title='x-axis'), yaxis= dict(title='y-axis'))
df.iplot(filename='cf-simple-line-chart', layout=layout)

data = [go.Bar(x=[1,2,3,4,5,6,7,8,9,10],y=[1,2,3,4,0.5,4,3,2,1])]
print data

layout = dict(title='Simple Bar Chart',
             xaxis = dict(title='x-axis'),
             yaxis = dict(title='y-axis'))
py.iplot(data, filename='basic-bar-chart', layout=layout)

color_theme = dict(color=['rgba(169,169,169,1)', 'rgba(255,160,122,1)','rgba(176,224,230,1)', 'rgba(255,228,196,1)',
                          'rgba(189,183,107,1)', 'rgba(188,143,143,1)','rgba(221,160,221,1)'])
print color_theme

trace0 = go.Bar(x=[1,2,3,4,5,6,7], y=[1,2,3,4,0.5,3,1], marker=color_theme)
data = [trace0]
layout = go.Layout(title='Custom Colors')
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='color-bar-chart')

fig = {'data': [{'labels': ['bicycle', 'motorbike', 'car', 'van', 'stroller'],
                 'values': [1, 2, 3, 4, 0.5], 'type': 'pie'}],
       'layout': {'title': 'Simple Pie Chart'}}
py.iplot(fig)

address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch09/09_02/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg

mpg.iplot(kind='histogram', filename='simple-histogram-chart')

cars_data = cars.ix[:,(1,3,4)].values

cars_data_std = StandardScaler().fit_transform(cars_data)

cars_select = pd.DataFrame(cars_data_std)
cars_select.columns = ['mpg', 'disp', 'hp']

cars_select.iplot(kind='histogram', filename='multiple-histogram-chart')

cars_select.iplot(kind='histogram', subplots=True, filename='subplot-histograms')

cars_select.iplot(kind='histogram', subplots=True, shape=(3,1), filename='subplot-histograms')

cars_select.iplot(kind='histogram', subplots=True, shape=(1, 3), filename='subplot-histograms')

cars_select.iplot(kind='box', filename='box-plots')

fig = {'data':[{'x':cars_select.mpg, 'y':cars_select.disp, 'mode':'markers','name':'mpg'},
              {'x':cars_select.hp, 'y':cars_select.disp,'mode':'markers', 'name':'hp'}]
      , 'layout':{'xaxis':{'title':''}, 'yaxis':{'title':'Standardized Displacement'}}}
py.iplot(fig, filename='grouped-scatter-plot')