import plotly
import plotly.graph_objs as go


""" Function to prepare data list in data.py for candlestick chart """
def generate_candlestick(x, open_price, high_price, low_price, close_price):
    return go.Candlestick(x=x, open=open_price, high=high_price, low=low_price,
                              close=close_price)