import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Read data
df = pd.read_csv('../Data/salary.csv')

values = df['salary'].tolist() + [600000,350000]
labels = df['name'].tolist() + df['school'].unique().tolist()
parents = df['school'].tolist() + ['University','University']

fig = go.Figure(go.Sunburst(
    labels = labels,
    values = values,
    parents = parents,
    textinfo = 'label+value',
    marker_colorscale = 'agsunset'
    ))


plotly.offline.plot(fig, filename='simple_sunburst_agsunset.html')
