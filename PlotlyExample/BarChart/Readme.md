# Bar Charts
In this folder, we will go over how to create bar charts with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>Simplebar.py</li>
	<li>Groupbar.py</li>
	<li>Stackbar.py</li>
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
	<li><i>expense.csv</i></li>
</ul>

## Syntax
### Data
Data is a list of <i>go.Bar()</i>, each <i>go.Bar()</i> represents a category of bars.
<br><br> 
If the data list has only 1 <i>go.Bar()</i>, it is a simple bar chart: Each attribute has only 1 bar.
<br><br>
If it is grouped, each attribute has a group of bars displayed (All bars belong to each attribute stick together) ordered by the order in the data list.
<br><br>
If it is stacked, each attribute has one bar, each category value would be stacked on top of other categories order by the the order in the data list.
<br><br>
go.Bar() has the following parameters:
<ul>
	<li>x: Attribute on x-axis</li>
	<li>y: Value on y-axis</li>
	<li>name: Category, which will be displayed on legend</li>
	<li>text: The text label will displayed on the bars</li>
	<li>textposition: Text label position
		<ul>
			<li>auto: On the top of the bar</li>
			<li>inside: On the top of the bar</li>
			<li>outside: Outside of the bar</li>
		</ul>
	</li>
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
	<li></li>
	<li></li>
	<li></li>
</ul>
<br><br>

Bar Chart Exclusive parameters:
<ul>
	<li>barmode: How the bars are grouped
		<ul>
			<li>grouped: Bars stick together if they belong to the same attribute</li>
			<li>stacked: Bars stack on top of each other if they belong to the same attribute</li>
		</ul></li>
</ul>

## Examples
### Example 1 - Simple Bar Chart
<img src=bar.png>
Coming Soon...

### Example 2 - Grouped Bar Chart
<img src=groupbar.png>
Coming Soon...

### Example 3 - Stacked Bar Chart
<img src=stackbar.png>
Coming Soon...