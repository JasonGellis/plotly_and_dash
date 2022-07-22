# histograms - are for continuous data. If categorical use a bar chart.
# increase bin size makes the bar wider, and the number of bins less.

# import libraries
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# import data
df = pd.read_csv('data/mpg.csv')

# create the data and layout
data = [go.Histogram(x=df['mpg'],
                     xbins=dict(start=0, end=50, # xbin sets a range
                                size=5))] # size of bin
layout = go.Layout(title='Histogram of mpg')

# plot
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
