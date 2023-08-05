from check_metadata import *
from generate_bar import generate_simplebar, generate_complexbar
from generate_boxplot import generate_boxplot
from generate_candlestick import generate_candlestick
from generate_scatterplot import generate_simplescatter, generate_numcolour_scatter, generate_catecolour_scatter
from generate_line import generate_simpleline, generate_multiplelines


""" Function to distinguish what viz_type and organize the required
metadata, and call the proper function from the generate_*.py scripts
and return the data list to generate_plotly.py
"""
def generate_plotlydata(df, metadata, viz_type):
    # Check if Optional args exist:
    text = check_text(metadata)
    textposition = check_textposition(metadata)
    textfont = check_textfont(metadata)
    hoverinfo = check_hoverinfo(metadata)
    name = check_name(metadata)

    # Call the function for respective viz_type
    # Bar Chart
    if viz_type.lower() == 'bar':
        # Check if Optional args exist:
        bar_colour = check_barcolour(metadata)
        width = check_width(metadata)

        # Currently only support 1 column dataset only
        if metadata['viz_subtype'].lower() == 'simple':
            data = generate_simplebar(
                df[metadata['x']], df[metadata['y']], text, bar_colour, width,
                textposition, textfont, hoverinfo)

        # Group or Stack Bar Chart
        # Mode whether Group or Stack Bar is set in layout.py
        elif metadata['viz_subtype'].lower() == 'group' \
                or metadata['viz_subtype'].lower() == 'stack':
            cate_col = check_cate_col(metadata)
            data = generate_complexbar(df, metadata['x'], metadata['y'],
                                       cate_col, text, bar_colour, width,
                                       textposition, textfont, hoverinfo)

    # Boxplot
    elif viz_type.lower() == 'boxplot' or viz_type.lower() == 'box_plot':
        # Check if Optional args exist:
        bar_colour = check_barcolour(metadata)
        boxmean = check_boxmean(metadata)

        # Allow user to use x or category_col or cate_col
        if 'x' in metadata:
            category_col = metadata['x']
        elif 'cate_col' in metadata:
            category_col = metadata['cate_col']
        else:
            category_col = metadata['category_col']
        data = generate_boxplot(df, category_col, metadata['y'],
                                bar_colour, boxmean, textposition)

    # Candlestick
    elif viz_type.lower() == 'candlestick':
        data = generate_candlestick(
                df[metadata['x']], df[metadata['open']], df[metadata['high']],
                df[metadata['low']], df[metadata['close']])

    # Scatter Plot/Bubble Chart
    elif viz_type.lower() in ['scatter', 'scatterplot', 'scatter_plot',
        'bubblechart', 'bubble_chart']:
        colourscale = check_colourscale(metadata)
        showscale = check_showscale(metadata)
        if metadata['viz_subtype'].lower() == 'simple':
            data = generate_simplescatter(
                df[metadata['x']], df[metadata['y']], hoverinfo)
        elif metadata['viz_subtype'].lower() in ['numeric_colour',
                'numeric_color','num_colour','num_color']:
            data = generate_numcolour_scatter(df[metadata['x']], 
                df[metadata['y']], df[metadata['z']], showscale,
                colourscale, hoverinfo)
        elif metadata['viz_subtype'].lower() in ['category_colour',
                'categorical_colour','cate_colour', 'category_color',
                'categorical_color','cate_color']:
            addition_colorscale = check_add_colourscale(metadata)
            showlegend = check_showlegend(metadata)
            data = generate_catecolour_scatter(df[metadata['x']], 
                df[metadata['y']], df[metadata['z']], showlegend, 
                addition_colorscale, hoverinfo)

    # Line Chart
    elif viz_type.lower() == 'line':
        datapoints = check_datapoints(metadata)
        if metadata['viz_subtype'].lower() == 'simple':
            data = generate_simpleline(df[metadata['x']], df[metadata['y']], 
                datapoints, hoverinfo)
        elif metadata['viz_subtype'].lower() in ['mutlilines','mutliple_lines',
            'mutli_lines']:
            curr_x = []
            curr_y = []
            curr_name = []
            curr_colour = []
            cate_col = check_cate_col(metadata)
            colour_scheme = check_line_colour(metadata)

            for unique_val in df[cate_col].unique():
                df_temp = df[df[cate_col]==unique_val]
                curr_x.append(df_temp[metadata['x']])
                curr_y.append(df_temp[metadata['y']])
                curr_name.append(unique_val)
                if colour_scheme is not None:
                    curr_colour.append(colour_scheme[unique_val])
                else:
                    curr_colour.append(None)

            data = generate_multiplelines(curr_x, curr_y, curr_name, 
                curr_colour, datapoints, hoverinfo)
    
    else:
        data = None




    return data
