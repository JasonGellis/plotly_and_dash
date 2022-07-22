# create a histogram that plots the 'length' filed from the abalone dataset.
# set the range from 0 to 1, with a bin size of 0.2

# import libraries
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# import data
df = pd.read_csv('data/abalone.csv')

# investigate data
df.info()
df.columns

# create data and layout
data = [go.Histogram(x=df['length'],
                     xbins=dict(start=0, end=1, # xbin sets a range
                                size=0.02))] # size of bin

layout = go.Layout(title='Shell lengths from the Abalone data set')

# plot figure
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
