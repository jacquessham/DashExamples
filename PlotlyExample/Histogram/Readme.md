# Histogram
Histogram are charts use rectangles represent frequency of the range of a continuous attribute. In this folder, we will go over how to create histogram with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>SimpleHistogram.py</li>
	<li>NormalizedHistogram.py</li>
	<li>OverlaidHistogram.py</li>
	<li>StackedHistogram.py</li>
	<li>CumulativeHistogram.py</li>
</ul>

## Pacakges Needed
This chapter requires the following packages for the scripts used:
<ul>
	<li>Plotly</li>
	<li>Pandas</li>
</ul>


## Syntax
### Data
Data is a list of <i>go.Histogram()</i>, each <i>go.Histogram()</i> represents a set of histogram.
<br><br>
go.Histogram() has the following parameters:
<ul>
	<li>x: Value</li>
	<li>y: Value in a horizontal histogram</li>
	<li>histnorm: Normalized Histogram
		<ul>
			<li>probability: Probability of an event happen of each bin</li>
			<li>percent: Percentage of the occurrence with respect to total number</li>
			<li>density: Number of occurrence in a bin divided by the size of the bin interval</li>
			<li>probability density: The Probility of an event happen of each density bin</li>
		</ul>
	</li>
	<li>xbins: Setting of each bin
		<ul>
			<li>size: Define the interval size of each bin, number</li>
		</ul>
	</li>
	<li>ybins: Same as xbins but for horizontal bars</li>
	<li>cumulative_enabled: Enable Cumulative Histogram, True/False</li>
	<li>opacity: Opacity, from 0-1</li>
	<li>marker_color: Bar colour (Take colour spelliing in string or RGB in string)</li>
	<li>hoverinfo: What information to be displayed when user hover over the bar, all the options are:
		<ul>
			<li>percent</li>
			<li>label+percent</li>
			<li>label</li>
			<li>name</li>
		</ul></li>
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
	<li>barmode: How the sets of histogram are displayed
		<ul>
			<li>stack: Histograms are drawn on top of another</li>
			<li>overlay: Have different data set sharing the same bins</li>
		</ul>
	</li>
	<li>bargap: Gap between bars, in pixel</li>
	<li>histfunc: Specifies the binning function (count: Count occurrences, sum: Sum the values, avg: Average the values, min/max: Display minimum or maximum value within the bin)</li>
	<li>histnorm: Type of Normalization used for histogram, None by default (probability: Bar display in %, density: Bar is calculated by occurrences divided by size, probability density: Bar is calculated by occurrences divided by size, all bin sum to 1)</li>
</ul>
<br><br>

Histogram Exclusive parameters:
<ul>
	<li>cumulative_enabled: Enable Cumulative Histogram, True/False</li>
	<li>marker_color: Bar colour (Take colour spelliing in string or RGB in string)</li>
	<li>barmode: How the sets of histogram are displayed
		<ul>
			<li>stack: Histograms are drawn on top of another</li>
			<li>overlay: Have different data set sharing the same bins</li>
		</ul>
	</li>
	<li>bargap: Gap between bars, in pixel</li>
	<li>histfunc: Specifies the binning function (count: Count occurrences, sum: Sum the values, avg: Average the values, min/max: Display minimum or maximum value within the bin)</li>
	<li>histnorm: Type of Normalization used for histogram, None by default (probability: Bar display in %, density: Bar is calculated by occurrences divided by size, probability density: Bar is calculated by occurrences divided by size, all bin sum to 1)</li>
</ul>

## Examples
### Example 1 - Simple Histogram
<img src=simple_histogram.png>

```
# Data
data = []
data.append(go.Histogram(x=df['salary']))
# Layout
layout = {'title':{'text':'Histogram of Salary among Friends', 'x':0.5}}

```
### Example 2 - Normalized Histogram
<img src=normalized_histogram.png>

```
# Data
data = []
data.append(go.Histogram(x=x, histnorm='probability'))
# Layout
layout = {'title':{'text':'Distribution of 500 Random Numbers', 'x':0.5}}
```

### Example 3 - Overlaid Histogram
<img src=overlaid_histogram.png>

```
data = []
for group in df['group'].unique():
    df_temp = df[df['group']==group]
    data.append(go.Histogram(x=df_temp['salary'],name=group))
# Layout
layout = {'title':{'text':'Everybody\'s Salary', 'x':0.5},
          'barmode':'overlay'}
```

### Example 4 - Stacked Histogram
<img src=stacked_histogram.png>

```
data = []
for group in df['group'].unique():
    df_temp = df[df['group']==group]
    data.append(go.Histogram(x=df_temp['salary'],name=group))
# Layout
layout = {'title':{'text':'Everybody\'s Salary', 'x':0.5},
          'barmode':'stack'}
```

### Example 5 - Cumulative Histogram
<img src=cumulative_histogram.png>

```
# Data
data = []
data.append(go.Histogram(x=df['salary'], cumulative_enabled=True))
# Layout
layout = {'title':{'text':'Everybody\'s Salary', 'x':0.5}}
```

### Example 6 - Aggregated Histogram
<img src=aggregated_histogram.png>

```
# Data
data = []
data.append(go.Histogram(x=df['salary'], y=df['salary'],  histfunc='sum'))
# Layout
layout = {'title':{'text':'Everybody\'s Salary (Summation by Group)', 'x':0.5}}
```

Note: <b><i>histfunc</i> aggreagates from y-axis. A numeric column must provided for y-axis arguement, or else, Plotly treats it as a simple histogram</b>

## Reference
Plotly Documentation <a href="https://plotly.com/python/histograms/">Histograms</a>
