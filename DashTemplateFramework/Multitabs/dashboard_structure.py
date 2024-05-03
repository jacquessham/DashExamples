from dash import dcc, html


def create_tabs(num_tab):
	tabs = []
	for i in range(num_tab):
		tabs.append(
				dcc.Tab(
					label=f'label{i+1}', value=f'label{i+1}',
					children=[
						html.Div(dcc.Graph(figure=None))
					]
				)
			)
	return tabs


def layout(app, num_tab):
	app.layout = html.Div([
			dcc.Tabs(
				id='dashboard-tabs',value='net_worth',
				children=create_tabs(num_tab)
			)
		])
	return app