import pandas as pd
import plotly
import plotly.graph_objs as go


def generate_simplescatter(x, y, hoverinfo='none'):
	return go.Scatter(x=x, y=y, hoverinfo=hoverinfo,
		mode='markers')

def generate_numcolour_scatter(x, y, z, showscale=True, colorscale=None,
			hoverinfo='none'):
	marker_config = {'color':z, 'showscale':showscale}
	if colorscale is not None:
		marker_config['colorscale'] = colorscale 
	return go.Scatter(x=x, y=y, mode='markers', hoverinfo=hoverinfo,
		marker=marker_config)

