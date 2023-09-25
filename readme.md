# Dash Examples

This is the effort to introduce to use Dash with Python to build dashboard for business intelligence purpose. Please also visit my <a href="https://medium.com/@jjsham/building-dashboard-using-plotly-dash-36bf94a1137">Medium Post</a> to introduce using Plotly Dash to build a dashboard.

## What is Dash?
Dash is an open source Python library to create a web-based visualiztion application provided by Plotly. This package is great for building dashboard, markdown reports and any kinds of data visualization. This package is built on top of pure Plotly and Flask allow you to build a dashboard using pure Plotly library and host the dashboard via Flask. The ideal use of this library could be building a dashboard using Dash and host it on AWS (Or other cloud computers) and allow views to read it via a link.

## Good Reasons to build dashboard with Dash

### Open Source Tool (It's Free!)
It is free. BI tools like Tableau or Microsoft Power BI are great but they are costly to operate. Dash is a good alternative tool to provide similar quality and experience with no cost. 

### Run in Python
Dash runs in Python. You may use Pandas and any Python library to manipulate your data frame before render the visualization with Dash.

### Great Appearance
The quality of the visualization in Dash or Plotly is very high that is comparable with Tableau charts because Dash renders d3 visualization. 

### Integrated with Plotly
Plotly is one of the great open source visualization package in the Python library. Many Python developers use Plotly for data visualization. As a product of Plotly, Dash allows developers to integrate their Plotly visualization on the Dash dashboard. Dash is a tool to make building dashboard using Plotly graph easier.

### Integrated with Flask
Dash runs web server in Flask. No need to set up in Flask, easy to host the web server in AWS. You don't need to be a web programmer to build the dashboard.

### Easy to use
Although the dashboard is viewed in a web broswer, it is a high level tool that the developers are only required to write in Python and have some understanding of html. It means no Javascript or d3 is needed to be written to produce the same product but you may leverage the interactive elements available in d3. Dash is very customizable that you may custom the dashboard using the html layout which eliminates the contraint of pure Plotly's customizability.

## Plotly Tutorial
Dash relies on Plotly plots, it is a good idea to understand how Plotly works first. Here are the tutorial and examples for plotting in Plotly:<br>
[Fundamentals](/PlotlyExample)<br>
[Bar Charts](/PlotlyExample/BarChart)<br>
[Line Charts](/PlotlyExample/LineChart)<br>
[Scatter Plot/Bubble Chart](/PlotlyExample/ScatterPlot)<br>
[Box Plots](/PlotlyExample/BoxPlot)<br>
[Pie/Donut Charts](/PlotlyExample/PieChart)<br>
[Histogram](/PlotlyExample/Histogram)<br>
[Treemaps](/PlotlyExample/Treemap)<br>
[Heatmaps](/PlotlyExample/Heatmap) <br>
[Candlestick Charts](/PlotlyExample/CandlestickChart)<br>
[Funnel Chart (Coming soon...)](/PlotlyExample/FunnelChart)<br>
[Choropleth Graphs](/PlotlyExample/ChoroplethGraph)<br>
[Sunburst Charts](/PlotlyExample/Sunburst) <br>
[Parallel Categories Diagram](/PlotlyExample/ParallelCoordinatesPlot)<br>
[Sankey Diagram (Coming Soon...)](/PlotlyExample/SankeyChart)<br>
[Dendrograms (Decision Tree)  (Coming Soon...)](/PlotlyExample/DecisionTree)<br>
<br><br>
Or click the link here to the [Plotly Example folder](/PlotlyExample) for the selected list of the visualizations can be made with Plotly.

## Tutorial and Examples
This repositories contains examples from the official Dash site and myself. There are 3 parts for the tutorial with different levels of functionality.
<br><br>
[Part 1 - Basics of Using Dash](/Part1) <br>
[Part 2 - Dash Callbacks](/Part2)<br>
[Part 3 - Interactive Visualization](/Part3)<br>
[Dashboard Example - Gaming Console Market Share in 2018](/DashboardExample)

## Template Framework for Plotly
You may find the template framework for Plotly when you want to quickly plot something with Plotly. You may find the scripts in the [Template Framework](/PlotlyTemplateFramework) folder.

## Reference
Official Website of Dash: [Dash User Guide](https://dash.plotly.com/)<br>
Medium Post: [Brief Introduction of Dash](https://medium.com/plotly/introducing-dash-5ecf7191b503) by <i>Plotly</i>