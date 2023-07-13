def generate_layout(title=None, xaxis=None, yaxis=None, legend=None,
                    plot_bgcolor='rgba(0,0,0,0)'):
    # Handle title
    if type(title) == str:
        title = {'text': title, 'x': 0.5}
    elif type(title) == dict:
        pass
    else:
        title = {'text': '**Title Type Error!!!', 'x': 0.5}

    # Handle xaxis
    if type(xaxis) == str:
        xaxis = {'title': xaxis}
    elif type(xaxis) == dict:
        pass
    else:
        xaxis = {'title': '**X-axis Type Error!!!'}

    # Hand yaxis
    if type(yaxis) == str:
        yaxis = {'title': yaxis}
    elif type(yaxis) == dict:
        pass
    else:
        yaxis = {'title': '**Y-axis Type Error!!!', 'gridcolor': 'lightgray'}

    # Handle Legend
    if type(legend) == dict:
        pass
    else:
        legend = {'x': 0.7, 'y': 1, 'orientation': 'h'}

    # Put all metadata together
    layout = {
        'title': title,
        'xaxis': xaxis,
        'yaxis': yaxis,
        'legend': legend,
        'plot_bgcolor': plot_bgcolor
    }

    return layout
