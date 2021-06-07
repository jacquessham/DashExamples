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
	<li><i>revenue_dept.csv</i></li>
	<li><i>expense_dept.csv</i></li>
</ul>

### revenue.csv
<i>revenue.csv</i> is a data set to display the revenue of a hypothetical department store by category, without a time dimension. 

### expense.csv
<i>expense.csv</i> is a data set to display the expense of a hypothetical department store by category, without a time dimension. 

## Syntax
### Data
Data is a list of <i>go.Pie()</i>, each <i>go.Pie()</i> represents a pie chart. Each <i>go.Pie()</i> you added in the data list, one more pie chart will be displayed. If you want a donut chart, add a <i>hole</i> parameter in <i>go.Pie()</i> to convert the pie chart to a donut chart

<br><br>
go.Pie() has the following parameters:
<ul>
	<li>label: Attribute of the chart</li>
	<li>value: Value for the given attribute, takes the values (not percentage, unless you insists)</li>
	<li>name: Category, which will be used for identifying the pie chart (More useful when you have more than 1 pie chart)</li>
	<li>hole: The size of the hole in the center, takes between 0 and 1. It represents the hole radius relative to the radius of the pie. It defaults at 0, as a pie chart. When hole is greater than 0, it becomes a donut chart</li>
	<li>hoverinfo: What information to be displayed when user hover over the pie slices, all the options are:
		<ul>
			<li>percent</li>
			<li>label+percent</li>
			<li>label</li>
			<li>name</li>
		</ul></li>
	<li>textinfo: What information to be displayed on the pie slices, default as <b>percent</b>, all the options are:
		<ul>
			<li>percent</li>
			<li>label+percent</li>
			<li>label</li>
			<li>name</li>
		</ul></li>
	<li>textfont_size: Font of the text on the pie</li>
	<li>marker (Dictionary): To define colour of each pie and borders
		<ul>
			<li>colors: A list of colours to be used for pies</li>
			<li>line (Dictionary): To specify color and width for border
				<ul>
					<li>color</li>
					<li>width</li>
				</ul></li>
		</ul></li>
	<li>insidetextorientation: Controls the orientation of the text inside chart sectors
		<ul>
			<li>auto: Oriented in any direction to have the largest font possible</li>
			<li>horizontal: Parallel with the bottom line (Horizaontal)</li>
			<li>radial: Oriented along the radius</li>
			<li>tangential: Perpendicular to the radius</li>
		</ul></li>
	<li>pull: "Pull-out" the pie from the center, take 0-1 for each pie</li>
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
	<li>uniformtext_minsize: Threhold of font size to be displayed on the pie, if not, will be handled with instruction stated in <i>uniformtext_mode</i>, default to be 0</li>
	<li>uniformtext_mode: How to handle text if the font is less than <i>uniformtext_minsize</i>
		<ul>
			<li>hide: Do not display</li>
			<li>show: Display without downscaling</li>
		</ul></li>
</ul>
<br><br>

Pie/Donut Chart Exclusive parameters:
<ul>
	<li>hole: The size of the hole in the center</li>
	<li>pull: "Pull-out" the pie from the center</li>
</ul>

## Examples
### Example 1 - Simple Pie Chart
Require files: <i>revenue_dept.csv</i> in the [Data folder](../Data)
<br>
<img src=simplepie.png>

```
data = []
data.append(go.Pie(labels=df['category'], values=df['revenue']))

# Layout
layout = {'title':{'text':'Department Store Revenue', 'x':0.5}}

```

### Example 2 - Grouped Donut Chart
Require files: <i>revenue_dept.csv</i> in the [Data folder](../Data)
<br>
<img src=simpledonut.png>

```
data = []
data.append(go.Pie(labels=df['category'], values=df['revenue'], hole=0.4))

# Layout
layout = {'title':{'text':'Department Store Revenue', 'x':0.5}}
```

### Example 3 - Pie Chart with Advance setting
Require files: <i>revenue_dept.csv</i> in the [Data folder](../Data)
<br>
<img src=prettypie.png>
<br>
See <i>Pretty_pie.py</i> in this folder for the code.

### Example 4 - Multiple Pie Charts
Require files: <i>revenue_dept.csv</i> and <i>expense_dept.csv</i> in the [Data folder](../Data)
<br>
<img src=multi_pies.png>
<br>
Multiple Pie charts required users to declare subplots in <i>figure</i> first that it requires different style of code to do so, see <i>Multiple_pies.py</i> in this folder for the code.