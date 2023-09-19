import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Read data
df = pd.read_csv('../Data/salary.csv')

values = df['salary'].tolist() + [0,0]
labels = df['name'].tolist() + df['school'].unique().tolist()
parents = df['school'].tolist() + ['','']

fig = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    textinfo = 'label+value+percent parent+percent entry+percent root',
    marker_colorscale = 'Blues'))


plotly.offline.plot(fig, filename='salary_example_tree.html')
