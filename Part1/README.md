# Part 1: Basics of Using Dash

## Prequisite of using Dash
<ul>
	<li> Knowing how Plotly works in Python</li>
	<li> Knowing how Flask works in Python</li>
	<li> Understand how html works</li>
</ul>

## Goals
The goals of Part 1 are:<br>
1. Understand the basic layout of Dash<br>
2. Understand the basic of dcc and html packages<br>
3. Graph a chart using figure in dcc.Graph()<br>
4. Pass a previous Plotly graph on Dash

## Plotly Dash Example
Reference here: <a href="https://dash.plotly.com/layout">Dash Layout</a>
<br>
<br>
app.py is the code copied from the plotly dash site for testing.
<br>
<br>
Dash is very similar to using Flask on building a html. In this example, app.layout to outline the html page and build the Plotly figure on top of the html elements. The example on the Dash Layout site demostrates a higher level method to build bar chart on Dash.
<br>
<br>
[dash_part1.py](dash_part1.py) is the file identical to <b>app.py</b> from the Dash Layout reference page.

## Example 1: Practice on my own
Plotly Dash can be viewed as a high-level visuilazation tool hosted by Flask. To build a Plotly Dash dashboard, you have to declare an <b>app object</b>, which is a Flask object. Then, you will design the dashboard by adding html components or dash core components into the <b>layout</b> instance. <b>Html components</b> are basic html instance; dash core components (dcc) are Dash-built object to show graphs or other Dash objects. The layout instance of app is composed of a tree of compoents. In each html components or dcc consists of attributes to define content, graphs, or format. For example, if you put html.H1(chilren='Hello World!'), Dash will translate that to < H1>Hello World!< /H1> on a html file. The code is run, it renders the html as you have defined and hosted on Flask server.
<br><br>
I used whisky.csv to plot a bar chart. You may find the data <a href="https://github.com/jacquessham/ScotchWhisky/tree/master/Data">here</a>. And the result looks like this:
<br>
<img src="whisky_dash.png">
<br>
<br>
And the original Plotly graph looks like:
<img src="whisky_plotly.png">
<br><br>


## Example 2: Using go.Figure on Dash
Reference here: <a href="https://dash.plotly.com/dash-core-components/graph">Plotly Figures on Dash</a>
<br><br>
If you know how to make a graph on Plotly and wish to host it on Dash. You may also do this. If you have existing code define the figure <b>object</b> in Plotly already, you may pass this figure object to dcc.Graph(), ie, you may define fig first, and pass fig to dcc.Graph(), dcc.Graph(figure=fig). It means you could define the figure instance outside of <b>app.layout</b>. In this example, I will use my existing Plotly graph and host it on Dash. The Plotly line chart is about the traffic of IPs given in the data set and was a homework I worked on my Data Visualization class in graduate school.
<br><br>
The result looks like this:
<img src="computer_security_dash.png">

## Notes
<ul>
	<li>Dash's purpose is to build the visualization on a html page and host the html page on a Flask server.</li>
	<li>Dash relies on <b>Flask</b>. Once you import Dash, it automatically import Flask. And the code is very similar to Flask.</li>
	<li>app.layout lists the html page in hierarchical structure</li>
	<li>You can either define figure outside or within app.layout. If you have done a visualization with Plotly before, you may just pass your previous Plotly figure into app.layout.</li>
	<li>Flask host your html page at your localhost. To change port, add 'port=xxxx' as an arguement in app.run_server()</li>
</ul>

## Next Charter
Clicker [here](../Part2) to advance to next chapter.