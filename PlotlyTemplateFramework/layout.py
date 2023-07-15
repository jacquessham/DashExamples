from generate_bar import barmode_add2_layout


def generate_layout(viz_type, metadata, title=None,
                    plot_bgcolor='rgba(0,0,0,0)'):

    #### Basic Layout Metadata ####
    # Handle title
    if type(title) == str:
        title = {'text': title, 'x': 0.5}
    elif type(title) == dict or title is None:
        pass
    else:
        title = {'text': '**Title Type Error!!!', 'x': 0.5}

    # Handle xaxis
    if 'xaxis' in metadata:
        xaxis = metadata['xaxis']
    else:
        xaxis = None

    # Hand yaxis, forcefully add gridcolour to lightgray if not stated
    if 'yaxis' in metadata:
        yaxis = metadata['yaxis']

        # Check if gridcolor is declared in arguement.json
        # but allow pre-declared colour other than lightgry
        if 'gridcolor' not in yaxis:
            yaxis['gridcolor'] = 'lightgray'
    else:
        yaxis = {'gridcolor': 'lightgray'}


    # Only accepting a dictionary or None for legend
    if 'legend' in metadata:
        legend = metadata['legend']
    else:
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
