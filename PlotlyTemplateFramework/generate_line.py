import plotly
import plotly.graph_objs as go


def get_mode(datapoints):
	if datapoints:
		return 'lines+markers'
	return 'lines'

def generate_simpleline(x, y, datapoints=False, hoverinfo='none'):
	mode = get_mode(datapoints)
	return go.Scatter(x=x, y=y, mode=mode, hoverinfo=hoverinfo)

def generate_multiplelines(x, y, name, line_colours,
		datapoints=False, hoverinfo='none'):
	mode = get_mode(datapoints)
	data =[]

	# x, y themselves should have partitioned already
	for x_i, y_i, name_i, colour in zip(x, y, name, line_colours):
		data.append(go.Scatter(x=x_i, y=y_i, mode=mode, name=name_i,
			hoverinfo=hoverinfo, line={'color': colour}))

	return data