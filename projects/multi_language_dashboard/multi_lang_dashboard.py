import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import json
import pandas as pd
from dash.dependencies import Input, Output
from dash import no_update
import dash_bootstrap_components as dbc


# Import the json languages file.
lang = json.load(open('languages.json', 'r', encoding='UTF-8'))

# import the data
df = pd.read_csv('OldFaithful.csv')

# create language dropdown menu
lang_options = {'en': 'English', 'de': 'German', 'es': 'Spanish', 'fr': 'French'}
lang_dropdown = html.Div(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(L, id=S, className='rounded-2') for S, L in lang_options.items()
            ],
            label='Language',
            toggleClassName='dropdown-menu-dark',
            color='secondary',
            menu_variant = 'secondary',
            className="",
            id = 'lang-dropdown'
        ),
    ], className='p-4 border border-info'
)

# create the scatter plot
graph = dcc.Graph(
        id='old_faithful',
        config=dict(locale='fr'),
        figure={
            'data': [
                go.Scatter(
                    x=df['X'],
                    y=df['Y'],
                    mode='markers'
                )
            ],
            'layout': go.Layout(
                title='Old Faithful Eruptions',  # 'Eruptions' part of title needs to change languages
                xaxis={
                    'title': 'Duration (in minutes)'  # x-axis needs to change languages
                },
                yaxis={
                    'title': 'Interval (in minutes)'  # y-axis needs to change languages
                },
                hovermode='closest'
            )
        },
    )

# create the app
external_stylesheets = [dbc.themes.BOOTSTRAP, 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']

app = dash.Dash(external_stylesheets=external_stylesheets)

# Create a Dash layout:
app.layout = html.Div([
    # drop down component
    lang_dropdown,
    
    # graph component
    html.Div([
        graph
    ], id='graph-container')
])


# call back
@app.callback(
   [
       Output('graph-container', 'children'),
       Output('lang-dropdown', 'label')
   ],
    [
        Input('en', 'n_clicks'),
        Input('de', 'n_clicks'),
        Input('es', 'n_clicks'),
        Input('fr', 'n_clicks'),
    ]
)

# call back
def make_graph(*args): 
    ctx = dash.callback_context

    if not ctx.triggered:
        return no_update, no_update
    else:
        lang_selection = ctx.triggered[0]['prop_id'].split('.')[0]
    
    lang= json.load(open('languages.json', 'r'))

    title = (lang[0]['text'][lang_selection])  # change the title
    xaxis = (lang[1]['text'][lang_selection])  # change the x-axis
    yaxis = (lang[2]['text'][lang_selection])  # change the y-axis
    xaxis_2 = (lang[3]['text'][lang_selection]) # change portion of x-axis in parentheses
    yaxis_2 = (lang[3]['text'][lang_selection]) # change portion of y-axis in parentheses

    
    graph2 = dcc.Graph(
        id='old_faithful',
        figure={
            'data': [
                go.Scatter(
                    x=df['X'],
                    y=df['Y'],
                    mode="markers"
                )
            ],
            'layout': go.Layout(
                title=f'Old Faithful {title}',  # part of title needs to change languages
                xaxis={
                    'title': f'{xaxis} ({xaxis_2})'  # x-axis needs to change languages
                },
                yaxis={
                    'title': f'{yaxis} ({yaxis_2})'  # y-axis needs to change languages
                },
                hovermode='closest'
            )
        },
        
    config=dict(locale='de')
    )
    
    return graph2, lang_options[lang_selection]

# Run app
if __name__ == '__main__':
    app.run_server(debug=False)
