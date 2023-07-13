import plotly
import plotly.graph_objs as go


def generate_boxplot(df, category_col, y_col,
                     bar_colour=None, boxmean=None, textposition='auto'):
    # Check len of bar_colour is same as len category_col, would fail if not
    if bar_colour is not None and len(bar_colour) != category_col:
        bar_colour = None

    # Prepare Data
    data = []

    for category in df[category_col].unique():
        df_temp = df[df[category_col] == category]
        data.append(
            go.Box(
                y=df_temp[y_col],
                name=category,
                marker_color=bar_colour,
                boxmean=boxmean
            )
        )

    return data
