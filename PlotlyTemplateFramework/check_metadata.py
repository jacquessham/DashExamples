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

# Bar Arg
def check_cate_col(metadata):
    if 'cate_col' in metadata:
        return metadata['cate_col']
    elif 'category_column' in metadata:
        return metadata['category_column']
    elif 'category_col' in metadata:
        return metadata['category_col']
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

# Boxplot Arg
def check_boxmean(metadata):
    if 'boxmean' in metadata:
        return metadata['boxmean']
    return None
