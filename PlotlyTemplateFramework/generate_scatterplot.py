from random import choices
import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.express as px
from css_colours import css_colours


# Helper function for mapping colour scheme
def prepare_colour_scheme(z_unique_val, z_unique_val_n, colour_choices):
	# Verify if colour_scheme is provided by users	
	if colour_choices is not None:
		if type(colour_choices) is dict:
			colour_scheme = colour_choices
		elif type(colour_choices) is list:
			colour_scheme = {z_val: colour 
					for z_val, colour in zip(z_unique_val, colour_choices)}
	# If users did not provide
	else:
	# If distinct number of labels equal or less than 10
		if z_unique_val_n <= 10:
			colour_choices = px.colors.qualitative.Plotly[:z_unique_val_n]
		# If distinct number of labels equal more than 10 but not many
		elif z_unique_val_n <= len(css_colours):
			colour_choices =  choices(css_colours, k=z_unique_val_n)
		# If distinct number of labels are too much
		else:
			if addition_colorscale is not None:
				colour_choices = plotly.colors.n_colors(
					addition_colorscale['low'], addition_colorscale['high'], 
					z_unique_val_n, colortype='rgb'
					)
			else:
				colour_choices =  plotly.colors.n_colors('rgb(0, 0, 255)', 
					'rgb(255, 0, 0)', z_unique_val_n, colortype='rgb')
		colour_scheme = {z_val: colour 
					for z_val, colour in zip(z_unique_val, colour_choices)}
	return colour_scheme

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

def generate_catecolour_scatter(x, y, z, showlegend=True, colour_choices=None,
			addition_colorscale=None, hoverinfo='none'):
	# Figure out the colour scheme mapping first
	z_unique_val = z.unique().tolist()
	z_unique_val_n = len(z_unique_val)

	colour_scheme = prepare_colour_scheme(z_unique_val, z_unique_val_n, 
		colour_choices)
	
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

def generate_bubble_chart(x, y, z_dict, showlegend=True, colour_choices=None,
			addition_colorscale=None, hoverinfo='none'):
	data = []
	# When colour is needed, convert it to label
	if 'colour' in z_dict:
		# Figure out the colour scheme mapping first
		colour_unique_val = z_dict['colour'].unique().tolist()
		colour_unique_val_n = len(colour_unique_val)
		colour_scheme = prepare_colour_scheme(colour_unique_val,
			colour_unique_val_n, colour_choices)
		for colour_val in colour_unique_val:
			i_temp = [i for i in z_dict['colour'].index 
						if z_dict['colour'][i]==colour_val]
			x_val = x.iloc[i_temp]
			y_val = y.iloc[i_temp]
			marker_config = {'color': [colour_scheme[colour_val]]*len(x_val)}
			if 'size' in z_dict:
				marker_config['size'] = z_dict['size'].iloc[i_temp]
			data.append(go.Scatter(x=x_val, y=y_val, name=colour_val,
			marker=marker_config, mode='markers', showlegend=showlegend, 
			hoverinfo=hoverinfo))
	# When colour is not needed, simply pass all parameters to plotly
	else:
		data.append(go.Scatter(x=x, y=y, marker={'size':z_dict['size']}, 
			mode='markers', showlegend=showlegend, hoverinfo=hoverinfo))
	return data

