# Template Examples
This folder contains the sample template for <i>arguements.json</i>. <b>Be sure to change the file name back to <i>arguements.json</i> after copying from this folder. <i>generate_plotly</i> only takes this filename!</b>

## Bar Chart
Here is the list of template for the subtype of bar chart.

<ul>
	<li><i>simplebar_arguements.json</i>: For simple bar chart</li>
	<li><i>complexbar_arguements.json</i>: For group or stack bar chart</li>
</ul>

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
		"textfont" (Optional) dict:
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
		"textfont" (Optional) dict:
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
<b>By default, the framework turn off the rangeslider. Set it to True to turn back on.</b>
