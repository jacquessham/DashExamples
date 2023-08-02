# Scatter Plot
Scatter Plot is a visualization display the relationship of data between two dimension of attributes. Line Chart, Bubble Chart and Scatter Plot in Plotly use the same module to plot the visualization. In this folder, we are going to go over how to create scatter plots with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>SimpleScatterplot.py</li>
	<li>NumColourScatterplot.py</li>
	<li>CateColourScatterplot.py</li>
	<li>Bubblechart.py</li>
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
	<li><i>tips.csv</i></li>
</ul>

## Syntax
### Data
Data is a list of <i>go.Scatter()</i>, each <i>go.Scatter()</i> represents a category of points and/or a line.
<br><br> 
If the data list has only 1 <i>go.Scatter()</i>, it is a line or a collection of points (If it is a line, refer to the [Line Chart folder](../LineChart)).
<br><br>
go.Scatter() has the following parameters:
<ul>
	<li>x: Attribute on x-axis</li>
	<li>y: Value on y-axis</li>
	<li>marker_color: Display the color based on a numeric column</li>
	<li>marker: In depth setting for data point, including
		<ul>
			<li>size: Numeric value for the data point size</li>
			<li>color: Same as marker_color</li>
			<li>colorscale: colourscale if color is a numeric array</li>
			<li>showscale (True/False): If colorscale presents, show the scale. It does not work when color is passed with RGB values/Colour keywords</li>
			<li>autocolorscale (True/False): Automatically choose a colorscale when color is a numeric array if no value is set for colorscale</li>
		</ul>
	</li>
	<li>mode: Setting on how to display
		<ul>
			<li>markers: Display data points only</li>
			<li>lines: Display in lines only</li>
			<li>lines+maker: Dispaly in lines with data points</li>
			<li></li>
		</ul>
	</li>
	<li>text: The text label will displayed on the lines</li>
	<li>textfont (Dictionary): Text label setting</li>
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

Scatter Plot Exclusive parameters:
<ul>
	<li>marker_color</li>
	<li>marker</li>
</ul>

## Examples
### Example 1 - Simple Scatterplot

<img src=simple_scatterplot.png>

```
# Data
data = []
data.append(go.Scatter(x=df['grand_total'], y=df['tips'],
					mode='markers'))
# Layout
layout = {'title':{'text':'Everybody\'s Tipping Distribution', 'x':0.5}}
```

<b>Note: You must set mode='markers', or else the data points would be connected</b>

### Example 2 - Coloured Scatterplot (With a 3rd Numeric Dimension)

<img src=numdim_scatterplot.png>

```
data = []
data.append(go.Scatter(x=df['grand_total'], y=df['tips'],
					marker_color=df['wait_mins'], 
					mode='markers'))
# Layout
layout = {'title':{'text':'Everybody\'s Tipping Distribution', 'x':0.5}}
```

### Example 3 - Coloured Scatterplot (With a 3rd Numeric Dimension)

<img src=catedim_scatterplot.png>

```
meal_type_color = [color_scheme[meal] for meal in df['meal_type'].tolist()]

# Data
data = []
data.append(go.Scatter(x=df['grand_total'], y=df['tips'],
					marker_color=meal_type_color,
					mode='markers'))
# Layout
layout = {'title':{'text':'Everybody\'s Tipping Distribution', 'x':0.5}}
```

Note 1: marker_color accepts both numeric values or RGB values/Colour keywords.
<b>Note 2: However, you must convert a categorical label to RGB values/Colour keywords</b>

### Example 4 - Advance Marker Configuration (Bubble Chart)

<img src=bubblechart.png>

```
meal_type_color = [color_scheme[meal] for meal in df['meal_type'].tolist()]

# Data
data = []
data.append(go.Scatter(x=df['grand_total'], y=df['tips'],
					marker={
						'size': df['wait_mins'],
						'color': meal_type_color
					},
					mode='markers'))
# Layout
layout = {'title':{'text':'Everybody\'s Tipping Distribution', 'x':0.5}}

```


## Reference
Plotly Documentation <a href="https://plotly.com/python/line-and-scatter/">Scatter Plot</a>