import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Define the regions and the full name
regions = {'CA': 'Canada', 'GB': 'Great Britain', 'HK': 'Hong Kong',
           'JP': 'Japan', 'KR': 'South Korea', 'US': 'United States',
           'WorldWide': 'World Wide'}
region2brief = dict([(regions[k], k) for k in regions])

# Read multiple data set
filepath = 'Data/Console_share_'
df = []
for region in regions:
	filepath_curr = filepath + region + '.csv'
	df_temp = pd.read_csv(filepath_curr)
	rows = df_temp.shape[0]
	df_temp['Region'] = [regions[region] for _ in range(rows)]
	df.append(df_temp)

df = pd.concat(df)
df = df.drop('Other', axis=1)
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m')


# Dash Set up
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Dropdown list and radio button options set up
region_dropdown = [{'label': regions[region], 'value': regions[region]} \
                   for region in regions]
time_options = [{'label': 'Monthly', 'value': 'month'},
                {'label': 'Yearly', 'value': 'year'}]

# Declare headline and description
headline = 'Headline here'
description = 'Description here'

# Dashboard layout
app.layout = html.Div([
	html.H1(children=headline), # Position 0, headline
	html.Div(children=description), # Position 1, descritpion
	html.Div([
		html.Div([
			dcc.Dropdown(
				id='region-dropdown',
				options=region_dropdown,
				value='World Wide'
				)
			], style={'width':'60%', 'display': 'inline-block'}),
		html.Div([
			dcc.RadioItems(
				id='time-radio',
				options=time_options,
				value='month'
				)
			], style={'width':'40%', 'display': 'inline-block'})
	]), # Position 2, Options
	html.Div(dcc.Graph(id='vis')), # Position 3, Graph
	html.Div(dcc.Markdown(id='markdown')) # Position 4, Markdown
]) # End Dashboard Div

def getLineChart(df, title):
	traces = []
	for console in df.columns:
		if console != 'Date' and console != 'Region':
			traces.append(dict(
				x=df['Date'],
				y=df[console],
				mode='lines+markers',
				marker={
						'size': 15,
						'line': {'width': 0.5, 'color': 'white'}
				},
				name=console
				))
	layout = dict(title=title, 
		          xaxis={'title':'Date'},
		          yaxis={'title':'Market Share (%)', 'range': [0,100]},
		          transition={'duration': 500})
	return {'data': traces, 'layout': layout}

def getBarChart(df, title):
	df = df.drop(['Date','Region'], axis=1)
	df = df.mean().reset_index()
	data = [dict(x=df.iloc[:,0], y=df.iloc[:,1],type='bar')]
	layout = dict(title=title, 
		          xaxis={'title':'Consoles'},
		          yaxis={'title':'Market Share (%)', 'range': [0,100]},
		          transition={'duration': 500})

	return {'data': data, 'layout': layout}

@app.callback([Output('vis','figure'), Output('markdown','children')],
	          [Input('region-dropdown','value'),
	           Input('time-radio','value')])
def display_graph(region, time):
	df_temp = df[df['Region']==region]
	fig = None
	if time == 'month':
		fig = getLineChart(df_temp, 'Title Here')
	elif time == 'year':
		fig = getBarChart(df_temp, 'Title Here')
	filepath_markdown = 'Data/Markdown_'
	filepath_markdown += region2brief[region]
	filepath_markdown += '.txt'
	f = open(filepath_markdown, 'r')
	text = f.read()
	f.close()
	return fig, text

if __name__ == '__main__':
    app.run_server(debug=True, port=1200)