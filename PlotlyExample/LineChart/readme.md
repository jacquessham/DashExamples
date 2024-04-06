# Line Chart
Line chart is a visualization that uses lines to connect a series of data points to show the trend of categories of data. Line Chart, Bubble Chart and Scatter Plot in Plotly use the same module to plot the visualization. In this folder, we are going to go over how to create line charts with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>SimpleLinechart.py</li>
	<li>SimpleLinechart_points.py</li>
	<li>Mutlilines_Linechart.py</li>
</ul>

## Pacakges Needed
This chapter requires the following packages for the scripts used:
<ul>
	<li>Pandas</li>
	<li>Plotly</li>
</ul>

## Data Used
This chapter may use the following data from the [Data folder](../Data):
<ul>
	<li><i>cust_num.csv</i></li>
</ul>

## Syntax
### Data
Data is a list of <i>go.Scatter()</i>, each <i>go.Scatter()</i> represents a category of points and/or a line.
<br><br> 
If the data list could have 1 or mutliple <i>go.Scatter()</i>, to represent a line, or mutliple lines. If it is a collection of points, refer to the [ScatterPlot folder](../ScatterPlot).
<br><br>
go.Scatter() has the following parameters:
<ul>
	<li>x: Attribute on x-axis</li>
	<li>y: Value on y-axis</li>
	<li>line: In depth setting for data point, including
		<ul>
			<li>color: Set color for the line, accept RGB values/Colour keywords</li>
		</ul>
	</li>
	<li>mode: Setting on how to display
		<ul>
			<li>markers: Display data points only</li>
			<li>lines: Display in lines only</li>
			<li>lines+maker: Dispaly in lines with data points</li>
		</ul>
	</li>
	<li>name: Explanation shown in legend</li>
	<li>text: The text label will displayed on the lines</li>
	<li>textfont (Dictionary): Text label setting</li>
	<li>hoverinfo: What information to be displayed when user hover over the bar, all the options are:
		<ul>
			<li>percent</li>
			<li>label+percent</li>
			<li>text</li>
			<li>name</li>
		</ul></li>
</ul>
<br>
<br>


### Layout
Genetic Layout parameters suggested to use:
<ul>
	<li>title (Dictionary): Chart title and fonts 
		<ul>
			<li>text: Chart title to be displayed</li>
			<li>x: text location on x-dimension, from 0-1</li>
			<li>y: text location on y-dimension, from 0-1</li>
		</ul></li>
	<li>xaxis (Dictionary): X-axis setting
		<ul>
			<li>tickmode: Setting of ticks</li>
			<li>tickangle: Degree the tick rotate (-: Anticlockwise, +: Clockwise)</li>
			<li>categoryorder: Sort the order of attributes on X-axis, either ascending or descending
				<ul>
					<li>category ascending: Sort attribute (attribute in name in Data) in ascending orders</li>
					<li>category descending: Sort attribute (attribute in name in Data) in descending orders</li>
					<li>total ascending: Sort value in ascending orders</li>
					<li>total descending: Sort value in descending orders</li>
					<li>min ascending/min descending: Sort by minimum value</li>
					<li>max ascending/max descending: Sort by maximum value</li>
					<li>sum ascending/sum descending: Sort by summation value</li>
					<li>mean ascending/mean descending: Sort by average value</li>
					<li>median ascending/median descending: Sort by median value</li>
					<li>array: Follow the sorting order defined in <b>categoryarray</b></li>
				</ul>
			</li>
			<li>dtick: The frequency the labels appear, the default setting is determined automatically</li>
			<li>categoryarray: Define the sorting order when <b>categoryorder is array</b></li>
			<li>type: Set axis scale, default is linear (linear, log, date, category, multicategory)</li>
		</ul></li>
	<li>yaxis (Dictionary): y-axis setting
		<ul>
			<li>tickmode: Setting of ticks</li>
			<li>tickangle: Degree the tick rotate (-: Anticlockwise, +: Clockwise)</li>
			<li>dtick: The frequency the labels appear, the default setting is determined automatically</li>
			<li>type: Set axis scale, default is linear (linear, log, date, category, multicategory)</li>
		</ul></li>
	</li>
</ul>
<br><br>

Line Chart Exclusive parameters:
Scatter Plot Exclusive parameters:
<ul>
	<li>marker_color</li>
	<li>marker</li>
</ul>

## Examples
### Example 1 - Simple Line Chart
<img src=simple_linechart.png>

```
# Data
data = []
data.append(go.Scatter(x=df['hour'], y=df['customers_count'],
					mode='lines'))
# Layout
layout = {'title':{'text':'Number of Customer Trend', 'x':0.5}}

fig = go.Figure(data=data, layout=layout)
```

Note: Simply use <i>go.Scatter()</i> and set mode to <i>lines</i>

### Example 2 - Simple Line Chart with Data Points

<img src=simple_linechart_points.png>

```
# Data
data = []
data.append(go.Scatter(x=df['hour'], y=df['customers_count'],
					mode='lines+markers'))
# Layout
layout = {'title':{'text':'Number of Customer Trend', 'x':0.5}}

fig = go.Figure(data=data, layout=layout)
```

### Example 3 - Multiple Lines Line Chart

<img src=multilines.png>

```
colour_scheme = ['red','blue','black','orange','yellow','brown','green']

# Data
data = []
for day, colour in zip(df['day'].unique(), colour_scheme):
	df_temp = df[df['day']==day]
	data.append(go.Scatter(x=df_temp['hour'], y=df_temp['customers_count'],
						line={'color': colour},
						name=day,
						mode='lines'))
# Layout
layout = {'title':{'text':'Number of Customer Trend by Days', 'x':0.5}}
```

## Reference
Plotly Documentation <a href="https://plotly.com/python/line-charts/">Line Chart</a>