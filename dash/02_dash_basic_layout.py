# Dash layouts (following dash documentation)

# Main ideas:
    # 1) There are specific libraries
    # 2) Call the layout
    # 3) set the div
    # 4) setup html components
        
import dash
from dash import dcc
from dash import html

app = dash.Dash() # creates a dash (flask-like) application

app.layout = html.Div(children =[ # 'div' tag is an empty container that is used to define a division or a section. It does not affect the content or layout
    html.H1('Hello Dash!'), # H1 = header 1
    html.Div('Dash: Dashboards with Python'),
    dcc.Graph(id='example',
              figure={'data':[ # data from plotly
                  {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'SF'}, 
                  {'x':[1,2,3],'y':[2,4,5],'type':'bar','name':'NYC'}
                  ], 
                      'layout':{ # data from plotly
                      'title':'Bar Plots!'
                      }}) 
    ]) 

if __name__ == '__main__':
    app.run_server()
