# Sunburst Chart
Sunburst Chart is similar to a treemap but visualize on a pie/donut chart. In this folder, we will go over how to create a sunburst chart with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>simplesunburst.py</li>
	<li>simplesunburst_colourscale.py</li>
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
### Data
Data is a list to store <i>go.Sunburst()</i>. <b>Treemap parameters structure is very different different with standard visualization types. No x or y columns are accepted, but alternative arguements!</b>
<br><br>
go.Sunburst() has the following parameters:
<ul>
	<li>values: The numeric value of the attribute</li>
	<li>labels: A categorical attribute</li>
	<li>parents: The parent categorical value of labels</li>
	<li>marker_colors: The colour of the area of each attribute</li>
	<li>textinfo: Determines which trace information appear on the graph, it can be:
		<ul>
			<li>text</li>
			<li>value</li>
			<li>current path</li>
			<li>percent root</li>
			<li>percent entry</li>
			<li>percent parent</li>
			<li>Or any combination of them, simply put a <b>+</b> sign between the values above without white space in between</li>
		</ul>
	</li>
	<li>hoverinfo: What information to be displayed when user hover over the coloured area, all the options are:
		<ul>
			<li>percent</li>
			<li>label+percent</li>
			<li>label</li>
			<li>name</li>
		</ul></li>
</ul>
<br>

## Example - Simple Sunburst Chart
<img src=simple_sunburst.png>

```
df = pd.read_csv('../Data/salary.csv')

values = df['salary'].tolist() + [600000,350000]
labels = df['name'].tolist() + df['school'].unique().tolist()
parents = df['school'].tolist() + ['','']

fig = go.Figure(go.Sunburst(
    labels = labels,
    values = values,
    parents = parents,
    textinfo = 'label+value'))

```

<br>
Note: We add two data points in order to demostrate the uniqueness of sunburst chart compared to a pie chart
<br><br>
Here is the visualization if <i>marker_color</i> is filled with <i>agsunset</i>:
<img src=simple_sunburst_agsunset.png>

## Reference
Plotly Documentation <a href="https://plotly.com/python/sunburst-charts/">Sunburst Charts</a>