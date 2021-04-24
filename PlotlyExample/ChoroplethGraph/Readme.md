# Choropleth Graphs
Choropleth graphs are maps with coloured areas to display the values to each geo location. Plotly's Choropleth Graph supports various maps, including the world and the US. In this folder, we will go over how to create chropleth graphs with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>Example_Basic_ChoroplethGraph.py</li>
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
	<li><i>county_avg_rent.csv</i></li>
	<li><i>countyfips.csv</i></li>
</ul>

### countyfips.csv
Plotly has a feature to draw borders based on FIPS (Federal Information Processing Standards) defined by the US government, so Plotly could draw the border automatically if you have connected the data with FIPS. <i>countyfips.csv</i> is the table for all FIPS number for all counties in the US. 

## Syntax
### Approach 1 - figure_factory.create_choropleth()
figure_factory.create_choropleth() is a easy way to create choropleth graphs in the United States, especially only displaying individual state. Different with the go.Figure(), figure_factory.create_choropleth() takes all data parameters and layout parameters.
<br><br>
figure_factory.create_choropleth() has the following parameters:
<ul>
	<li>fips: FIPS (Federal Information Processing Standards) defined by the US government, an attribute to locate the counties in United States</li>
	<li>values: Values</li>
	<li>colorscale: The set of colours to display the value of each area, see <i>plotly.colors.sequential</i> for colour sets</li>
	<li>show_state_data: (Coming Soon...)</li>
	<li>scope: The map used in the visualization</li>
	<li>binning_endpoints: To map the range of values to colorscale</li>
	<li>county_outline (Dictionary): Define the lines on county borders
		<ul>
			<li>color: Color of county borders, RGB or Hex in string</li>
			<li>width: The width of borderline in px, integer</li>
		</ul></li>
	<li>state_outline (Dictionary): Define the lines on state borders<ul>
			<li>color: Color of county borders, RGB or Hex in string</li>
			<li>width: The width of borderline in px, integer</li>
		</ul></li>
</ul>
<br>


Choropleth Graph Exclusive parameters:
<ul>
	<li>fips: FIPS (Federal Information Processing Standards) defined by the US government, an attribute to locate the counties in United States</li>
	<li>show_state_data: (Coming Soon...)</li>
	<li>scope: The map used in the visualization</li>
	<li>binning_endpoints: To map the range of values to colorscale</li>
	<li>county_outline (Dictionary): Define the lines on county borders
		<ul>
			<li>color: Color of county borders, RGB or Hex in string</li>
			<li>width: The width of borderline in px, integer</li>
		</ul></li>
	<li>state_outline (Dictionary): Define the lines on state borders<ul>
			<li>color: Color of county borders, RGB or Hex in string</li>
			<li>width: The width of borderline in px, integer</li>
		</ul></li>
</ul>

## Examples
### Example 1 - Using figure_factory.create_choropleth()
<img src=basic_choropleth.png>

```
# Define the endpoints 
endpts = list(range(1,6))

fig = ff.create_choropleth(
	  fips = df['fips'], values = df['median_sqft_price'], 
	  colorscale = plotly.colors.sequential.Oranges,
	  show_state_data = True, scope = ['CA'],
	  binning_endpoints=endpts,
	  county_outline={'color': 'rgb(15,15,55)', 'width': 1},
	  state_outline={'color': 'rgb(15,15,55)', 'width': 1},
	  legend_title='Median Rent')

```


