import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df = pd.read_csv('../Data/cust_num.csv')

colour_scheme = ['red','blue','black','orange','yellow','brown','green']

# Data
data = []
for day, colour in zip(df['day'].unique(), colour_scheme):
	df_temp = df[df['day']==day]
	data.append(go.Scatter(x=df_temp['hour'], y=df_temp['customers_count'],
						line={'color': colour},
						name=day,
						mode='lines'))
# Layout
layout = {'title':{'text':'Number of Customer Trend by Days', 'x':0.5}}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='mutlilines_linechart.html')