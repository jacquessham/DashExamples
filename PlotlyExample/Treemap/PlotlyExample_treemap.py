import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)


values = ["11", "12", "13", "14", "15", "20", "30"]
labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "A1", "A2", "A3", "A4", "", "B1"]
marker_colours = ["pink", "royalblue", "lightgray", "purple", 
                  "lightgray", "lightblue", "lightgreen"]

fig = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    marker_colors = marker_colours,
    textinfo = 'label+value+percent parent+percent entry+percent root',
    marker_colorscale = 'Blues'))


plotly.offline.plot(fig, filename='plotly_example_tree.html')