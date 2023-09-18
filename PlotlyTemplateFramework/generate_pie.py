import pandas as pd
import plotly
import plotly.graph_objs as go


def generate_simplepie(x, y, hole=0, textinfo='percent',hoverinfo='none'):
	return go.Pie(labels=x, values=y, hole=hole, textinfo=textinfo, hoverinfo=hoverinfo)
