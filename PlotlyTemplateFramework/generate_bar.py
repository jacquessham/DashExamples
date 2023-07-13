import plotly
import plotly.graph_objs as go


def generate_simplebar(x, y, text=None, bar_colour='blue',
                       textposition='auto', text_font=None)
   if text_font is None:
        text_font = {'color': 'white'}

    return go.Bar(x=x, y=y, text=text, textposition=textposition,
            marker_color=bar_colour, text_font=text_font)
