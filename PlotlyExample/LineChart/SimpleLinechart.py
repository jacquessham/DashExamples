import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df = pd.read_csv('../Data/cust_num.csv')

df = df[df['day']=='Monday']

# Data
data = []
data.append(go.Scatter(x=df['hour'], y=df['customers_count'],
					mode='lines'))
# Layout
layout = {'title':{'text':'Number of Customer Trend', 'x':0.5}}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='simple_linechart.html')