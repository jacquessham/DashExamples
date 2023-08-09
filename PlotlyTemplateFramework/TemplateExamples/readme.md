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
	<li><i>catecolour_scatter_arguement.json</i>: For scatter plot with a colour dimension showing categorical value</li>
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
		"z": (Required) str: colour dimension column name (Must be categorical value),
		"viz_subtype" (Required) str:"cate_color",
		"showlegend" (Optional) str/boolean: true|false|"true"|"false"|"True"|"False",
		"colour_scheme|colour_choice" (Optional) dict/list: ({
			"unique_value_1":"CSS Colour Keyword/rgb(0-255, 0-255, 0-255)",
			"unique_value_2":"CSS Colour Keyword/rgb(0-255, 0-255, 0-255)",
			"unique_value_3":"CSS Colour Keyword/rgb(0-255, 0-255, 0-255)"
		}|["CSS Colour Keyword/rgb(0-255, 0-255, 0-255)",
			"CSS Colour Keyword/rgb(0-255, 0-255, 0-255)",
			"CSS Colour Keyword/rgb(0-255, 0-255, 0-255)"]),
		"addition_colourscale" (Optional, only apply when there are ~140+ labels):{
			"low" (Required) str:"rgb(0-255, 0-255, 0-255)",
			"high" (Required) str: "rgb(0-255, 0-255, 0-255)"
		}
	}
}
```

Note: 
<ul>
	<li>The framework would pick the default colour scale in Plotly colour scheme if <i>colour_scheme</i> is not provided</li>
	<li><b>If colour_scheme is provided, you must provide the exact number of unique values found in the colour column dimension for mapping!</b></li>
	<li>There are 10 colours in the Plotly default colour scale, when <i>colour_scheme</i> is not provided and there are more than 10 but less than 125 in the colour column, <b>the framework would randomly pick the colours in available in <i>css_colours.py</i></b></li>
	<li>When <i>colour_scheme</i> is not provided and <i>addition_colourscale</i> only be applied when there are 125 labels in the colour diemnsion column. When the number of labels is less than that, the whole dictionary would be ignored</li>
</ul>

### bubblechart_arguements.json
This template is for bubble chart, and here are the required or optional columns:

```
{
	"df_directory": (Required) str,
	"viz_type": (Required) "scatter|scatterplot|scatter_plot|bubblechart|bubble_chart",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name, 
		"y": (Required) str: y-axis column name, 
		"colour" (Required only if size is not provided) str: colour dimension column name (Must be categorical value),
		"size" (Required only if colour is not provided) str: data point size dimension column name (Must be numeric value),
		"viz_subtype" (Required only when viz_type = ""scatter|scatterplot|scatter_plot") str:"bubblechart|bubble_chart",
		"constant_itemsizing" (Optional) str/boolean: true|false|"true"|"false"|"True"|"False"
		"showlegend" (Optional) str/boolean: true|false|"true"|"false"|"True"|"False",
		"colour_scheme|colour_choice" (Optional) dict/list: ({
			"unique_value_1":"CSS Colour Keyword/rgb(0-255, 0-255, 0-255)",
			"unique_value_2":"CSS Colour Keyword/rgb(0-255, 0-255, 0-255)",
			"unique_value_3":"CSS Colour Keyword/rgb(0-255, 0-255, 0-255)"
		}|["CSS Colour Keyword/rgb(0-255, 0-255, 0-255)",
			"CSS Colour Keyword/rgb(0-255, 0-255, 0-255)",
			"CSS Colour Keyword/rgb(0-255, 0-255, 0-255)"]),
		"addition_colourscale" (Optional, only apply when there are ~140+ labels):{
			"low" (Required) str:"rgb(0-255, 0-255, 0-255)",
			"high" (Required) str: "rgb(0-255, 0-255, 0-255)"
		}
	}
}
```

Note: 
<ul>
	<li>The framework allows user to plot either colour or size, or both colour and size for dimensions other than X or Y</li>
	<li><b>Currently Bubble Chart only supports categorical value for colour dimension</b></li>
	<li><b>By default, the legend of size dimension is set to have constant bubble size. If you wish to have variable bubble size in the legend, set false to <i>constant_itemsizing</i>!</b></li>
	<li>The framework would pick the default colour scale in Plotly colour scheme if <i>colour_scheme</i> is not provided</li>
	<li><b>If colour_scheme is provided, you must provide the exact number of unique values found in the colour column dimension for mapping!</b></li>
	<li>There are 10 colours in the Plotly default colour scale, when <i>colour_scheme</i> is not provided and there are more than 10 but less than 125 in the colour column, <b>the framework would randomly pick the colours in available in <i>css_colours.py</i></b></li>
	<li>When <i>colour_scheme</i> is not provided and <i>addition_colourscale</i> only be applied when there are 125 labels in the colour diemnsion column. When the number of labels is less than that, the whole dictionary would be ignored</li>
</ul>

## Line Chart
Here is the list of template for the subtype of line chart.

<ul>
	<li><i>simplesline_arguements.json</i>: For single line line chart</li>
	<li><i>Multilines_arguements.json</i>: For mutliple lines line chart</li>
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

## Histogram
Here is the list of template for the subtype of line chart.

<ul>
	<li><i>simplehistogram_arguements.json</i>: For simple histogram</li>
	<li><i>normalizedhistogram_arguements.json</i>: For normalized histogram </li>
	<li><i>catehistogram.json</i>: Histogram with more than 1 categorical value</li>
	<li><i>aggregatedhistogram_arguements.json</i>: For histogram with aggregated values other than count</li>
</ul>

### simplehistogram_arguements.json
This template is for simple histogram, and here are the required or optional columns:

```
{
	"df_directory": (Required) str,,
	"viz_type": (Required) "histogram",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name,
		"viz_subtype": (Required)"simple",
		"cumulative|cumulative_enable": (Optional): "t|true|True|f|false|False(Default)"
	}
}
```

### normalizedhistogram_arguements.json
This template is for normalized histogram, and here are the required or optional columns:

```
{
	""df_directory": (Required) str,,
	"viz_type": (Required) "histogram",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name,
		"viz_subtype": (Required) "normalized|normalised",
		"histnorm": (Required) "probability|density|probability density",
		"cumulative|cumulative_enable": (Optional): "t|true|True|f|false|False(Default)"
	}
}
```

### catehistogram.json
This template is for normalized histogram, and here are the required or optional columns:

```
{
	""df_directory": (Required) str,,
	"viz_type": (Required) "histogram",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name,
		"cate_col": (Optional) categorical column name,
		"viz_subtype": (Required) "cate_histogram|category_histogram|categorical_histogram",
		"cumulative|cumulative_enable": (Optional): "t|true|True|f|false|False(Default)"
	}
}
```



### aggregatedhistogram_arguements.json
This template is for normalized histogram, and here are the required or optional columns:

```
{
	""df_directory": (Required) str,,
	"viz_type": (Required) "histogram",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) str: x-axis column name,
		"cate_col": (Optional) categorical column name,
		"viz_subtype": (Required) "agg_histogram|aggregated_histogram",
		"cumulative|cumulative_enable": (Optional): "t|true|True|f|false|False(Default)",
		"barmode": (Optional, Required when cumulateive_enable is true) "stack|overlay",
		"histfunc": (Optional) "count(Default)|sum|avg|min|max"
	}
}
```
## Heatmap
You may find <i>simpleheatmap_arguements.json</i> for the sample template and here are the required or optional columns:

```
{
	"df_directory":(Required) str,
	"viz_type": (Required) "heatmap",
	"viz_name":(Required) str,
	"metadata":{
		"x": (Required) str, 
		"y": (Required) str,
		"colour": (Required) str,
		"colourscale": (Optional) str,
		"hoverinfo" (Optional) str: "none (Default)|auto|percent|lable|label+percent|..."
	}
}
```