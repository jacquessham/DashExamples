import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df = pd.read_csv('../Data/salary.csv')

# Data
data = []
data.append(go.Bar(y=df['name'], x=df['salary'],
	               text=df['salary'], textposition='auto',
	               orientation='h',
	               textfont=dict(color='white')))
# Layout
layout = {'title':{'text':'Everybody\'s Salary', 'x':0.5}}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='hbar.html')
