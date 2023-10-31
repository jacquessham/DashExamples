# Sankey Chart
Sankey chart is a flow diagram which is able to display mutliple dimension from one state to another states. 

## Files
The following scripts are used in this chapter:
<ul>
	<li>plotlyexample_sankey.py</li>
	<li>simple_sankey.py</li>
</ul>

## Pacakges Needed
This chapter requires the following packages for the scripts used:
<ul>
	<li>Pandas</li>
	<li>Plotly</li>
</ul>


## Syntax
### Data
Data is a list to store <i>go.Sankey()</i>. <i>go.Sankey()</i> consists of two parts: <b>node</b> and <b>link</b>. <b>Sunburst parameters structure is very different different with standard visualization types. No x or y columns are accepted, but alternative arguements!</b>
<br><br>
go.Sankey() has the following parameters:
<ul>
	<li>valueformat: Value format used in the hoverinfo</li>
	<li>valuesuffix: Add suffix after the value displayed in the hoverinfo</li>
	<li>node: Use to display attribute
		<ul>
			<li>pad: The size of node pad</li>
			<li>thickness: The size of thickness</li>
			<li>label: What to display in the node</li>
			<li>color: Colour filled in the node</li>
			<li>line: Setting of the node line
				<ul>
					<li>color</li>
					<li>line</li>
				</ul>
			</li></ul>
	</li>
	<li>link: Use to display the fact between two attributes
		<ul>
			<li>source: Start of the link, use the indices of label in node</li>
			<li>target: End of the link, use the indices of label in node</li>
			<li>value: Value of the link</li>
			<li>color: Colour filled in the link</li>
		</ul>
	</li>
</ul>
<br>

## Plotly Example
<img src=plotly_example.png>

```
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"],
      color = ["blue","red","purple","yellow","green","orange"]
    ),
    link = dict(
      source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [2, 3, 3, 4, 4, 5],
      value = [8, 4, 2, 8, 4, 2],
      color = ["lightblue","pink","lightblue","mediumpurple","lightyellow","lightyellow"]
  ))])

fig.update_layout(title_text="Hello World!")
```

## Example - Hours of Video Games Played on Console
<img src=simple_sankey.png>

<br><br>
See [simple_sankey.py](/simple_sankey.py) for code example.


## Reference
Plotly Documentation <a href="https://plotly.com/python/sankey-diagram/">Sankey Chart</a>
