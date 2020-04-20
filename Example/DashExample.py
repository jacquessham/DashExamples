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
vis_type_options = [{'label': 'Line Chart', 'value': 'line'},
                {'label': 'Bar Chart', 'value': 'bar'}]

# Declare headline and description
headline = 'Gaming Console Marketshare in 2018'
description = '''
                  The marketshare of gaming console is different in 
                  every corner in the world. For exmample, the marketshare
                  of Xbox in Japan is significantly lower than the marketshare
                  in the US. In this dashboard, you may select the region in 
                  the dropdown list below and the visualization. A brief 
                  analysis of the gaming market share in the 
                  selected region will be displayed under the graph. 
              '''

# Dashboard layout
app.layout = html.Div([
	html.H1(children=headline, style={'text-align':'center'}), 
	# Position 0, headline
	html.Div(children=description, style={'width':'60%'}), 
	# Position 1, descritpion
	html.Div([
		html.Div([
			html.P('Select Region:'),
			dcc.Dropdown(
				id='region-dropdown',
				options=region_dropdown,
				value='World Wide',
				style={'width': '90%'}
				)
			], style={'width':'60%', 'display': 'inline-block',
			          'vertical-align': 'middle'}),
		html.Div([
			html.P('Select Visualization:'),
			dcc.RadioItems(
				id='type-radio',
				options=vis_type_options,
				value='line'
				)
			], style={'width':'40%', 'display': 'inline-block',
			          'vertical-align': 'middle'})
	]), # Position 2, Options
	html.Div(dcc.Graph(id='vis')), # Position 3, Graph
	html.Div(dcc.Markdown(id='markdown'), style={'width':'60%'}) 
	# Position 4, Markdown
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
	df = df.drop(['Region'], axis=1)
	data = []
	for console in df.columns:
		if console != 'Date':
			temp = {}
			temp['x'] = df['Date']
			temp['y'] = df[console]
			temp['type'] = 'bar'
			temp['name'] = console
			data.append(temp)

	layout = dict(title=title, 
		          xaxis={'title':'Consoles'},
		          yaxis={'title':'Market Share (%)', 'range': [0,100]},
		          barmode='group',
		          transition={'duration': 500})

	return {'data': data, 'layout': layout}

@app.callback([Output('vis','figure'), Output('markdown','children')],
	          [Input('region-dropdown','value'),
	           Input('type-radio','value')])
def display_graph(region, vis_type):
	df_temp = df[df['Region']==region]
	fig = None
	vis_title = 'Gaming Market Share in 2018'
	if vis_type == 'line':
		fig = getLineChart(df_temp, vis_title)
	elif vis_type == 'bar':
		fig = getBarChart(df_temp, vis_title)
	filepath_markdown = 'Data/Markdown_'
	filepath_markdown += region2brief[region]
	filepath_markdown += '.txt'
	f = open(filepath_markdown, 'r')
	text = 'A brief analysis: '
	text += f.read()
	f.close()
	return fig, text

if __name__ == '__main__':
    app.run_server(debug=True, port=1200)