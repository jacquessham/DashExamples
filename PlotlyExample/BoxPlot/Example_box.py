import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df = pd.read_csv('../Data/salary.csv')

# Prepare data
data = []
for school in df['school'].unique():
	df_temp = df[df['school']==school]
	data.append(go.Box(y=df_temp['salary'], name=school, boxmean=True))

# Layout
layout = dict(title={'text':'Alumni Salary across Schools', 'x':0.5},
              barmode='group', xaxis=dict(tickmode='linear'))

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='box.html')