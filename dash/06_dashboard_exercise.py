# create a dashboard

# Old Faithful has a bi-modal eruption interval
# Build a dashboard that imports the old fiathful data and displays a scatterplot.
# The field names are:
    # D = dates of recodings by month (August)
    # X = duration of the current eruption in minutes (to nearest 0.1 minute)
    # Y waiting time until the next eruption in minutes (to nearest minute)
    
# import libraries.
import dash
from dash import dcc
from dash import html# Dash layouts (following dash documentation)
import plotly.graph_objs as go
import pandas as pd

# import data
df = pd.read_csv('data/OldFaithful.csv')

# investigate data
df.columns
df.info()

# create the dashboard application
app = dash.Dash() # creates a dash application

app.layout = html.Div([dcc.Graph(id ='old_faithful', # dcc.Graph calls the plotly figure\s
                                 figure = {'data':[ # this data list is the same as 'Data' from plotly.
                                         go.Scatter( # go.Scatter from plotly
                                             x=df['X'],
                                             y=df['Y'],
                                             mode='markers',
                                             marker = {
                                                 'color': 'rgb(51, 204, 200)',
                                                 'symbol':'circle',
                                                 'line':{'width':1}
                                             }
                                             )],
                                           'layout': go.Layout( # this go.Layout is the same as 'layout' from plotly.
                                               title='Old Faithful eruption intervals',
                                               xaxis={'title': 'Duration of the current eruption in minutes (to nearest 0.1 minute)'},
                                               yaxis={'title': 'Interval to next eruption in minutes'})}
                                 )]) 

if __name__ == '__main__':
    app.run_server()
