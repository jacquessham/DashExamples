import plotly
import plotly.graph_objs as go


""" Function to prepare data list in data.py for simple bar chart """
def generate_simplebar(x, y, text=None, bar_colour=None, width=None,
                       textposition='auto', textfont={'color': 'white'},
                       hoverinfo='none'):
    return go.Bar(x=x, y=y, width=width,
                  text=text, textposition=textposition,
                  marker_color=bar_colour, textfont=textfont,
                  hoverinfo=hoverinfo)


""" Function to prepare data list in data.py for group or stack bar chart """
def generate_complexbar(df, x, y, cate_col, text=None, bar_colour=None,
                        width=None, textposition='auto', 
                        textfont={'color': 'white'}, hoverinfo='none'):
    data = []
    if bar_colour is None:
        for cate in df[cate_col].unique():
            df_temp = df[df[cate_col] == cate]
            data.append(
                go.Bar(
                    name=cate,
                    x=df_temp[x], y=df_temp[y],
                    width=width,
                    text=text, textposition=textposition,
                    textfont=textfont, hoverinfo=hoverinfo
                )
            )

    else:
        for cate, colour in zip(df[cate_col].unique(), bar_colour):
            df_temp = df[df[cate_col] == cate]
            data.append(
                go.Bar(
                    name=cate, x=df_temp[x], y=df_temp[y],
                    marker_color=colour,
                    text=text, textposition=textposition,
                    textfont=textfont, hoverinfo=hoverinfo
                )
            )
    return data


def barmode_add2_layout(layout, barmode):
    """ Function to add metadata in layout.py for group or stack bar chart
    """
    # "simple" is not a Plotly option
    if barmode == 'simple':
        return layout
    layout['barmode'] = barmode
    return layout
