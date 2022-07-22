# creating scatter plots with plotly
# scatter plots allow for comparison of two (or more) variables for a set of data.

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Create random data seed
np.random.seed(42)

random_x = np.random.randint(1, 101, 100) # single column of 100 random integers
random_y = np.random.randint(1, 101, 100)

# ploty uses a strange syntax (in which the plot is an object nested a variable 
# called data), and then call that variable for the actual plot.

# plot the data using markers (dots)
data = [go.Scatter(x=random_x, # create the data variable as a list
                   y=random_y,
                   mode='markers',
                   marker = dict(
                       size=12,
                       color='rgb(51,204,153)',
                       symbol='pentagon',
                       line={'width':2}
                       ))] 
layout = go.Layout(title='Hello First Plot', # create the layout variable
                    xaxis=dict(title='MY X AXIS'), # use a dictionary call
                    yaxis=dict(title='MY Y AXIS'),
                    hovermode='closest') # lets you see x and y coords
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename = 'scatter.html')
