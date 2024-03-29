import pandas as pd
import plotly
import plotly.graph_objs as go
from data import *
from layout import *


""" Prepare data and layout, and return the figure object to render
with Plotly
"""
def generate_plotly_viz(df, metadata, viz_type, viz_name):
    data = generate_plotlydata(df, metadata, viz_type)
    layout = generate_layout(viz_type, metadata, title=viz_name)

    fig = go.Figure(data=data, layout=layout)
    return fig
