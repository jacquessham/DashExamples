import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html


# Flask and html set up
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Load the data
data_path = "../../ScotchWhisky/Data/whisky.csv"
whisky = pd.read_csv(data_path)
"""
This is same as:
select region, smoky, count(1)
from data
group by 1,2;
"""
whisky = whisky.groupby(['Region','Smoky'])['Smoky'].count().reset_index(name='count')
regions = whisky['Region'].unique()
whisky_data = []
for region in regions:
	temp = {}
	temp['x'] = whisky[whisky['Region']==region]['Smoky'].tolist()
	temp['y'] = whisky[whisky['Region']==region]['count'].tolist()
	temp['type'] = 'bar'
	temp['name'] = region
	whisky_data.append(temp)

app.layout = html.Div(children=[
	html.H1(children='''Example 1: Bar Chart with Single-malt 
		                Scotch Whisky Statistics'''),

	html.Div(children='''In here, we are counting distilleries
		                 per region and their whisky smokiness'''),

	dcc.Graph(
		id='whisky-barchart',
		figure={
			'data':whisky_data,
			'layout':{'title': 'Smoky Single-malt Whiskies per Region',
			          'xaxis': {'title': 'Score of Smokiness'},
			          'yaxis': {'title': 'Count of Distilleries'}
			          } # End Layout
		} # End figure
	) # End Graph
]) # End Div

if __name__=='__main__':
	app.run_server(debug=True, port=8051)


