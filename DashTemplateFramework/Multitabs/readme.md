# Multitabs
Multi-tabs module allows users to display the dashboard on the selected category in the dashboard. There are two approaches and this folder includes the modules with both approaches.

## Module
There are 2 approaches to create multitabs:
<ul>
	<li>Create a Div independent of individual tabs (One Div-approach)</li>
	<li>Create a Div along with all individual tabs (MultiDiv-approach) - Not recommended</li>
</ul>

With the first approach, it allows the code to be more dynamic, flexible and robust without declare each a Div in each tab. With the second approach, it allows you to have Div's more customized layout under each tab and without loading every time switching back and forth between tabs.
<br><br>
The second approach only works for Plotly chart is static because the callback function only works on one Div/Graph component. If there are two tabs with two Graph component, the callback function can only handles one component at a time. But the input will mess up another function and create errors, and thus only works for static to prevent another component to re-render with incorrect parameters. Therefore, this approach is not recommended for dynamic dashboard. 

### One Div-Approach
The module allows user to select the tab. The visualization is independent from the tab so it will trigger and re-generate the visualization when a tab is selected.

<img src=one_div.png>


## Reference
link: <a href="https://dash.plotly.com/dash-core-components/tabs">here</a>