# Add style calls to html components

import dash
from dash import dcc
from dash import html# Dash layouts (following dash documentation)

app = dash.Dash() # creates a dash (flask-like) application

# create a color dictionary that can be called
colors = {'background': '#111111', 'text': '#7FDBFF'}

app.layout = html.Div(children =[ # 'div' tag is an empty container that is used to define a division or a section. It does not affect the content or layout
    html.H1('Hello Dash!', style={'textAlign': 'center',
                                  'color':colors['text']}), # H1 = header 1
    dcc.Graph(id='example',
              figure={'data':[ 
                  {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'SF'}, 
                  {'x':[1,2,3],'y':[2,4,5],'type':'bar','name':'NYC'}
                  ], 
                      'layout':{ 
                      'plot_bgcolor': colors['background'],
                      'paper_bgcolor':colors['background'],
                      'font':{'color': colors['text']},
                      'title':'Bar Plots!'
                      }}) 
    ], style = {'backgroundColor':colors['background']})

if __name__ == '__main__':
    app.run_server()
