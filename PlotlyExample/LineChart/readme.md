# Line Chart
Line chart is a visualization that uses lines to connect a series of data points to show the trend of categories of data. Line Chart and Scatter Plot in Plotly use the same module to plot the visualization. In this folder, we are going to go over how to create line charts with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>Coming Soon...</li>
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
	<li>Coming Soon</li>
	<li><i></i></li>
</ul>

## Syntax
### Data
Data is a list of <i>go.Scatter()</i>, each <i>go.Scatter()</i> represents a category of points and/or a line.
<br><br> 
If the data list has only 1 <i>go.Scatter()</i>, it is a line or a collection of points (If it is a collection of points, refer to the [ScatterPlot folder](../ScatterPlot)).
<br><br>
go.Scatter() has the following parameters:
<ul>
	<li>x: Attribute on x-axis</li>
	<li>y: Value on y-axis</li>
	<li>name: Category, which will be displayed on legend</li>
	<li>mode: Setting on how to display
		<ul>
			<li>lines: Display in lines only</li>
			<li>lines+maker: Dispaly in lines with data points</li>
			<li></li>
		</ul>
	</li>
	<li>stackgroup: Setting on stacking lines
		<ul>
			<li>Coming Soon...</li>
		</ul>
	</li>
	<li>text: The text label will displayed on the lines</li>
	<li>textposition: Text label position
		<ul>
			<li>auto: On the top of the bar</li>
			<li>inside: On the top of the bar</li>
			<li>outside: Outside of the bar</li>
		</ul>
	</li>
	<li>textfont (Dictionary): Text label setting</li>
	<li>marker_color: Bar colour (Take colour spelliing in string or RGB in string)</li>
	<li>hoverinfo: What information to be displayed when user hover over the bar, all the options are:
		<ul>
			<li>percent</li>
			<li>label+percent</li>
			<li>label</li>
			<li>name</li>
		</ul></li>
</ul>
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
		</ul></li>
	<li>yaxis (Dictionary): y-axis setting
		<ul>
			<li>tickmode: Setting of ticks</li>
			<li>tickangle: Degree the tick rotate (-: Anticlockwise, +: Clockwise)</li>
			<li>dtick: The frequency the labels appear, the default setting is determined automatically</li>
		</ul></li>
	</li>
</ul>
<br><br>

Line Chart Exclusive parameters:
<ul>
	<li>Coming Soon...</li>
</ul>

## Examples
Coming Soon...