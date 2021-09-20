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
data.append(go.Histogram(x=df['salary'], histnorm='probability'))
# Layout
layout = {'title':{'text':'Everybody\'s Salary', 'x':0.5}}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='normalized_histogram.html')
