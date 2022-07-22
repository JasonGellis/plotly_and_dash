# bubble charts are like scatter plots but include size, relative to input, 
# and colour coding.

# import libraries
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# import data
df = pd.read_csv('data/mpg.csv')

# investigate data
print(df.columns)

# data and layout
data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text=df['name'], # text gives information when hovering over a point
                   mode='markers',
                   marker=dict(size=df['weight']/100, # divide by 100 as weight is so large
                   color = df['cylinders'],
                   showscale=True))] 

layout=go.Layout(title='Vehicle mpg. vs horsepower',
                 xaxis= dict(title='horsepower'),
                 yaxis=dict(title='mpg.'),
                 hovermode='closest') # closest marker to cursor

# plot
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='mpg.html')
