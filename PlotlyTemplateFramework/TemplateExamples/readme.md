# Template Examples
This folder contains the sample template for <i>arguements.json</i>.

## Bar Chart
Here is the list of template for the subtype of bar chart.

<ul>
	<li>simplebar_arguements.json</li>
	<li></li>
	<li></li>
</ul>

### simplebar_arguements.json
This template is for simple bar chart, and here are the required or optional columns:

```
{
	"df_directory": (Required),
	"viz_type": (Required) "bar",
	"viz_name": (Required)  # Title of the visualization,
	"metadata":{
		"x": (Required) x-axis column name, 
		"y": (Required) y-axis column name, 
		"viz_subtype": (Required)"simple|gropu|stack",
		"bar_colour|bar_color": (Optional),
		"textposition": (Optional),
		"textfont" (Optional):
	}
}

```


## Box Plot
You may find <i>boxplot_arguements.json</i> for the sample template and here are the required or optional columns:

```
{
	"df_directory": (Required),
	"viz_type": (Required)"boxplot|box_plot",
	"viz_name": (Required),
	"metadata":{
		"x|category_col|cate_col": (Required) x-axis/category column name, 
		"y": (Required) y-axis column name,
		"bar_colour|bar_color": (Optional),
		"boxmean": (Optional) "True|False",
		"textfont" (Optional)
	}
}
```
