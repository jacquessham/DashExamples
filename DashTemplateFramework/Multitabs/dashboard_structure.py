from dash import dcc, html


def create_tabs(num_tab):
	tabs = []
	for i in range(num_tab):
		tabs.append(
				dcc.Tab(
					label=f'label{i+1}', value=f'label{i+1}'
				)
			)
	return tabs


def layout(app, num_tab):
	app.layout = html.Div([
			dcc.Tabs(
				id='dashboard-tabs',value='label_1',
				children=create_tabs(num_tab)
			),
			html.Div(id='content')
		])
	return app