import plotly
import plotly.graph_objs as go


def generate_simplebar(x, y, text=None, bar_colour='blue',
                       textposition='auto', textfont=None):
    if textfont is None:
        textfont = {'color': 'white'}

    return go.Bar(x=x, y=y, text=text, textposition=textposition,
            marker_color=bar_colour, textfont=textfont)
