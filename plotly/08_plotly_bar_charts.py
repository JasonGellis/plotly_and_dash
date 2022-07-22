# plotly bar charts
# bar chars represent discrete categorical data with bars proportional to the 
# values they represent.
# generally, x = categories, y = count 

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# import the data
df = pd.read_csv('data/2018WinterOlympics.csv')

# create data and layout
# barplot should have total counts of 3 types of medals

# three traces needed for each type of medal
trace1 = go.Bar(x=df['NOC'],
                y=df['Gold'],
                name='Gold',
                marker={'color':'#FFD700'})

trace2 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                name='Silver',
                marker={'color':'#9EA0A1'})

trace3 = go.Bar(x=df['NOC'],
                y=df['Bronze'],
                name='Bronze',
                marker={'color':'#CD7F32'})

data = [trace1, trace2, trace3]
layout = go.Layout(title='Medals', barmode='stack')

# plot the figure
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='olympic_medals.html')
