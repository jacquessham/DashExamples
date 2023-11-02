# Plotly Template Framework
The goal of this subsection is to provide a framework to easily plot a visualization via Plotly with low code and avoid excessively copy-and-paste code from previously written Plotly script. The scripts are written in Python.

## How to use it?
You may pass all the arguements and metadata to <i>generate_plotly_viz()</i> in <i>generate_plotly.py</i> and return to your Plotly or Dash rendering object in your scripts. Alternatively, you may fill out the arguement and metadata in <i>arguements.json</i> and execute <i>call_plotly.py</i> to declare the rendering object in this driver script.
<br><br>
<b>The scripts always expect the data frame in Pandas DataFrame!!!</b>

### Integrating with Other Projects
You may copy all the <b>.py</b> scripts as a package, minus <i>call_plotly.py</i>, to your project or repository. Similarily, you may may pass all the arguements and metadata to <i>generate_plotly_viz()</i> in <i>generate_plotly.py</i> and return to your Plotly or Dash rendering object in stated in your driver script in your project. <b>The framework is purely for personal use, the functionality is very limited. There is no plan to establish the framework as open-source package.</b>

## Scripts
### call_plotly.py
A driver script to call <i>generate_plotly.py</i> to generate a Plotly visualization. If you are exporting the <i>figure</i> to Dash, you may ignore this script. In order to work, you must execute <i>arguements.json</i> before executing.

### arguements.json
The arguements and metadata to declare the Plotly rending object in <i>call_plotly.py</i>. An example of the minimum requirement of generating a bar chart is the following:

```
{
	"df_directory":"Data/salary.csv", 
	"viz_type":"Bar", 
	"viz_name":"Salary by Name",
	"metadata":{
		"x":"name", 
		"y":"salary", 
		"viz_subtype":"simple"
	},
}
```

<br>

You may find the sample template and requirement details in the [Template Examples](/TemplateExamples) folder.

### generate_plotly.py
The script to ingest data and metadata to generate visualization. This script will call <i>data.py</i> and <i>layout.py</i> to construct <i>data</i> and <i>layout</i> and put into the <i>figure</i> object with <i>generate_plotly_viz()</i>. Note that <i>generate_plotly_viz()</i> can be returned to any script, as long as the <i>figure</i> object is passed to Plotly or Dash rendering object.

### data.py
The script to construct the data object for <i>figure</i> object. It would dynamically construct with different visualization type along with the given metadata.
<br><br>
Currently, it supports:
<ul>
	<li>Bar Chart 
		<ul>
			<li>Simple Bar Chart</li>
			<li>Group Bar Chart</li>
			<li>Stack Bar Chart</li>
		</ul>
	</li>
	<li>Box Plot</li>
	<li>Candlestick Chart</li>
	<li>Scatter Plot
		<ul>
			<li>Simple Scatter Plot</li>
			<li>Scatter Plot with a colour dimension with numeric data</li>
			<li>Scatter Plot with a colour dimension with categorical data</li>
			<li>Bubble Chart</li>
		</ul></li>
	<li>Line Chart
		<ul>
			<li>Simple Line Chart</li>
			<li>Multilines Line Chart</li>
			<li>Line Chart for Linear Regression (Coming soon...)</li>
		</ul></li>
	<li>Histogram
		<ul>
			<li>Simple Histogram</li>
			<li>Normalized Histogram</li>
			<li>Histogram with more than 1 categorical value</li>
			<li>Histogram with aggregated values other than count</li>
		</ul></li>
	<li>Heatmap</li>
	<li>Pie/Donut Chart</li>
	<li>Funnel Chart
		<ul>
			<li>Simple Funnel Chart</li>
			<li>Stacked Funnel Chart</li>
			<li>Simple Funnel Area Chart</li>
		</ul></li>
</ul>

<br><br>
Among the chart type examples in the [Plotly Example folder](../PlotlyExample), here are the list that will not support:
<ul>
	<li>Choropleth Graph</li>
	<li>Treemap</li>
	<li>Sunburst Chart</li>
	<li>Dendrograms</li>
</ul> 
<br><br>
For each visualization type, it would have its <i>generate_(viz_type).py</i> to utilize the functions to generate the data object.
<br><br>
<b>Here are the list of the framework do differently with Plotly:</b>
<ul>
	<li>Bar Chart: hoverinfo is set to <b>none</b>, you have stated <i>all</i> or other value for hovering</li>
	<li>Candlestick Chart: the framework turn off the rangeslider.</li>
</ul>

#### generate_bar.py
The module to generate data object for Bar Chart. You may create a simple, group, or stack bar chart.

#### generate_boxplot.py
The module to generate data object for Box Plot.

#### generate_candlestick.py
The module to generate data object for Candlestick Chart.

#### generate_funnel.py
The module to generate data object for Funnel Chart or Funnel Area Chart. You may create a simple or stack funnel chart, or simple funnel area chart.

#### generate_heatmap.py
The module to generate data object for Heatmap.

#### generate_histogram.py
The module to generate data object for Histogram.

#### generate_line.py
The module to generate data object for Line Chart. You may create a single line chart, multiline chart or linear regression chart (Coming soon...).

#### generate_pie.py
The module to generate data object for Pie Chart or Donut Chart.

### layout.py
The script to construct the layout object for <i>figure</i> object with the given metadata. If no metadata is given, the layout object is generated with the default setting (The layout setting suggested by the author).
<br><br>
You may add a column(s) of:
<ul>
	<li>xaxis</li>
	<li>yaxis</li>
	<li>legend</li>
</ul>

<br>
in <b>metadata</b> to customize the layout setting. And example is:

```
{
	"df_directory":"Data/salary.csv", 
	"viz_type":"Bar", 
	"viz_name":"Salary by Name",
	"metadata":{
		"x":"name", 
		"y":"salary", 
		"viz_subtype":"simple",
		"xaxis":{
			"tickmode":"linear",
			"tickangle":-45
		},
		"yaxis":{
			"tickmode":"linear",
			"tickangle":-45
		}
	},
}
```
<br>
You may not include those setting in the template, Plotly would use the default setting.
<br><br>
For all details of the layout setting, verify the columns details in the <a href=https://github.com/jacquessham/DashExamples/tree/master/PlotlyExample>Plotly Example</a> folder for more details. 