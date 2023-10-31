# Funnel Chart
Coming soon...


## Files
The following scripts are used in this chapter:
<ul>
	<li></li>
	<li></li>
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
	<li><i>ecom_funnel.csv</i></li>
</ul>

## Syntax
### Data
Data is a list to store either <i>go.Funnel()</i> or <i>go.Funnelarea()</i>. The difference... <b>Please note that x accepts facts or numerics values, while y accepts attribute values or categorical values. Swapping x and y will lead to unexpected behaviour!</b>

#### go.Funnel()
go.Funnel() has the following parameters:
<ul>
	<li>x: The numeric value of the attribute</li>
	<li>y: A categorical value</li>
	<li>name: Category, which will be used for identifying the stacked funnel</li>
	<li>marker: Setting for the funnel bar
		<ul>
			<li>color: The colour of the area of each attribute</li>
			<li>line: The setting for the line
				<ul>
					<li>width</li>
					<li>line</li>
				</ul></li>
			<li>connector: The setting for the connector between each funnel bar
				<ul>
					<li>line
						<ul>
							<li>color</li>
							<li>dash</li>
						</ul>
					</li>
				</ul></li>
		</ul></li>
	<li>textposition: Text position for y, it can be:
		<ul>
			<li>inside</li>
			<li>outside</li>
			<li>auto</li>
			<li>none</li>
		</ul>
		</li>
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


#### go.Funnelarea()
<b>Note: go.Funnelarea() uses <i>value</i> and <i>text</i>!</b> Instead of <i>x</i> and <i>y</i>
<br><br>
go.Funnelarea() has the following parameters:
<ul>
	<li>value: The numeric value of the attribute</li>
	<li>text: A categorical value</li>
	<li></li>
	<li>marker: Setting for the funnel bar
		<ul>
			<li>color: The colour of the area of each attribute</li>
			<li>line: The setting for the line
				<ul>
					<li>width</li>
					<li>line</li>
				</ul></li>
			<li>connector: The setting for the connector between each funnel bar
				<ul>
					<li>line
						<ul>
							<li>color</li>
							<li>dash</li>
						</ul>
					</li>
				</ul></li>
		</ul></li>
	<li>textposition: Text position for y, it can be:
		<ul>
			<li>inside</li>
			<li>outside</li>
			<li>auto</li>
			<li>none</li>
		</ul>
		</li>
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

## Example 1 - Simple Funnel Chart
<img src=simple_funnel.png>

```
fig = go.Figure(go.Funnel(
    y = df['stage'],
    x = df['count'])
)
```

## Example 2 - Stacked Funnel Chart
<img src=stack_funnel.png>

```
data = []
for shop in df['shop'].unique():
	df_temp = df[df['shop']==shop]
	data.append(go.Funnel(
		name = shop,
	    y = df_temp['stage'],
	    x = df_temp['count'])
	)
```

## Example 3 - Simple Funnel Area
Coming soon...

## Reference
Plotly Documentation <a href="https://plotly.com/python/funnel-charts/">Funnel Charts</a>