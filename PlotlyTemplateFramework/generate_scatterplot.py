import plotly
import plotly.graph_objs as go


def generate_simplescatter(x, y, hoverinfo='none'):
	return go.Scatter(x=x, y=y, hoverinfo=hoverinfo,
		mode='markers')
