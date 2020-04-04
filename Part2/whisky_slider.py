import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

whisky = pd.read_csv('../../ScotchWhisky/Data/whisky.csv')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Let user to select the score of smoky
# Display the score of body and sweetness

app.layout = html.Div([
    dcc.Graph(id='graph-output'),
    dcc.Slider(
    	id='smoky-slider',
    	min=whisky['Smoky'].min(),
    	max=whisky['Smoky'].max(),
    	marks={str(score): str(score) for score in whisky['Smoky'].unique()},
    	step=None
    ) # End Slider
]) # End Div

@app.callback(
	Output('graph-output','figure'),[Input('smoky-slider','value')])
def update_figure(selected_score):
	whisky_filtered = whisky[whisky.Smoky==selected_score]
	traces = []
	for region in whisky_filtered.Region.unique():
		df_temp = whisky_filtered[whisky_filtered.Region==region]
		traces.append(dict(
			x=df_temp['Body'],
			y=df_temp['Sweetness'],
			text=df_temp['Distillery'],
			mode='markers',
			opacity=0.8,
			markers={
			    'size': 15,
			    'line': {'width': 0.5, 'color': 'white'}
			},
			name=region
		))

	return {
		'data': traces,
		'layout': dict(
			xaxis={'title': 'Body Score', 'range':[0,4]},
			yaxis={'title': 'Sweetness Score', 'range':[0,4]},
			legend={'x':0, 'y': 0},
			hovermode='closest',
			transition= {'duration': 1000}
		)
	}

if __name__ == '__main__':
	app.run_server(debug=True, port=8051)
