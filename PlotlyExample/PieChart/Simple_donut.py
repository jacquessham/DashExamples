import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df = pd.read_csv('../Data/revenue.csv')

# Data
data = []
data.append(go.Pie(labels=df['category'], values=df['revenue'], hole=0.4))

# Layout
layout = {'title':{'text':'Department Store Revenue', 'x':0.5}}


fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='simple_donut.html')