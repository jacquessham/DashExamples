import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Read data
df = pd.read_csv('../Data/ecom_funnel.csv')
df = df[df['shop']=='Shop A']

fig = go.Figure(go.Funnelarea(
    text = df['stage'], # Text displayed on funnel bars
    # labels = df['stage'], # Text displayed only in legend
    values = df['count'])
)

plotly.offline.plot(fig, filename='simple_funnelarea.html')