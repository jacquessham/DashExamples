from generate_bar import *


# Currently only support 1 column dataset only
# Bar Chart only
def generate_plotlydata(df, metadata, viz_type):
    data = []

    if viz_type.lower() == 'bar':
        if metadata['viz_subtype'].lower() == 'simple':
            data.append(generate_simplebar(
                df[metadata['x']], df[metadata['y']]))

    return data
