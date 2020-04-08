import json
from random import randint
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Declare Dash properties
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

# Define how does the graph looks like
fig = {
	'data':[
		{
			'x': [randint(0,1000)/100.0 for i in range(4)],
			'y': [randint(0,500)/100.0 for i in range(4)],
			'text': ['alpha','bravo','charlie','delta'],
			'name': '1st Category',
			'mode': 'markers',
			'marker': {'size': 12}
		},
		{
			'x': [randint(200,600)/100.0 for i in range(4)],
			'y': [randint(400,900)/100.0 for i in range(4)],
			'text': ['papa','quebec','romeo','sierra'],
			'name': '2nd Category',
			'mode': 'markers',
			'marker': {'size': 16}
		}
	], # End data
	'layout': {'clickmode': 'event+select'}
}


# Define the layout of the graph
app.layout = html.Div([
	html.H1(children='Example 7: Interactive Visualization'), 
	# Position 0, headline
	html.P('''
			This example demostrates the interactive functionality in Dash.
		'''), # Position 1, description
	html.Hr(),
	dcc.Graph(
		id='vis',
		figure=fig
	), # End Graph
	# Position 2, graph
	html.Pre(id='hover-data',style=styles['pre']), # Position 3, hover textbox
	html.Pre(id='click-data',style=styles['pre']),
	# Position 4, textbox displays clicked data point
	html.Pre(id='click-datas',style=styles['pre']),
	# Position 4, textbox displays clicked 1+ data point
])


@app.callback(Output('hover-data','children'),[Input('vis','hoverData')])
def display_hoverdata(hoverdata):
	# If nothing is hover, it would throw an error
	if hoverdata is None:
		return None
	temp = hoverdata['points'][0]
	x = temp['x']
	y = temp['y']
	text = temp['text']
	message = '''
	            The data point is ({},{}) and the text is {}
	          '''.format(x, y, text)
	return message

# This interaction only works on one data point
@app.callback(Output('click-data','children'),[Input('vis','clickData')])
def display_clickeddata(clickeddata):
	# If nothing is clicked, it also would throw an error
	if clickeddata is None:
		return None
	temp = clickeddata['points'][0]
	x = temp['x']
	y = temp['y']
	text = temp['text']
	message = '''
	            You have clicked ({},{}) which the text is {}
	          '''.format(x, y, text)
	return message

# This interaction works for more than one data point
@app.callback(Output('click-datas','children'),[Input('vis','selectedData')])
def display_clickeddata(clickeddata):
	# If nothing is clicked, it prevents displaying null
	if clickeddata is None:
		return ''
	x = []
	y = []
	texts = []
	points = clickeddata['points']
	for point in points:
		x.append(point['x'])
		y.append(point['y'])
		texts.append(point['text'])
	pairs = ['('+str(x)+','+str(y)+')' for x,y in zip(x,y)]
	pairs = ','.join(pairs)
	texts = ', '.join(texts)
	message = '''
	            You have clicked {} that the text are {}
	          '''.format(pairs, texts)
	return message

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)