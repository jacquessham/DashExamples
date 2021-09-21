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
for group in df['school'].unique():
    df_temp = df[df['school']==group]
    data.append(go.Histogram(x=df_temp['salary'],name=group,
    	                     xbins={'size':50000}))
# Layout
layout = {'title':{'text':'Everybody\'s Salary', 'x':0.5},
          'barmode':'stack'}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='stacked_histogram.html')
