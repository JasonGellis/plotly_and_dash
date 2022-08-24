# markdown with dash

# import libraries
import dash
from dash import dcc
from dash import html

# first set the markdown text as a variable surrounded by ''' '''
markdown_text = '''
### Dash and Markdown
Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/) specification of Markdown.
Review the [60 Second Markdown Tutorial](http://commonmark.org/help)

Review how to set things in ***bold text*** and *italics*,
`inline code snippets`, lists, quotes, and more.
'''

# create dashboard app
app = dash.Dash()

# us dash core components
app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
    ])

if __name__ == '__main__':
    app.run_server()
    