# Box Plots
Box Plots are plots to display the statistics of the given data, including median, quartiles, sometimes mean, and even outliers. In this folder, we will go over how to create box plots with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>Example_box.py</li>
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
	<li><i>salary.csv</i></li>
</ul>

## Syntax
### Data (Under Construction)
Data is a list of <i>go.Box()</i>, each <i>go.Box()</i> represents an attribute. If the data list has only 1 <i>go.Box()</i>, there is only 1 attribute (Only 1 box bar presents).
<br><br>
go.Bar() has the following parameters:
<ul>
	<li>x: Value on x-axis (Horizontal Box Plot, if used, <b>y</b> should be empty)</li>
	<li>y: Value on y-axis (Vertical Box Plot, if used, <b>x</b> should be empty)</li>
	<li>name: Attribute, it will be represented as 1 box bar and displayed on x-axis</li>
	<li>boxmean: Parameter whether the mean is presented on the chart, takes only <b>True</b> and <b>False</b>, default as <b>False</b></li>
	<li>textfont (Dictionary): Text label setting</li>
</ul>
<br>


### Layout (Under Construction)
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
			<li></li>
		</ul></li>
	<li>xaxis (Dictionary): y-axis setting
		<ul>
			<li>tickmode: Setting of ticks</li>
			<li></li>
		</ul></li>
	<li></li>
</ul>
<br><br>
Box Plot Exclusive parameters:
<ul>
	<li>boxmean: Parameter whether the mean is presented on the chart</li>
</ul>

### Syntax Difference with Bar Chart
One difference between box plot and bar chart is syntax used for attribute and values. In box plot's <i>go.Box()</i>, <b>name</b> is used for attribute while either <b>x</b> or <b>y</b> is used for values. Note that, no error will be threw if both x and y are passed with values. However, it does not display the proper box plot as desired. Therefore, only pass the values with x or y, never pass both parameters (Meaning: Only use <b>y</b> and <b>name</b> if you want vertical box plot or use <b>x</b> and <b>name</b> if you want horizontal box plot)

## Examples
<img src=box.png>
