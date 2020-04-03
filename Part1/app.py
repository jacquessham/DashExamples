"""
This is the code from the Dash tutorial Part 2 - Layout
"""
import dash
import dash_core_components as dcc
import dash_html_components as html

# CSS Template
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Flask app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[ #id="_dash-app-content"
    html.H1(children='Hello Dash'), # Position 0, children in Div

    html.Div(children='''
        Dash: A web application framework for Python.
    '''), # Postion 1, children in Div (H1 is built on top of here)

    dcc.Graph(
        id='example-graph', # Name this div
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ) # Position 2, children in Div
])

if __name__ == '__main__':
    app.run_server(debug=True)
