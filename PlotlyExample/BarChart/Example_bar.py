import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df = pd.read_csv('expense.csv')
df = df.groupby(['name','expense_category'])['amount'].sum().reset_index()
# Round number for amount column
df['amount'] = df['amount'].round(2)

# Prepare data
data =[]
for cate in df['expense_category'].unique():
	df_temp = df[df['expense_category']==cate]
	data.append(go.Bar(name=cate, 
	               x=df_temp['name'], y=df_temp['amount'],
	               text=df_temp['amount'], textposition='auto',
	               textfont=dict(color='white')))

fig_title = 'Everybody\'s Expense'
layout = dict(title={'text':fig_title, 'x':0.5},
              barmode='group', xaxis=dict(tickmode='linear'))

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='bar.html')