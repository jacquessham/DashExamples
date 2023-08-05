from random import choices
import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.express as px
from css_colours import css_colours


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

def generate_catecolour_scatter(x, y, z, showlegend=True, 
			addition_colorscale=None, hoverinfo='none'):
	# Figure out the colour scheme mapping first
	z_unique_val = z.unique().tolist()
	z_unique_val_n = len(z_unique_val)

	# If distinct number of labels equal or less than 10
	if z_unique_val_n < 100:
		colour_scheme = {z_val: colour for z_val, colour in zip(z_unique_val, px.colors.qualitative.Plotly[:z_unique_val_n])}
	# If distinct number of labels equal more than 10 but not many
	elif z_unique_val_n <= len(css_colours):
		colour_scheme = {z_val: colour for z_val, colour in zip(z_unique_val, choices(css_colours, k=z_unique_val_n))}
	# If distinct number of labels are too much
	else:
		if addition_colorscale is not None:
			colour_scheme = {z_val: colour for z_val, colour in zip(z_unique_val, plotly.colors.n_colors(addition_colorscale['low'], addition_colorscale['high'], z_unique_val_n, colortype='rgb'))}
		else:
			colour_scheme = {z_val: colour for z_val, colour in zip(z_unique_val, plotly.colors.n_colors('rgb(0, 0, 255)', 'rgb(255, 0, 0)', z_unique_val_n, colortype='rgb'))}

	# Prepare data list and partition by label
	data = []
	for z_val in z_unique_val:
		i_temp = [i for i in z.index if z[i]==z_val]
		x_val = x.iloc[i_temp]
		y_val = y.iloc[i_temp]
		data.append(go.Scatter(x=x_val, y=y_val, 
			marker_color=colour_scheme[z_val], name=z_val, mode='markers',
			showlegend=showlegend, hoverinfo=hoverinfo))

	return data
