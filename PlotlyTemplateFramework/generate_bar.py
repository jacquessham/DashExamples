import plotly
import plotly.graph_objs as go


# Function to prepare data list in data.py for simple bar chart
def generate_simplebar(x, y, text=None, bar_colour='light blue',
                       textposition='auto', textfont={'color': 'white'}):

    return go.Bar(x=x, y=y, text=text, textposition=textposition,
                  marker_color=bar_colour, textfont=textfont)

# Function to prepare data list in data.py for group or stack bar chart
def generate_complexbar(df, x, y, cate_col, text=None, bar_colour=None,
                        textposition='auto', textfont={'color': 'white'}):
    data = []
    if bar_colour is None:
        for cate in df[cate_col].unique():
            df_temp = df[df[cate_col] == cate]
            data.append(
                go.Bar(
                    name=cate,
                    x=df_temp[x], y=df_temp[y],
                    text=text, textposition=textposition,
                    textfont=textfont
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
                    textfont=textfont
                )
            )
    return data

# Function to add metadata in layout.py for group or stack bar chart
def barmode_add2_layout(layout, barmode):
    layout['barmode'] = barmode
    return layout
