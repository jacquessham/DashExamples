### Universal Viz Arg
def check_text(metadata):
    if 'text' in metadata:
        return metadata['text']
    return None

### Universal Viz Arg
def check_textposition(metadata):
    if 'textposition' in metadata:
        return metadata['textposition']
    elif 'text_position' in metadata:
        return metadata['text_position']
    return None

### Universal Viz Arg
def check_hoverinfo(metadata):
    if 'hoverinfo' in metadata:
        return metadata['hoverinfo']
    return 'none' # To turn it off

### Universal Viz Arg
def check_name(metadata):
    if 'name' in metadata:
        return metadata['name']
    return None

### Bar Arg
def check_width(metadata):
    if 'width' in metadata:
        return metadata['width']
    return None

### Bar, Boxplot Arg
def check_textfont(metadata):
    if 'textfont' in metadata:
        return metadata['textfont']
    elif 'text_font' in metadata:
        return metadata['text_font']
    return None

### Bar, Boxplot Arg
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

### Bar, Line, Histogram Arg
def check_cate_col(metadata):
    if 'cate_col' in metadata:
        return metadata['cate_col']
    elif 'category_column' in metadata:
        return metadata['category_column']
    elif 'category_col' in metadata:
        return metadata['category_col']
    return None

### Boxplot Arg
def check_boxmean(metadata):
    if 'boxmean' in metadata:
        return metadata['boxmean']
    return None

### Line Chart
# Return a boolean value
def check_datapoints(metadata):
    if 'datapoints' in metadata:
        return metadata['datapoints'] in ['t', 'true', 'True']
    elif 'data_points' in metadata:
        return metadata['data_points'] in ['t', 'true', 'True']
    return False

### Line Chart
def check_line_colour(metadata):
    if 'line_colour' in metadata:
        return metadata['line_colour']
    elif 'line_color' in metadata:
        return metadata['line_color']
    return None

### Scatterplot/Bubble Chart, Heatmap
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

### Scatterplot/Bubble Chart
def check_add_colourscale(metadata):
    if 'addition_colourscale' in metadata:
        return metadata['addition_colourscale']
    elif 'addition_colorscale' in metadata:
        return metadata['addition_colorscale']
    return None

### Scatterplot/Bubble Chart
def check_colour_scheme(metadata):
    if 'colour_scheme' in metadata:
        return metadata['colour_scheme']
    elif 'color_scheme' in metadata:
        return metadata['color_scheme']
    elif 'colour_choices' in metadata:
        return metadata['colour_choices']
    elif 'colour_choices' in metadata:
        return metadata['color_choices']
    return None

### Scatterplot/Bubble Chart
# Return a boolean value
def check_showlegend(metadata):
    if 'showlegend' in metadata:
        return metadata['showlegend'] in ['t','true','True', True]
    return True # Should show showscale by default

### Scatterplot/Bubble Chart
# Return a boolean value
def check_showscale(metadata):
    if 'showscale' in metadata:
        return metadata['showscale'] in ['t','true','True', True]
    return True # Should show showscale by default

### Histogram
def check_histnorm(metadata):
    if 'histnorm' in metadata:
        return metadata['histnorm']
    return None

### Histogram
def check_cumulative_enabled(metadata):
    if 'cumulative' in metadata:
        return metadata['cumulative'] in ['t','true','True', True]
    elif 'cumulative_enabled' in metadata:
        return metadata['cumulative_enabled'] in ['t','true','True', True]
    return False

### Histogram
def check_histfunc(metadata):
    if 'histfunc' in metadata:
        return metadata['histfunc']
    return 'count' # By default, return count
