# Dash lets you insert Plotly plots directly

import dash
from dash import dcc
from dash import html# Dash layouts (following dash documentation)
import plotly.graph_objs as go
import numpy as np

app = dash.Dash() # creates a dash application

# create data
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

app.layout = html.Div([dcc.Graph(id ='scatterplot', # dcc.Graph calls the plotly figure\s
                                 figure = {'data':[ # this data list is the same as 'Data' from plotly.
                                         go.Scatter( # go.Scatter from plotly
                                             x=random_x,
                                             y=random_y,
                                             mode='markers',
                                             marker = {
                                                 'size':12,
                                                 'color': 'rgb(51, 204, 154)',
                                                 'symbol':'pentagon',
                                                 'line':{'width':2}
                                             }
                                             )],
                                           'layout': go.Layout( # this go.Layout is the same as 'layout' from plotly.
                                               title='Scatterplot',
                                               xaxis={'title': 'X axis title'})}
                                 )]) 

if __name__ == '__main__':
    app.run_server()
