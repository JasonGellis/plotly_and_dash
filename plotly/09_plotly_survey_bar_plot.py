# create a stacked bar chart. NOTE: The questions should appear as the index 
# while responses appear as column labels

# import packages
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# import data
df = pd.read_csv('data/mocksurvey.csv', index_col=0) # set questions to index

# create traces
data = [go.Bar(x=df.index,y=df[response],
               name=response) for response in df.columns]

# create layout
layout = go.Layout(
    title='Mock Survey Results',
    barmode='stack'
)

# plot the figure
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='response.html')
