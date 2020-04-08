import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Read file and split period into year and month
data = pd.read_csv('Air_Traffic_Passenger_Statistics.csv')
data['Activity Period'] = data['Activity Period'].astype(str)
data['Year'] = data['Activity Period'].str[:4].astype(int)
data['Month'] = data['Activity Period'].str[5:].astype(int)

# Select columns
selected_column = 'GEO Summary'
data = data[['Published Airline','Year','Month','Passenger Count',
             'GEO Region',selected_column]]

# Declare Dash properties
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Layout is headline, description, graph, and slider
app.layout = html.Div([
	html.H1(children='Example 3: Slider'),
	html.Div(html.P(['''
			This example demostrates how to use slider on the dashboard.''',
			html.Br(),
			'''
			The chart display the observation of passenger traffic of 
			each airline flying from/to a region in each month in a year.
			The slider control the year.''',
			html.Br(),
			'''
			This is not a good chart to visualize the data but the purpose
			is to build a slider on this dashboard.'''
		])),
    dcc.Graph(id='graph-output'),
    dcc.Slider(
    	id='year-slider',
    	min=data['Year'].min(),
    	max=data['Year'].max(),
    	value=data['Year'].min()+1,
    	marks={str(year): str(year) for year in data['Year'].unique()},
    	step=None
    ) # End Slider
]) # End Div

# @app.callback is defined for the below function
@app.callback(
	Output('graph-output','figure'),[Input('year-slider','value')])
def update_figure(selected_year):
	# Filter the year selected in slider
	df_filtered = data[data['Year']==selected_year]
	# Each element in traces is for one value in selected_column
	# Each value will be displayed as different colour
	traces = []
	for summ in df_filtered[selected_column].unique():
		# Filter data points in filtered year and selected_column
		df_filtered_temp = df_filtered[df_filtered[selected_column]==summ]
		traces.append(dict(
			x=df_filtered_temp['Month'],
			y=df_filtered_temp['Passenger Count'],
			text=df_filtered_temp['Published Airline']+': Flying from/to '+\
			     df_filtered_temp['GEO Region'],
			mode='markers',
			marker={
	                'size': 15,
	                'line': {'width': 0.5, 'color': 'white'}
	            },
	        name=summ
		))
	
	# return all info for figure
	return {
		'data': traces,
		'layout': dict(
			xaxis={'title': 'Month'},
			yaxis={'title': 'Passenger Count', 'type': 'log'},
			legend={'x':0, 'y': 0}, # Legend in bottom left
			hovermode='closest',
			transition= {'duration': 200}
		)
	}

if __name__ == '__main__':
	app.run_server(debug=True, port=8051)
