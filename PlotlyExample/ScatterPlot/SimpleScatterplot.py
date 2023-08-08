import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df = pd.read_csv('../Data/tips.csv')

# Data
data = []
data.append(go.Scatter(x=df['grand_total'], y=df['tips'],
					mode='markers'))
# Layout
layout = {'title':{'text':'Everybody\'s Tipping Distribution', 'x':0.5}}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='simple_scatterplot.html')