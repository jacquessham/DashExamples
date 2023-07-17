# Bar Charts
Bar charts are charts use rectangles represent data values for each attribute. In this folder, we will go over how to create bar charts with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>Simplebar.py</li>
	<li>Groupbar.py</li>
	<li>Stackbar.py</li>
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
	<li><i>expense_everybody.csv</i></li>
</ul>

## Syntax
### Data
Data is a list of <i>go.Bar()</i>, each <i>go.Bar()</i> represents a category of bars.
<br><br> 
If the data list has only 1 <i>go.Bar()</i>, it is a simple bar chart: Each attribute has only 1 bar.
<br><br>
If it is grouped, each attribute has a group of bars displayed (All bars belong to each attribute stick together) ordered by the order in the data list.
<br><br>
If it is stacked, each attribute has one bar, each category value would be stacked on top of other categories order by the the order in the data list.
<br><br>
go.Bar() has the following parameters:
<ul>
	<li>x: Attribute on x-axis</li>
	<li>y: Value on y-axis</li>
	<li>name: Category, which will be displayed on legend</li>
	<li>text: The text label will displayed on the bars</li>
	<li>textposition: Text label position
		<ul>
			<li>auto: On the top of the bar</li>
			<li>inside: On the top of the bar</li>
			<li>outside: Outside of the bar</li>
		</ul>
	</li>
	<li>textfont (Dictionary): Text label setting</li>
	<li>marker_color: Bar colour (Take colour spelliing in string or RGB in string)</li>
	<li>width: Width of the bar in pixel</li>
	<li>hoverinfo: What information to be displayed when user hover over the bar, all the options are:
		<ul>
			<li>all (Default)</li>
			<li>none/skip (Both keywords in string means no hovering)</li>
			<li>percent</li>
			<li>label+percent</li>
			<li>label</li>
			<li>name</li>
			<li>text</li>
		</ul></li>
	<li>hovertemplate: The information to be displayed when user hover over the bar, defined in HTML format</li>
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
	<li>xaxis (Dictionary): X-axis setting
		<ul>
			<li>tickmode: Setting of ticks</li>
			<li>tickangle: Degree the tick rotate (-: Anticlockwise, +: Clockwise)</li>
			<li>categoryorder: Sort the order of attributes on X-axis, either ascending or descending
				<ul>
					<li>category ascending: Sort attribute (attribute in name in Data) in ascending orders</li>
					<li>category descending: Sort attribute (attribute in name in Data) in descending orders</li>
					<li>total ascending: Sort value in ascending orders</li>
					<li>total descending: Sort value in descending orders</li>
					<li>min ascending/min descending: Sort by minimum value</li>
					<li>max ascending/max descending: Sort by maximum value</li>
					<li>sum ascending/sum descending: Sort by summation value</li>
					<li>mean ascending/mean descending: Sort by average value</li>
					<li>median ascending/median descending: Sort by median value</li>
					<li>array: Follow the sorting order defined in <b>categoryarray</b></li>
				</ul>
			</li>
			<li>categoryarray: Define the sorting order when <b>categoryorder is array</b></li>
		</ul></li>
	<li>yaxis (Dictionary): y-axis setting
		<ul>
			<li>tickmode: Setting of ticks</li>
			<li>tickangle: Degree the tick rotate (-: Anticlockwise, +: Clockwise)</li>
		</ul></li>
	<li>barmode: How the bars are grouped (See below for detail)</li>
	<li>uniformtext (Dictionary): Allow bar chart becomes Marimekko Chart by forcing bars to stick together
		<ul>
			<li>mode: Put "hide" to becomes Marimekko chart</li>
			<li>minsize: Minimum size of bars</li>
		</ul>
	</li>
</ul>
<br><br>

Bar Chart Exclusive parameters:
<ul>
	<li>barmode: How the bars are grouped
		<ul>
			<li>grouped: Bars stick together if they belong to the same attribute</li>
			<li>stacked: Bars stack on top of each other if they belong to the same attribute</li>
			<li>relative: Stacked bars, but negative values stack below 0</li>
		</ul></li>
	<li>marker_color: Bar colour</li>
</ul>

## Examples
### Example 1 - Simple Bar Chart
<img src=bar.png>

```
# Data
data = []
data.append(go.Bar(x=df['name'], y=df['salary'],
	               text=df['salary'], textposition='auto',
	               textfont=dict(color='white')))
# Layout
layout = {'title':{'text':'Everybody\'s Salary', 'x':0.5}}

```

### Example 2 - Grouped Bar Chart
<img src=groupbar.png>

```
data =[]
for cate, colour, width in zip(df['expense_category'].unique(),colours, widths):
	df_temp = df[df['expense_category']==cate]
	data.append(go.Bar(name=cate, 
	               x=df_temp['name'], y=df_temp['amount'],
	               marker_color=colour,
	               width=[width]*len(df_temp['name']),
	               text=df_temp['amount'], textposition='auto',
	               textfont={'color':'white'}))

fig_title = 'Everybody\'s Expense'
layout = dict(title={'text':fig_title, 'x':0.5},
              barmode='group', 
              xaxis=dict(tickmode='linear',tickangle=-45))
```

<br>
Each bar is a stored as an element in data list, and set barmode to <b>group</b>.


### Example 3 - Stacked Bar Chart
<img src=stackbar.png>

```
# Prepare data
data =[]
for cate in df['expense_category'].unique():
	df_temp = df[df['expense_category']==cate]
	data.append(go.Bar(name=cate, 
	               x=df_temp['name'], y=df_temp['amount'],
	               text=df_temp['amount'], textposition='auto',
	               textfont=dict(color='white')))

fig_title = 'Everybody\'s Expense'
layout = dict(title={'text':fig_title, 'x':0.5},
              barmode='stack', 
              xaxis=dict(tickmode='linear',categoryorder='total descending'))

```

<br>
Each bar is a stored as an element in data list, and set barmode to <b>stack</b>.

