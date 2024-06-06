from dash import dcc, html


def create_tabs(labels):
	tabs = []
	for i in labels:
		tabs.append(
				dcc.Tab(
					label=i, value=i
				)
			)
	return tabs


def layout(app, num_tab):
	labels = [f'label_{i+1}' for i in range(num_tab)]
	app.layout = html.Div([
			dcc.Tabs(
				id='dashboard-tabs',value=labels[0],
				children=create_tabs(labels)
			),
			html.Div(id='content')
		])
	return app