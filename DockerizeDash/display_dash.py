import dash
import dash_core_components as dcc
import dash_html_components as html


# Initiate App
app = dash.Dash(__name__)

# The layout of the dashboard
app.layout = html.Div(children=[
	html.H1(children='''Example 1: Bar Chart with Single-malt 
		                Scotch Whisky Statistics'''),

	html.Div(children='''In here, we are counting distilleries
		                 per region and their whisky smokiness'''),

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
]) # End Div

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=9000)
