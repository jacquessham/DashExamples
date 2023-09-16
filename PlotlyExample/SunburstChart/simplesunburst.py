import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Read data
df = pd.read_csv('../Data/hk_population.csv')

values = df['population'].tolist() + [600000,850000,3000000,0]
labels = df['district'].tolist() + ['Island','Kowloon','New Territories']
parents = df['area'].tolist() + ['Hong Kong','Hong Kong','Hong Kong']

fig = go.Figure(go.Sunburst(
    labels = labels,
    values = values,
    parents = parents,
    textinfo = 'label+value'
    ))


plotly.offline.plot(fig, filename='simple_sunburst.html')
