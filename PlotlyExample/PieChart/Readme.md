# Pie/Donut Charts
Pie chart is a visualization which displays the numerical proportion of each attribute in the data set. A donut chart is a pie chart, except there is a hole in the center of the pie. In this folder, we will go over how to create bar charts with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>Simple_pie.py</li>
	<li>Simple_donut.py</li>
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
	<li><i>revenue.csv</i></li>
</ul>

### revenue.csv
<i>revenue.csv</i> is a data set to display the revenue of a hypothetical department store by category, without a time dimension. 

## Syntax
### Data (Under Construction)
Data is a list of <i>go.Pie()</i>, each <i>go.Pie()</i> represents a pie chart. Each <i>go.Pie()</i> you added in the data list, one more pie chart will be displayed. If you want a donut chart, add a <i>hole</i> parameter in <i>go.Pie()</i> to convert the pie chart to a donut chart

<br><br>
go.Pie() has the following parameters:
<ul>
	<li>label: Attribute of the chart</li>
	<li>value: Value for the given attribute, takes the values (not percentage, unless you insists)</li>
	<li>name: Category, which will be used for identifying the pie chart (More useful when you have more than 1 pie chart)</li>
	<li>hole: The size of the hole in the center, takes between 0 and 1. It represents the hole radius relative to the radius of the pie. It defaults at 0, as a pie chart. When hole is greater than 0, it becomes a donut chart</li>
	<li>textinfo: What information to be displayed on the pie slices, default as <b>percent</b>, all the options are:
		<ul>
			<li>percent</li>
			<li>label+percent</li>
		</ul></li>
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
</ul>
<br><br>

Pie/Donut Chart Exclusive parameters:
<ul>
	<li>hole: The size of the hole in the center</li>
</ul>

## Examples
### Example 1 - Simple Pie Chart
<img src=simplepie.png>

```
data = []
data.append(go.Pie(labels=df['category'], values=df['revenue']))

# Layout
layout = {'title':{'text':'Department Store Revenue', 'x':0.5}}

```

### Example 2 - Grouped Donut Chart
<img src=simpledonut.png>

```
data = []
data.append(go.Pie(labels=df['category'], values=df['revenue'], hole=0.4))

# Layout
layout = {'title':{'text':'Department Store Revenue', 'x':0.5}}
```
