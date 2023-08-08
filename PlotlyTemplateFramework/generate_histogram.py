import pandas as pd
import plotly
import plotly.graph_objs as go


def generate_simplehistogram(x, histnorm=None, cumulative_enabled=False):
	return go.Histogram(x=x, histnorm=histnorm, 
		cumulative_enabled=cumulative_enabled)

def generate_categoricalhistogram(df, x_col, cate_col, 
			cumulative_enabled=False):
	data = []
	for group in df[cate_col].unique():
		df_temp = df[df[cate_col]==group]
		data.append(go.Histogram(x=df_temp[x_col], name=group, 
			cumulative_enabled=cumulative_enabled))
	return data

def generate_aggregatedhistogram(df, x_col, cate_col, histfunc='count',
			cumulative_enabled=False):
	data = []
	for group in df[cate_col].unique():
		df_temp = df[df[cate_col]==group]
		data.append(go.Histogram(x=df_temp[x_col], y=df_temp[x_col],
			histfunc=histfunc, name=group, 
			cumulative_enabled=cumulative_enabled))
	return data