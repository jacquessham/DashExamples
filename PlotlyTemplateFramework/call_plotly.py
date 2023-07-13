import json
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


with open('arguements.json') as f:
    args = json.load(f)
df = pd.read_csv(args['df_directory'])
fig = generate_plotly_viz(df, args['x'], args['y'],
                          args['viz_type'], args['viz_name'])
plotly.offline.plot(fig, filename='call_plotly.html')
