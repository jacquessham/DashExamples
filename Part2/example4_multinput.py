import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

data = pd.read_csv('Air_Traffic_Passenger_Statistics.csv')
data['Activity Period'] = data['Activity Period'].astype(str)
data['Year'] = data['Activity Period'].str[:4].astype(int)
data['Month'] = data['Activity Period'].str[5:].astype(int)

selected_column = 'GEO Summary'
data = data[['Published Airline','Year','Month','Passenger Count',
             selected_column]]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

