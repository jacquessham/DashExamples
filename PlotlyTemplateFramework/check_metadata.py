# Universal Viz Arg
def check_text(metadata):
    if 'text' in metadata:
        return metadata['text']
    return None

# Universal Viz Arg
def check_textposition(metadata):
    if 'textposition' in metadata:
        return metadata['textposition']
    elif 'text_position' in metadata:
        return metadata['text_position']
    return None

# Universal Viz Arg
def check_hoverinfo(metadata):
    if 'hoverinfo' in metadata:
        return metadata['hoverinfo']
    return 'none' # To turn it off

# Universal Viz Arg
def check_name(metadata):
    if 'name' in metadata:
        return metadata['name']
    return None

# Bar Arg
def check_width(metadata):
    if 'width' in metadata:
        return metadata['width']
    return None

# Bar, Boxplot Arg
def check_textfont(metadata):
    if 'textfont' in metadata:
        return metadata['textfont']
    elif 'text_font' in metadata:
        return metadata['text_font']
    return None

# Bar, Boxplot Arg
def check_barcolour(metadata):
    # Allow user to spell English and American English and use of _
    if 'barcolour' in metadata:
        return metadata['barcolour']
    elif 'bar_colour' in metadata:
        return metadata['bar_colour']
    elif 'barcolor' in metadata:
        return metadata['barcolor']
    elif 'bar_color' in metadata:
        return metadata['bar_color']
    return None

# Bar, Line Arg
def check_cate_col(metadata):
    if 'cate_col' in metadata:
        return metadata['cate_col']
    elif 'category_column' in metadata:
        return metadata['category_column']
    elif 'category_col' in metadata:
        return metadata['category_col']
    return None

# Boxplot Arg
def check_boxmean(metadata):
    if 'boxmean' in metadata:
        return metadata['boxmean']
    return None

# Line Chart
# Return a boolean value
def check_datapoints(metadata):
    if 'datapoints' in metadata:
        return metadata['datapoints'] in ['t', 'true', 'True']
    elif 'data_points' in metadata:
        return metadata['data_points'] in ['t', 'true', 'True']
    return False

def check_line_colour(metadata):
    if 'line_colour' in metadata:
        return metadata['line_colour']
    elif 'line_color' in metadata:
        return metadata['line_color']
    return None

# Scatterplot/Bubble Chart
def check_colourscale(metadata):
    if 'colourscale' in metadata:
        return metadata['colourscale']
    elif 'colorscale' in metadata:
        return metadata['colorscale']
    elif 'colour_scale' in metadata:
        return metadata['colour_scale']
    elif 'color_scale' in metadata:
        return metadata['color_scale']
    return None

# Return a boolean value
def check_showscale(metadata):
    if 'showscale' in metadata:
        return metadata['showscale'] in ['t','true','True', True]
    return True # Should show showscale by default