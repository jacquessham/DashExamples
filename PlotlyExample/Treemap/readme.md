# Treemap
Treemap. In this folder, we will go over how to create bar charts with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>PlotlyExample_treemap.py</li>
	<li>SalaryExample_treemap.py</li>
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
Data is a list to store <i>go.Treemap()</i>. <b>Treemap parameters structure is very different different with standard visualization types. No x or y columns are accepted, but alternative arguements!</b>
<br><br>
go.heatmap() has the following parameters:
<ul>
	<li>values: The numeric value of the attribute</li>
	<li>labels: A categorical attribute</li>
	<li>parents: The parent categorical value of labels</li>
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
	<li>marker_colors: The colour of the area of each attribute</li>
	<li>hoverinfo: What information to be displayed when user hover over the coloured area, all the options are:
		<ul>
			<li>percent</li>
			<li>label+percent</li>
			<li>label</li>
			<li>name</li>
		</ul></li>
</ul>
<br>


## Tips
<ul>
	<li>x, y, z can not be pass as parameters</li>
	<li>layout is not working in go.Treemap() as expected</li>
	<li>All attribute requires parent value and simply passing a Pandas dataframe column would not work, you may add the root value at the end of the array of values and an empty value at the end of the array of parents</li>
</ul>



## Examples
### Example 1 - Treemap from Plotly
<img src=plotly_treemap.png>

```
values = ["11", "12", "13", "14", "15", "20", "30"]
labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "A1", "A2", "A3", "A4", "", "B1"]
marker_colours = ["pink", "royalblue", "lightgray", "purple", 
                  "lightgray", "lightblue", "lightgreen"]

fig = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    marker_colors = marker_colours,
    textinfo = 'label+value+percent parent+percent entry+percent root',
    marker_colorscale = 'Blues'))
```
### Example 2 - Treemap with Salary Dataset
<img src=salary_treemap.png>

```
df = pd.read_csv('../Data/salary.csv')

values = df['salary'].tolist() + [0,0]
labels = df['name'].tolist() + df['school'].unique().tolist()
parents = df['school'].tolist() + ['','']

data = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    textinfo = 'label+value+percent parent+percent entry+percent root',
    marker_colorscale = 'Blues'))
```