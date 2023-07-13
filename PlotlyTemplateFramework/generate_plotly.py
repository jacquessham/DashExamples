import pandas as pd
import plotly
import plotly.graph_objs as go
from data import *
from layout import *


def generate_plotly_viz(df, x, y, viz_type, viz_name):
    data = generate_plotlydata(df[x], df[y], viz_type)
    layout = generate_layout(title=viz_name)

    fig = go.Figure(data=data, layout=layout)
    return fig
