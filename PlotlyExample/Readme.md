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
