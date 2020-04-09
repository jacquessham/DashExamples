import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Read file and manipulate data
data = pd.read_csv('Air_Traffic_Passenger_Statistics.csv')
data['Activity Period'] = data['Activity Period'].astype(str)
data['Year'] = data['Activity Period'].str[:4].astype(int)
data['Month'] = data['Activity Period'].str[5:].astype(int)
selected_column = 'GEO Summary'

# Dash Set up
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Options Set up
terminal_options = [{'label': i, 'value': i} for i in data['Terminal'].unique()]
terminal_options.append({'label': 'All', 'value': '*'})
terminal_options.sort(key=lambda x: x['label']) # Sort dropdown list label
geo_summ_options = [{'label': i, 'value': i} for i in 
				          data['GEO Summary'].unique()]
geo_summ_options.append({'label': 'All', 'value': '*'})
geo_summ_options.sort(key=lambda x: x['label']) # Sort radio list label

app.layout = html.Div([
	html.H1(children='Example 4: Multiple Input'), 
	# Layout Position 0, headline
	html.Div(html.P(['''
		This example demostrates how to pass two inputs to the visualization.
	''',
	html.Br(),
	'''
		This example is the same as example 3 but adding two more filters.
	''',
	html.Br(),
	'''
		There are a lot of violation on data visualization rules, but
		the purpose of this example is to demostrate the functionalities.
		Sorry for the inconvenience. 
	'''
	])),  # Layout Position 1, description
	html.Div([
		html.Div([
			dcc.Dropdown(
				id='terminal-dropdown',
				options=terminal_options,
				value='*'
			)], style={'width':'40%', 'display': 'inline-block'}),
		html.Div([
			dcc.RadioItems(
				id='geo-summary-radio',
				options=geo_summ_options,
				value='*'
			)
		], style={'width':'40%', 'display': 'inline-block'})
		# 'display' : 'inline-block' forces two div to be parallel
	]), # End input Div
	# Layout Position 2, Input options

	dcc.Graph(id='vis'), # Layout Position 3, graph

	dcc.Slider(
		id='year-slider',
    	min=data['Year'].min(),
    	max=data['Year'].max(),
    	value=data['Year'].min()+1,
    	marks={str(year): str(year) for year in data['Year'].unique()},
    	step=None
	) # Layout Position 4, slider

]) # End outter Div


# Obtain 3 inputs from two dropdown lists and slider to produce one graph
@app.callback(
	Output('vis', 'figure'),
	[Input('terminal-dropdown','value'), Input('geo-summary-radio','value'),
	 Input('year-slider','value')])
def update_figure(terminal, geo_summ, selected_year):
	df_filtered = data[data['Year']==selected_year]
	if geo_summ != '*':
		df_filtered = df_filtered[df_filtered['GEO Summary']==geo_summ]
	if terminal != '*':
		df_filtered = df_filtered[df_filtered['Terminal']==terminal]

	traces = []
	for summ in df_filtered[selected_column].unique():
		df_filtered_temp = df_filtered[df_filtered[selected_column]==summ]
		traces.append(dict(
			x=df_filtered_temp['Month'],
			y=df_filtered_temp['Passenger Count'],
			text=df_filtered_temp['Published Airline']+': Flying from/to '+\
			     df_filtered_temp['GEO Region'] + ' (' +
			     df_filtered['Terminal'] + ')',
			mode='markers',
			marker={
	                'size': 15,
	                'line': {'width': 0.5, 'color': 'white'}
	            },
	        name=summ
		))

	return {
		'data': traces,
		'layout': dict(
			xaxis={'title': 'Month'},
			yaxis={'title': 'Passenger Count', 'type': 'log'},
			legend={'x':0, 'y': 0},
			hovermode='closest',
			transition= {'duration': 200}
		)
	}

if __name__ == '__main__':
	app.run_server(debug=True, port=8052)
