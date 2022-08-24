# dashboard components - html components

# Div element = section or block of the dashboard e.g., as graph
# CSS allows you to style Div elements using dictionaries

# import libraries.
import dash
from dash import html

# create dashboard app
app = dash.Dash()

app.layout = html.Div(['This is the outermost div!', # FIRST DIV
                       html.Div( # SECOND DIV
                           ['This is an inner div!'],
                           style={'color':'red', 'border':'2px red dashed'}),
                       html.Div('Another inner div!', # THIRD DIV
                           style={'color':'blue', 'border': '3px blue solid'})], 
                      style={'color':'green', 'border':'2px green solid'}) # STYLE FOR OUTER DIV

if __name__ == '__main__':
    app.run_server()
    