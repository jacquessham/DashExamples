from generate_bar import *


# Currently only support 1 column dataset only
# Bar Chart only
def generate_plotlydata(x, y, viz_type):
    data = []

    if viz_type == 'bar' or viz_type == 'Bar':
        data.append(generate_simplebar(x, y))

    return data
