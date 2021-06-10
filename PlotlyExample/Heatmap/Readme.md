# Heatmaps
Heatmap. In this folder, we will go over how to create bar charts with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>Simple_heatmap.py</li>
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

### cust_num.csv
<i>cust_num.csv</i> is data set that records the customer traffic of a hypothetical department store by day of week and hours.

## Syntax
### Data
Data is a list to store <i>go.Heatmap()</i>.
<br><br>
go.heatmap() has the following parameters:
<ul>
	<li>x: Attribute on x-axis</li>
	<li>y: Attribute on y-axis</li>
	<li>z: Value of the attribute on x and y-axis, and display in colour</li>
	<li>colorscale: The colour scale on how data is displayed, depends on z</li>
	<li>hoverongaps: When there is missing value in the data, it will not show hovertext if this column is set to false (Default to true)</li>
	<li>hoverinfo: What information to be displayed when user hover over the coloured area, all the options are:
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
		</ul></li>
	<li>yaxis (Dictionary): y-axis setting
		<ul>
			<li>tickmode: Setting of ticks</li>
			<li>tickangle: Degree the tick rotate (-: Anticlockwise, +: Clockwise)</li>
		</ul></li>
</ul>
<br><br>

Heatmap Exclusive parameters:
<ul>
	<li>z: Value of the attribute on x and y-axis</li>
	<li>hoverongaps: Display or not if data is missing</li>
</ul>

## Examples
### Example 1 - Simple Heatmap
<img src=simpleheatmap.png>

```
# Data
data = []
data.append(go.Heatmap(z=df['customers_count'],
	                   x=df['day'], y=df['hour'],
	                   colorscale='ylorrd'))

# Layout
layout = {'title':{'text':'Department Store Traffic',
	               'x':0.5},
	      'xaxis': {'tickmode':'linear'},
	      'yaxis': {'tickmode':'linear'}}

```
