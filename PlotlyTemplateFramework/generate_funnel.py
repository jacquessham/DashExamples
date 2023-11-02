import plotly
import plotly.graph_objs as go


""" Function to prepare data list in data.py for simple funnel chart """
def generate_simplefunnel(x, y, marker=None, connector=None,
                          textposition='auto', textinfo='value',
                          hoverinfo='none'):
    return go.Funnel(x=x, y=y, marker=marker, connector=connector, 
                     textposition=textposition, textinfo=textinfo, 
                     hoverinfo=hoverinfo)

""" Function to prepare data list in data.py for stack funnel chart """
def generate_stackfunnel(df, x, y, cate_col, marker=None, 
                         connector=None, textposition='auto', 
                         textinfo='value', hoverinfo='none'):
    data = []
    for cate in df[cate_col].unique():
        df_temp = df[df[cate_col] == cate]
        data.append(
            go.Funnel(
                name=cate,
                x=df_temp[x], y=df_temp[y], marker=marker,
                connector=connector, textposition=textposition,
                textinfo=textinfo, hoverinfo=hoverinfo
            )
        )
    return data

""" Function to prepare data list in data.py for simple funnel area chart """
def generate_simplefunnelarea(values, text=None, labels=None, marker=None, 
                              textposition='auto', textinfo='value', 
                              hoverinfo='none'):
    return go.Funnelarea(text=text, labels=labels, values=values, 
                         marker=marker, textposition=textposition, 
                         textinfo=textinfo, hoverinfo=hoverinfo)
