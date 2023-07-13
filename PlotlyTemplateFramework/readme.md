# Plotly Template Framework
The goal of this subsection is to provide a framework to easily plot a visualization via Plotly with low code and avoid excessively copy-and-paste code from previously written Plotly script. The scripts are written in Python.

## How to use it?
You may pass all the arguements and metadata to <i>generate_plotly_viz()</i> in <i>generate_plotly.py</i> and return to your Plotly or Dash rendering object in your scripts. Alternatively, you may fill out the arguement and metadata in <i>arguements.json</i> and execute <i>call_plotly.py</i> to declare the rendering object in this driver script.
<br><br>
<b>The scripts always expect the data frame in Pandas DataFrame!!!</b>

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
		"viz_subtype":""
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
		</ul>
	</li>
	<li>Box Plot</li>
	<li>Coming soon...</li>
</ul>
<br><br>
For each visualization type, it would have its <i>generate_(viz_type).py</i> to utilize the functions to generate the data object.

#### generate_bar.py
The module to generate data object for Bar Chart.
<br><br>
<b>Currently only support simple 2-D bar chart.</b>

#### generate_boxplot.py
The module to generate data object for Box Plot


### layout.py
The script to construct the layout object for <i>figure</i> object with the given metadata. If no metadata is given, the layout object is generated with the default setting (The layout setting suggested by the author).