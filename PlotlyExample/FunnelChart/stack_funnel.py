import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Read data
df = pd.read_csv('../Data/ecom_funnel.csv')

data = []
for shop in df['shop'].unique():
	df_temp = df[df['shop']==shop]
	data.append(go.Funnel(
		name = shop,
	    y = df_temp['stage'],
	    x = df_temp['count'])
	)
# Layout
layout = dict(title={'text':'Ecommerce Funnel', 'x':0.5},
              barmode='group', xaxis=dict(tickmode='linear'))

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='stack_funnel.html')