import plotly
import plotly.graph_objs as go


def generate_heatmap(x, y, z, colourscale, hoverinfo='none'):
	if colourscale is None:
		colourscale = 'ylorrd'
	return go.Heatmap(z=z, x=z, y=y,colorscale=colourscale, 
		hoverinfo=hoverinfo)
