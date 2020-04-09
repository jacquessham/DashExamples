# Part 2: Dash Callbacks

## Last Chapter
Click [here](../Part1) to go back to the last chapter. 

## Goals
In this chapter, we are going over callbacks in Dash, allowing user to filter or select data to update the visualization. The goals of Part 2
<br>
1. Use slider to filter data <br>
2. Use textbox for inputing data<br>
3. Use dropdown list to filter data<br>
4. Use radio items to filter data<br>
5. Use Input() and Output() to update the visualizations.<br>
6. Understand how to pass multiple inputs<br>
7. Generate more than 1 output <br>
8. Provide the state of what user has selected
<br><br>
You may find the reference [here](https://dash.plotly.com/basic-callbacks)

## Input() and Output()
Under dash.dependencies, import Input() and Output() in order to update the visualization on Dash.<br><br>
Before using these functions, you have to make sure you have to assign the id's in components you wish to be receiving the input or generating onto.<br><br>
Like Flask, you have to add "@app.callback()" above the functions, then, you will put Output()'s and Input()'s to locate the components on the html page. 

## Example 3: Slider
There are two steps to add slider on your html page. First, add dcc.Slider() in app.layout. Second, add a function to define how the slider re-generate the visualization.<br><br>
Following the [code](/dash_slider.py) from the Dash tutorial, the result looks like this:
<img src='dash_slider_pic.png'>
<br><br><br><br>
The file [example3_slider.py](/example3_slider.py) is the file built for my practice. The data is the passenger traffic of San Francisco International Airport from [DataSF](https://datasf.org/opendata/). The dashboard is aimed to displaythe passenger traffic of each airline and destination at a given year. The dashboard contains a scatterplot with x-axis of month and y-axis of passenger traffic count using a slider to select the year. Although the visualization violates a lot of principles of data visualization, the purpose of this dashboard is to demostrate how to use a slider to filter the data set. <br><br>
The result looks like this:
<img src='example3_cap.png'>
<br><br>
If you want to display the scatter points in different colour based on the third demension, you may pass a list of dictionary of data points in figure. In dash_slider.py, you may find the list <b>traces</b> to include data from different continent.

## Example 4: Multiple Inputs


## Notes
<ul>
	<li>Never have duplicated id's. Follow the rules of naming id's in html.</li>
	<li>The key and value of tuple in Output/Input is: (id, property)</li>
	<li>In @app.callback(), use list to include more than 1 Input() or Output()</li>
</ul>

## Next Charter
Clicker [here](../Part3) to advance to next chapter.