# dash core components - https://dash.plotly.com/dash-core-components

# import libraries
import dash
from dash import dcc
from dash import html

# create dashboaard app
app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options=[{'label':'New York City', # label is what the user sees
                           'value':'NYC'},# NYC is the value passed back to the dashboard.
                          {'label': 'San Francisco',
                           'value':'SF'}],
                 value='SF'), # default value for the dropdown menu
    
    html.Label('Slider'),
    dcc.Slider(min=-10, max=10, step=0.5, value=0,
               marks = {i: i for i in range(-10,10)}),
    
    html.P(html.Label('Some Radio Items')), # html.P will create a line break and stop div overlap
    dcc.RadioItems(options=[{'label':'New York City', # label is what the user sees
                           'value':'NYC'},# NYC is the value passed back to the dashboard.
                          {'label': 'San Francisco',
                           'value':'SF'}],
                   value='SF') # default value for buttons
    ])

if __name__ == '__main__':
    app.run_server()
    