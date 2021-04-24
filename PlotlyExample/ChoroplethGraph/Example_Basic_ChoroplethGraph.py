import pandas as pd
import plotly
import plotly.figure_factory as ff
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

df_rent = pd.read_csv('../Data/county_avg_rent.csv')
df_fips = pd.read_csv('../Data/countyfips.csv')

df = df_rent.merge(df_fips, on='countyname', how='inner')
df = df[(df['fips'] >= 6000) & (df['fips'] <= 7000)]

# Define the endpoints 
endpts = list(range(1,6))

fig = ff.create_choropleth(
	  fips = df['fips'], values = df['median_sqft_price'], 
	  colorscale = plotly.colors.sequential.Oranges,
	  show_state_data = True, scope = ['CA'],
	  binning_endpoints=endpts,
	  county_outline={'color': 'rgb(15,15,55)', 'width': 1},
	  state_outline={'color': 'rgb(15,15,55)', 'width': 1},
	  legend_title='Median Rent')

fig.update_layout(title={'text':'Median Rent per Square Foot by County', 'x':0.5})

plotly.offline.plot(fig, filename='basic_choropleth.html')
