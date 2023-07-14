from check_metadata import *
from generate_bar import generate_simplebar, generate_complexbar
from generate_boxplot import generate_boxplot


def generate_plotlydata(df, metadata, viz_type):
    # Check if Optional args exist:
    text = check_text(metadata)
    textposition = check_textposition(metadata)
    textfont = check_textfont(metadata)

    # Call the function for respective viz_type
    # Bar Chart
    if viz_type.lower() == 'bar':
        # Check if Optional args exist:
        bar_colour = check_barcolour(metadata)

        # Currently only support 1 column dataset only
        if metadata['viz_subtype'].lower() == 'simple':
            data = generate_simplebar(
                df[metadata['x']], df[metadata['y']], text, bar_colour,
                textposition, textfont)

        # Group or Stack Bar Chart
        # Mode whether Group or Stack Bar is set in layout.py
        if metadata['viz_subtype'].lower() == 'group' or metadata['viz_subtype'].lower() == 'stack':
            cate_col = check_cate_col(metadata)
            data = generate_complexbar(df, metadata['x'], metadata['y'],
                                       cate_col, text, bar_colour,
                                       textposition, textfont)

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

    else:
        data = None

    return data
