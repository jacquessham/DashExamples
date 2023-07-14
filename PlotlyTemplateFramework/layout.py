from generate_bar import barmode_add2_layout


def generate_layout(viz_type, metadata, title=None, xaxis=None, yaxis=None,
                    legend=None, plot_bgcolor='rgba(0,0,0,0)'):

    #### Basic Layout Metadata ####
    # Handle title
    if type(title) == str:
        title = {'text': title, 'x': 0.5}
    elif type(title) == dict or title is None:
        pass
    else:
        title = {'text': '**Title Type Error!!!', 'x': 0.5}

    # Handle xaxis
    if type(xaxis) == str:
        xaxis = {'title': xaxis}
    elif type(xaxis) == dict or xaxis is None:
        pass
    else:
        xaxis = {'title': '**X-axis Type Error!!!'}

    # Hand yaxis
    if type(yaxis) == str:
        yaxis = {'title': yaxis}
    elif type(yaxis) == dict:
        pass
    elif yaxis is None:
        yaxis = {'gridcolor': 'lightgray'}
    else:
        yaxis = {'title': '**Y-axis Type Error!!!', 'gridcolor': 'lightgray'}

    # Only accepting a dictionary or None for legend
    if legend is not None and type(legend) != dict:
        legend = None

    # Put all metadata together
    layout = {
        'title': title,
        'xaxis': xaxis,
        'yaxis': yaxis,
        'legend': legend,
        'plot_bgcolor': plot_bgcolor
    }

    #### Bar Chart Specific Layout ####
    if viz_type.lower() == 'bar':
        barmode = metadata['viz_subtype']
        layout = barmode_add2_layout(layout, barmode)

    return layout
