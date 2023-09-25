# Parallel Coordinates Plot
Parallel Coordinates Plot is a special plot for massive amount of observations to be visualizations different numerical dimensions. In this folder, we will go over how to create a Parallel Coordinates Plot with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>simple_pcate.py</li>
	<li>complex_pcate.py</li>
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
	<li><i>grades.csv</i></li>
</ul>

## Syntax
### Data
Data consists of two parts: <i>line</i> and <i>dimensions</i>. <i>line</i> is the setup of line colours and related metadata and whereas <i>dimensions</i> stores the values and attribute related metadata in a list of dictionaries. <b>Parallel Coordinates Plot parameters structure is very different different with standard visualization types. No x or y columns are accepted, but alternative arguements!</b>
<br><br>
go.Parcoords has the following parameters:
<ul>
	<li>line - dictionary of the setting of the lines in the plot
		<ul>
			<li>color: Accept numbers as label in order to determine what colour to be plotted. IDs or primary keys are good columns to be used</li>
			<li>colorscale: An array of normalized value (0-1.0) mapped to colour, or Plotly reserved words of colorscale</li>
			<li>showscale: True or False to show colour scale as a legend</li>
			<li>cmin: Upper bound of the colour domain, setting the accepted range in the <i>color</i>column in this dictionary</li>
			<li>cmax: Lower bound of the colour domain, setting the accepted range in the <i>color</i>column in this dictionary</li>
		</ul></li>
	<li>dimensions - array of attribute, each array may consist of:
		<ul>
			<li>range: The range of this axis</li>
			<li>constraintrange (Optional): select an range within this attribute to be shown on the plot, none if not specify</li>
			<li>label: Attribute value, in string</li>
			<li>values: Value of the data points</li>
			<li>visible: Determine whether this trace is visible. Accept <i>True</i>, <i>False</i>, and <i>'legendonly'</i>(Trace would not be drawn but appear as a legend item)</li>
			<li>tickvals: To set a interval of the column <i>values</i></li>
			<li>ticktext: To display the text of the column <i>tickvals</i> alternatively to the original text in the column <i>values</i></li>
		</ul></li>
	<li>unselected - dictionary of setting of the lines are not selected by user or range outside of <i>constraintrange</i>
		<ul>
			<li>color: The colour of the unselected lines</li>
			<li>Opacity: opacity of the unselected lines, accept values between 0 and 1</li>
		</ul></li>
</ul>

## Example - Parallel Coordinates Plot
<img src=simple_parcoords.png>


<img src=simple_parcoords_constrain.png>
<br>
This is the example of a parallel coordinates plot where constraint range is applied between 70 and 100.

<img src=complex_parcoords.png>
<br>

```
# Read data
df = pd.read_csv('../Data/grades.csv')
students = df['name'].unique()
num_student = len(students)

# Prepare colorscale for each line
colours = ['gold','green','red','lightblue','pink']
nums = [num*1.0/(num_student-1) for num in range(0,num_student-1)] + [1.0]

colourscale_metadata = [[num, colour] 
		for num, colour in zip(nums , colours)]

# Prepare labels
labels = df.columns.tolist()[2:]


# Prepare the setup of the visualization
fig = go.Figure(data=go.Parcoords(
		line={
			'color': df['student_id'],
			'colorscale': colourscale_metadata,
			'showscale': True
		},
		dimensions=[
			{'range':[70,100],
			  'constraintrange':[90,101],
			  'label': labels[0],
			  'values': df[labels[0]]
			},
			{'range':[70,100],
			  'constraintrange':[70,101],
			  'label': labels[1],
			  'values': df[labels[1]],
			  'tickvals':[80, 90, 100],
			  'ticktext':['Fair','Great','Excellent']
			},
			{'range':[70,100],
			  'label': labels[2],
			  'values': df[labels[2]]
			},
			{'range':[70,100],
			  'label': labels[3],
			  'values': df[labels[3]],
			  'tickvals':[70, 80, 90, 100],
			  'ticktext':['C','B','A','A+']
			}
		]
	))

# Layout
fig.update_layout(
    plot_bgcolor = 'white',
    paper_bgcolor = 'white'
)
```

## Reference
Plotly Documentation <a href="https://plotly.com/python/parallel-coordinates-plot/">Parallel Coordinates Plot</a>