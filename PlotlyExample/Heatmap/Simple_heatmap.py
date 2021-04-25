import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df = pd.read_csv('../Data/cust_num.csv')

# Data
data = []
data.append(go.Heatmap(z=df['customers_count'],
	                   x=df['day'], y=df['hour'],
	                   colorscale='ylorrd'))

# Layout
layout = {'title':{'text':'Department Store Traffic',
	               'x':0.5},
	      'xaxis': {'tickmode':'linear'},
	      'yaxis': {'tickmode':'linear'}}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='simple_heatmap.html')