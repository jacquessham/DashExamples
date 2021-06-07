import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df_revenue = pd.read_csv('../Data/revenue_dept.csv')
df_expense = pd.read_csv('../Data/expense_dept.csv')

# Define fig
fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

# Data
# marker colors may added in go.Pie
fig.add_trace(go.Pie(labels=df_revenue['category'], 
	                 values=df_revenue['revenue'],name='Revenue'),1,1)
fig.add_trace(go.Pie(labels=df_expense['category'], 
	                 values=df_expense['expense'],name='Expense'),1,2)

# Layout
fig.update_layout(title_text='Department Store Revenue',title_x=0.5)

plotly.offline.plot(fig, filename='multiple_pies.html')