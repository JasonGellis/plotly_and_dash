# A line chart displays a series of data points (markers) connected by line segments.
# It is similar to a scatter plot except that the measurement points are ordered
# (typically by their x-axis value) and joined by straight line segments.
# They are often used to visualize trend data over time - a time series.

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# set random seed
np.random.seed(56)

x_values = np.linspace(0,1,100) # 100 hundred numbers, evenly spaced between 0 and 1
y_values = np.random.randn(100) # 100 numbers from a random normal distribution

# for organization, plotly syntax calls every line on a figure a 'trace'. 
# each trace is passed to data
trace0 = go.Scatter(x=x_values,
                   y=y_values+5, # add 5 to every value from y_values
                   mode='markers',
                   name='markers') 
trace1 = go.Scatter(x=x_values,
                    y=y_values,
                    mode='lines',
                    name='lines')
trace2 = go.Scatter(x=x_values,
                    y=y_values-5, # minus 5 to every value from y_values
                    mode='lines+markers',
                    name='lines and markers')

# setup data and layout
data = [trace0, trace1, trace2]
layout = go.Layout(title='Line Chart')

# create the figure
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename='Line Chart.html')
