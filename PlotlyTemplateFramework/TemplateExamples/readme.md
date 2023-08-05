# Template Examples
This folder contains the sample template for <i>arguements.json</i>. <b>Be sure to change the file name back to <i>arguements.json</i> after copying from this folder. <i>generate_plotly</i> only takes this filename!</b>

## Bar Chart
Here is the list of template for the subtype of bar chart.

<ul>
	<li><i>simplebar_arguements.json</i>: For simple bar chart</li>
	<li><i>complexbar_arguements.json</i>: For group or stack bar chart</li>
</ul>

Note: <b>The framework turn off hovering by default</b>, which is different from Plotly. You need to turn back on by including this column in <i>metadata</i>.

### simplebar_arguements.json
This template is for simple bar chart, and here are the required or optional columns:

```
{
	"df_directory": (Required) str,
	"viz_type": (Required) "bar",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name, 
		"y": (Required) str: y-axis column name, 
		"viz_subtype": (Required)"simple",
		"bar_colour|bar_color": (Optional) str,
		"width" : (Optional) float: Between 0 and 1,
		"textposition": (Optional) str: "auto|inside|outside|...or more",
		"textfont" (Optional) dict: {},
		"hoverinfo" (Optional) str: "none (Default)|auto|percent|lable|label+percent|..."
	}
}

```

### complexbar_arguements.json
This template is for group or stack bar chart, and here are the required or optional columns:

```
{
	"df_directory": (Required) str,
	"viz_type": (Required) "bar",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name, 
		"y": (Required) y-axis column name, 
		"cate_col": (Required) ,
		"viz_subtype": (Required) "group|stack",
		"bar_colour|bar_color": (Optional) list,
		"width" : (Optional) float: Between 0 and 1,
		"textposition": (Optional) str: "auto|inside|outside|...or more",
		"textfont" (Optional) dict: {},
		"hoverinfo" (Optional) str: "none (Default)|auto|percent|lable|label+percent|..."
	}
}
```

## Box Plot
You may find <i>boxplot_arguements.json</i> for the sample template and here are the required or optional columns:

```
{
	"df_directory": (Required) str,
	"viz_type": (Required)"boxplot|box_plot",
	"viz_name": (Required) str,
	"metadata":{
		"x|category_col|cate_col": (Required) x-axis/category column name, 
		"y": (Required) y-axis column name,
		"bar_colour|bar_color": (Optional) list,
		"boxmean": (Optional) "True|False",
		"textfont" (Optional) dict
	}
}
```

## Candlestick Chart
You may find <i>candlestick_arguements.json</i> for the sample template and here are the required or optional columns:

```
{
	"df_directory":(Required) str,
	"viz_type": (Required) "candlestick",
	"viz_name":(Required) str,
	"metadata":{
		"x": (Required) str, 
		"open": (Required) str,
		"high": (Required) str,
		"low": (Required) str,
		"close": (Required) str,
		"rangeslider": (Optional) "True|False"
	}
}
```
<br>
Note: 
<ul>
	<li><b>By default, the framework turn off the rangeslider. Set it to True to turn back on.</b></li>
	<li>In terms of bar colour, it is always green for increase and red for decrease. The framework does not allow to change this colour pattern since there is no alternative in normal use cases.</li>
</ul>

## Scatter Plot
Here is the list of template for the subtype of scatterplot.

<ul>
	<li><i>simplescatter_arguements.json</i>: For simple scatter plot</li>
	<li><i>numcolour_scatter_arguements.json</i>: For scatter plot with a colour dimension showing numeric value</li>
	<li><i></i>: Coming soon...</li>
</ul>

Note: <b>The framework turn off hovering by default</b>, which is different from Plotly. You need to turn back on by including this column in <i>metadata</i>.

### simplescatter_arguements.json
This template is for simple scatter plot, and here are the required or optional columns:


```
{
	"df_directory": (Required) str,
	"viz_type": (Required) "scatter|scatterplot|scatter_plot",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name, 
		"y": (Required) str: y-axis column name, 
		"viz_subtype" str: (Required)"simple",
		"hoverinfo" (Optional) str: "none (Default)|auto|percent|lable|label+percent|..."
	}
}
```

### numcolour_scatter_arguements.json
This template is for scatter plot with a colour dimension with numeric/integer type column, and here are the required or optional columns:

```
{
	"df_directory": (Required) str,
	"viz_type": (Required) "scatter|scatterplot|scatter_plot",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name, 
		"y": (Required) str: y-axis column name, 
		"z": (Required) str: colour dimension column name (Must be numeric value),
		"showscale" (Optional) str/boolean: true|false|"true"|"false"|"True"|"False",
		"colour_scale" (Optional) str : Any colour scale available in Plotly,
		"viz_subtype" (Required) str: "num_color",
		"hoverinfo" (Optional) str: "none (Default)|auto|percent|lable|label+percent|..."
	}
}
```

Note:
<ul>
	<li><b>This arguement template only works for numeric column for colour dimension</b></li>
	<li><b>The framework turn on colour scale by default</b>, you have to turn off in the metadata</li>
	<li>If no colour scale provided, colour scale is picked by Plotly backend</li>
</ul>

### catecolour_scatter_arguement.json
This template is for scatter plot with a colour dimension with categorical type column (Non-numeric column), and here are the required or optional columns:

```
{
	"df_directory": (Required) str,
	"viz_type": (Required) "scatter|scatterplot|scatter_plot",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name, 
		"y": (Required) str: y-axis column name, 
		"z": (Required) str: colour dimension column name (Must be numeric value),
		"viz_subtype" (Required) str:"cate_color",
		"showlegend" (Optional) str/boolean: true|false|"true"|"false"|"True"|"False",
		"addition_colourscale" (Optional, only apply when there are ~140+ labels):{
			"low" (Required) str:"rgb(0-255, 0-255, 0-255)",
			"high" (Required) str: "rgb(0-255, 0-255, 0-255)"
		}
	}
}
```

Note: 
<ul>
	<li><b>Currently the framework only pick the default colour scale in Plotly colour scheme!</b> Optional to customize the colour scale will be released in the future release</li>
	<li>There are 10 colours in the Plotly default colour scale, when are there are more than 10 but less than ~140, <b>the framework would randomly pick the colours in available in <i>css_colours.py</i></b></li>
	<li><i>addition_colourscale</i> only be applied when there are ~140+ labels in the colour diemnsion column. When the number of labels is less than that, the whole dictionary would be ignored</li>
</ul>

### bubblechart_arguements.json
Coming soon...

## Line Chart
Here is the list of template for the subtype of line chart.

<ul>
	<li><i>simplescatter_arguements.json</i>: For simple scatter plot</li>
	<li><i></i>: Coming soon...</li>
</ul>

Note: <b>The framework turn off hovering by default</b>, which is different from Plotly. You need to turn back on by including this column in <i>metadata</i>.

### simplesline_arguements.json
This template is for simple line chart, and here are the required or optional columns:

```
{
	"df_directory": (Required) str,
	"viz_type": (Required) "line",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name, 
		"y": (Required) str: y-axis column name, 
		"viz_subtype": (Required)"simple",
		"datapoints": (Optional): "t|true|True|f|false|False(Default)",
		"hoverinfo" (Optional) str: "none (Default)|auto|percent|lable|label+percent|..."
	}
}

```

Note: <b>The framework does not plot data point by default</b>

### Multilines_arguements.json
This template is for multiple lines chart, while lines are partitioned by categorical value in a data frame. Here are the required or optional columns:

```
{
	"df_directory": (Required) str,
	"viz_type": (Required) "line",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name, 
		"y": (Required) str: y-axis column name, 
		"viz_subtype": (Required) "mutlilines|mutliple_lines|mutli_lines",
		"datapoints": (Optional): "t|true|True|f|false|False(Default)",
		"cate_col": (Required) categorical column name,
		"hoverinfo" (Optional) str: "none (Default)|auto|percent|lable|label+percent|...",
		"line_colour": (Optional) {
			"category 1": RGB values/Colour Keyword,
			"category 1": RGB values/Colour Keyword,
			...
			"category len(Unique values available in cate_col)": RGB values/Colour Keyword
		}
	}
}
```

Note: 
<ul>
	<li>The framework automatically use the categorical value as the name of each line.</li>
	<li>If <i>line_colour</i> is presented, the number of colour mapping must match the number of unique values available in <i>cate_col</i></li>
</ul>


### lr_arguements.json
This template is for line chart along with scatter points, ie, linear regression use cases. Here are the required or optional columns:

```
Coming soon...
```
