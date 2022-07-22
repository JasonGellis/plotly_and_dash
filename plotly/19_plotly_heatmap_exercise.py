# Objective: Using the flights dataset create a heatmap with the followin parameters:
# x-axis = year
# y-axis = month
# z-axis = passengers

# import libraries
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# import data
df = pd.read_csv('data/flights.csv')
df.columns

# create data and layout
data = [go.Heatmap(x=df['year'],
                   y=df['month'],
                   z=df['passengers'],
                   colorscale='Jet')]

layout = go.Layout(title = 'Passenger flights 1950-1960')

# plot figure
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
