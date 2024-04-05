# Plotly Fundamentals
This section would explain the basics of Plotly and how to use <b>Python</b> to generate simple Plotly charts. We will be focus on <i>plotly.graph_objs (go)</i>.

## Installation
pip install plotly==version - check <a href="https://plotly.com/python/getting-started/">Plotly documenation</a> for the latest version
<br>
pip install ipython - Plotly relies on ipython to render an interactive graph
<br>

## Setting and Basics
This tutorial lets you to generate Plotly graphs office.
<br><br>
Required package:
<ul>
	<li>plotly.graph_objs (go) - To specify the chart type</li>
	<li>plotly.offline - Allow you to generate the plot offline</li>
</ul>

<br><br>
Each Plotly chart requires the following elements:
<ul>
	<li>init_notebook_mode(connected=True)</li>
	<li>data list</li>
	<li>layout</li>
	<li>go.Figure() - object to store data list and layout</li>
	<li>plotly.offline.plot() - generate the chart and save in html</li>
</ul>
<br>



### Data list
A data list contain one or multiple plotly.graph_objs, which contains the metadata of visualization type, configuration, and data. For example, you may add a <i>go.Scatter()</i> into a list like below:

```
data = []
data.append(go.Scatter(x=df['hour'],y=df['amount']))
```

Plotly objects accepts lists, Pandas DataFrames, or NumPy Arrays.

### Layout
Layout is a dictionary consists the detailed configuration of the visualization, such as x-axis, y-axis, legend, background configuration. For example, you may set a title in this dictionary like below:

```
layout = {'title':{'text':'Number of Customer Trend by Days', 'x':0.5}}
``` 

### go.Figure()
<i>go.Figure()</i> requires two elements to generate a Plotly graph: <b>Data list</b> and <b>Layout</b>. Once <i>go.Figure()</i> has accepted both elements, you may generate a visualization with <i>plotly.offline.plot()</i>
<br><br>
After you have prepared a data list and a dictionary of layout, you may pass those as agrument into <i>go.Figure()</i>:

```
fig = go.Figure(data=data, layout=layout)
```



### plotly.offline.plot()
The function to trigger Plotly to render the visualization on a HTML page according to <i>go.Figure()</i>:

```
plotly.offline.plot(fig, filename='my_scatterplot.html')
```

Plotly would save the HTML page in the current directory, but the browser would also automatically render the HTML.

## General Layout of a Typical Simple Plotly Chart with Python

```
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df = pd.read_csv('../Data/tips.csv')

# Data
data = []
data.append(go.Scatter(x=df['grand_total'], y=df['tips'],
					mode='markers'))
# Layout
layout = {'title':{'text':'Everybody\'s Tipping Distribution', 'x':0.5}}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='simple_scatterplot.html')
```

### Logarithm Plots in Plotly
Creating a logarithm plot is very useful when visualizing very skewed data. Plotly allows you to simply pass one parameter in the layout dictionary to turn a regular plot to a logarithm plot without manually adjust the data points. Add the <i>type</i> parameter equals to <i>log</i> under the desired columns. Here is the example to take logarithm on the observations on both X-axis and Y-axis:

```
layout = {'title':{'text':'Everybody\'s Tipping Distribution', 'x':0.5},
	'xaxis':{'type':'log'}, 'yaxis':{'type':'log'}}

```

<br>
Reference: <a href="https://plotly.com/python/log-plot/#logarithmic-axes-with-graph-objects"> Plotly Documentation</a>

### Background Colour
The default background colour on Plotly plots are gray, but you may adjust it by adding the <i>plot_bgcolor</i> parameter along with the RGBA colour scale to the layout dictionary. Here is the example to turn the background colour to white:

```
layout = {'title':{'text':'Everybody\'s Tipping Distribution', 'x':0.5},
	'xaxis':{'gridcolor':'lightgray'}, 'yaxis':{'gridcolor':'lightgray'},
	'plot_bgcolor': 'rgba(0,0,0,0)'}
```

<br>
Note:
<ul>
	<li>Because after Plot BG colour is turned to white, it is hard to compare data value with the axis ticks. Therefore, it is recommended to add <i>'gridcolor':'lightgray'</i> to both X-axis and Y-axis</li>
	<li>White background and light gray grid colour is the default setting to the Template Framework</li>
</ul>


## Bar Charts
You may find how to create bar charts with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/BarChart">Bar Charts folder</a>.

## Line Charts
You may find how to create line charts with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/LineChart">Line Charts folder</a>.

## Scatter Plots/Bubble Charts
You may find how to create scatter plots with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/ScatterPlot"> Scatter Plots folder</a>.

## Box Plots
You may find how to create Box plots with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/BoxPlot">Box Plots folder</a>.

## Pie/Donut Charts
You may find how to create Pie charts/Dount charts with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/PieChart">Pie Chart folder</a>.

## Treemaps
You may find how to create Treemap with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/Treemap">Treemap folder</a>.

## Histogram
You may find how to create Histogram with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/Histogram">Histogram folder</a>.

## Heatmaps
You may find how to create Heatmap with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/Heatmap">Heatmp folder</a>.

## Candlestick Charts
You may find how to create candlestick charts with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/CandlestickChart">Candlestick Charts folder</a>.

## Choropleth Graphs
You may find how to create Choropleth graph with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/ChoroplethGraph">Choropleth Graph folder</a>.

## Sunburst Charts
You may find how to create Sunburst Charts with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/SunburstChart">Sunburst Charts folder</a>.

## Parallel Coordinates Plot
You may find how to create Parallel Coordinates Plot with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/ParallelCategories">Parallel Coordinates Plot folder</a>.

## Sankey Chart
You may find how to create Sankey Chart with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/SankeyChart">Sankey Chart folder</a>.

## Funnel Chart
You may find how to create Funnel Chart with Plotly in the <a href="https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample/FunnelChart">Funnel Chart folder</a>.
