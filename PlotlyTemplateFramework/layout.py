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
        # barmode = 'simple' is not a option in Plotly, string fixing
        layout = barmode_add2_layout(layout, barmode)

    #### Candlestick Specific Layout ####
    if viz_type.lower() == 'candlestick':
        # If rangeslieder is stated in arguements.json
        if 'rangeslider' in metadata:
            if layout['xaxis'] is not None:
                layout['xaxis']['rangeslider'] = metadata['rangeslider']
            else:
                layout['xaxis'] = {'rangeslider': metadata['rangeslider']}
        # If rangeslieder is not stated in arguements.json
        else:
            if layout['xaxis'] is not None:
                layout['xaxis']['rangeslider'] = {'visible':False}
            else:
                layout['xaxis'] = {'rangeslider':{'visible':False}}

    #### Bubble Chart Specific Layout
    if viz_type.lower() in ['bubblechart', 'bubble_chart'] or (
        viz_type.lower() in ['scatter', 'scatterplot', 'scatter_plot']
        and metadata['viz_subtype'].lower() in ['bubblechart', 
        'bubble_chart']):
        if 'constant_itemsizing' in metadata:
            if metadata['constant_itemsizing'] in ['t','true','True',True]:
                if layout['legend'] is not None:
                    layout['legend']['itemsizing'] = 'constant'
                else:
                    layout['legend'] = {'itemsizing':'constant'}  
        else:
            if layout['legend'] is not None:
                    layout['legend']['itemsizing'] = 'constant'
            else:
                layout['legend'] = {'itemsizing':'constant'}

    #### Histogram Specific Layout
    if viz_type.lower() == 'histogram' and (metadata['viz_subtype'].lower() in
            ['cate_histogram', 'category_histogram', 'categorical_histogram']):
        layout['barmode'] = metadata['barmode']
        

    return layout
