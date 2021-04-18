import pandas as pd
import yfinance
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

apple = yfinance.Ticker('AAPL')
df = apple.history(period='ytd').reset_index()

data = []
data.append(go.Candlestick(x=df['Date'], open=df['Open'],
	                       high=df['High'], low=df['Low'],
	                       close=df['Close']))
layout = {'title':{'text':'Year-to-Date Apple Stock Price','x':0.5},
          'xaxis':{'title':'Date','rangeslider':{'visible':False}},
		  'yaxis':{'title':'Price ($)'},
          'hovermode':False}
fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='apple_candlestick.html')
