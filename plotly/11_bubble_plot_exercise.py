# creat a bubble chart that compares three features from the mpg.csv data set

# import libraries
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# import data
df = pd.read_csv('data/mpg.csv')

# column names
df.columns
# ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight','acceleration', 
# 'model_year', 'origin', 'name']

# horsepower is an object and has '?'. These need to be replaced with NaN 
# and made into floats for use with marker size in the bubble plot
df['horsepower']=df['horsepower'].replace('?', np.NaN)
df['horsepower']=df['horsepower'].astype(float)


# create data and layout
data = [go.Scatter(x=df['model_year'],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['cylinders'],
                   color=df['horsepower'],
                   showscale=True))]

layout=go.Layout(title='Vehicle mpg vs model year',
                 xaxis=dict(title='model year'),
                   yaxis=dict(title='mpg'))

fig=go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble_chart_exercise.html')
