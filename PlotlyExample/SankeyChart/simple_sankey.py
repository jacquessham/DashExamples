import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Define label and its corresponding colours
num2name_colour = {
	0:{'label':'Person 4 Golden','pad_colour':'gold','link_colour':'lightyellow'},
	1:{'label':'Persona 5 Royal','pad_colour':'red','link_colour':'pink'},
	2:{'label':'Altas','pad_colour':'purple','link_colour':'mediumpurple'},
	3:{'label':'Sega','pad_colour':'blue','link_colour':'lightblue'},
	4:{'label':'PS4','pad_colour':'black','link_colour':'lightgray'},
	5:{'label':'PC','pad_colour':'white','link_colour':'lightgray'},
	6:{'label':'Yakuza 7','pad_colour':'yellow','link_colour':'lightyellow'},
	7:{'label':'Flight Simulator','pad_colour':'blue','link_colour':'lavender'}

}

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = [num2name_colour[k]['label'] for k in num2name_colour],
      color = [num2name_colour[k]['pad_colour'] for k in num2name_colour]
    ),
    link = dict(
      source = [0,1,2,3,3,6,7], 
      target = [2,2,3,4,5,3,5],
      value = [400,320,400+320,200+320+120,200,120,250],
      color = [num2name_colour[0]['link_colour'],
      		num2name_colour[1]['link_colour'],
      		num2name_colour[2]['link_colour'],
      		num2name_colour[3]['link_colour'],
      		num2name_colour[3]['link_colour'],
      		num2name_colour[6]['link_colour'],
      		num2name_colour[7]['link_colour']
      ]
  ))])

fig.update_layout(title_text="Hours of Video Games Played on Console")

plotly.offline.plot(fig, filename='simple_sankey.html')
