# Candlestick Charts
Candlestick chart is chart to display the price, including opening price, closing price, highest and lowest price, of a security or derivatives in a given period. In this folder, we will go over how to create candlestick charts with Python and Plotly.

## Files
The following scripts are used in this chapter:
<ul>
	<li>AAPLprice.py</li>
</ul>

## Pacakges Needed
This chapter requires the following packages for the scripts used:
<ul>
	<li>Pandas</li>
	<li>Plotly</li>
	<li>yfinance (Only used for <i>AAPLprice.py</i> to obtain data, does not require if you have any data set from other sources)</li>
</ul>

## Data Used
This chapter may obtain Apple stock price via API call using <i>yfinance</i>. In this

## Syntax
### Data
Data is a list of <i>go.Candlestick()</i>. Although you are expected to only have one <i>go.Candlestick()</i> in the list, you should put <i>go.Candlestick()</i> in a list for Plotly.
<br><br>
go.Candlestick() has the following parameters:
<ul>
	<li>x: Date</li>
	<li>open: Opening price of the security/derivative</li>
	<li>high: Highest price of the security/derivative</li>
	<li>low: Lowest price of the security/derivative</li>
	<li>close: Closing price of the security/derivative</li>
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
	<li>yaxis (Dictionary): Y-axis setting
		<ul>
			<li>title: Y-axis title</li>
			<li>tickmode: Setting of ticks</li>
			<li></li>
		</ul></li>
	<li>xaxis (Dictionary): X-axis setting
		<ul>
			<li>title: X-axis title</li>
			<li>tickmode: Setting of ticks</li>
			<li><ul>
				<li>rangeslider (Dicionary): Whether to include rangeslider for user to shrink or expand the range, default to <b>True</b> </li> and display the same candlestick chart in the rangeslider
			</ul></li>
		</ul></li>
	
</ul>
<br><br>
Candlestick Chart Exclusive parameters:
<ul>
	<li>Data
		<ul>
			<li>open: Opening price of the security/derivative</li>
			<li>high: Highest price of the security/derivative</li>
			<li>low: Lowest price of the security/derivative</li>
			<li>close: Closing price of the security/derivative</li>
		</ul></li>
	<li>Layout
		<ul>
			<li>xaxis (Dictionary): y-axis setting
				<ul>
					<li>rangeslider (Dicionary): Whether to include rangeslider for user to shrink or expand the range</li>
				</ul></li>
			<li></li>
		</ul></li>
</ul>


## Examples
### Simple Candlestick Chart
<img src=Candlestick.png>

```
# Prepare data
data.append(go.Candlestick(x=df['Date'], open=df['Open'],
	                       high=df['High'], low=df['Low'],
	                       close=df['Close']))

layout = {'title':{'text':'Year-to-Date Apple Stock Price','x':0.5},
          'xaxis':{'title':'Date','rangeslider':{'visible':False}},
		  'yaxis':{'title':'Price ($)'},
          'hovermode':False}
```

<b>By default, Plotly set rangeslider to be visible. You must turn off manually.</b>

## Reference
Plotly <a href=https://plotly.com/python/candlestick-charts/>Candlestick Chart Documentation</a>
