import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

options = ['Weight','Length','Volume']
unit_options = ['Imperial','Metrics']


app.layout = html.Div([
	html.H1(children='''
		Example 5: Multiple Inputs, Multiple Outputs, and State
	'''), # Layout position 0, headline

	html.Div(html.P(['''
		This example demostrates multiple outputs, chained callbacks,
		and State.
	''',
	html.Br(),
	'''
		In this example, you may use this for converting units. Select
		your desired metrics and types. Then, enter the number and it
		will convert to other units.
	'''

	])), # Position 1, description

	html.Div([
		dcc.RadioItems(
			id='unit-radio',
			options=[{'label': unit, 'value':unit} for unit in
			          unit_options],
			value=unit_options[0]),
		html.Hr(),
		dcc.RadioItems(
			id='options-radio',
			options=[{'label': choice, 'value':choice} for choice
			          in options],
			value=options[0]),
		html.Hr()

	]), # Position 2, inputs

	

	html.Div(id='state-div'), # Position 4, State

	html.Br(), html.Br(),

	html.Div(children='''
			Please enter a number in the below text box:
		'''), # Position 5, instruction to enter initial value

	dcc.Input(id='input-textbox', value='', type='text'),
	# Position 6, textbox input

	html.Hr(),

	html.Div([
		html.Table([
			html.Tr([html.Td('It is equivalent to: '),
				     html.Td(id='input-val-neg')]),
			html.Tr([html.Td('The initial value:'),html.Td(id='input-val')]),
			html.Tr([html.Td('It is equivalent to: '),
				     html.Td(id='input-val-plus1')])
		]) # End table

	]) # Position 7, output in Table

]) # End Outer Div

# Display the state
@app.callback(Output('state-div','children'),
	          [Input('unit-radio','value'), Input('options-radio','value')])
def update_state(selected_metric, selected_type):
	return 'You have selected %s in %s.'%(selected_type, selected_metric)

@app.callback([Output('input-val-neg','children'),
	           Output('input-val','children'),
	           Output('input-val-plus1','children')],
	           [Input('unit-radio','value'),
	            Input('options-radio','value'),
	            Input('input-textbox','value')
	           ])
def calculate(selected_metric, selected_type, inti_val):
	input_val_neg, input_val, input_val_1 = (None, None, None)
	if inti_val == '':
		inti_val = 1
	else:
		# The value entered in textbox is string, convert to number
		inti_val = float(inti_val)

	if selected_type == 'Weight':
		if selected_metric == 'Imperial':
			input_val_neg = f'{inti_val*16:.2f} oz'
			input_val = f'{inti_val:.2f} lbs'
			input_val_1 = f'{inti_val/2240:.4f} tons'
		elif selected_metric == 'Metrics':
			input_val_neg = f'{inti_val*1000:.2f} grams'
			input_val = f'{inti_val:.2f} kilograms'
			input_val_1 = f'{inti_val/1000:.4f} metric tons'

	elif selected_type == 'Length':
		if selected_metric == 'Imperial':
			input_val_neg = f'{inti_val*5280:.2f} feet'
			input_val = f'{inti_val:.2f} miles'
			input_val_1 = f'{inti_val*1760:.2f} yards'
		elif selected_metric == 'Metrics':
			input_val_neg = f'{inti_val*1000:.2f} meters'
			input_val = f'{inti_val:.2f} kilometers'
			input_val_1 = f'{inti_val*100000:.2f} centimeters'

	elif selected_type == 'Volume':
		if selected_metric == 'Imperial':
			input_val_neg = f'{inti_val*16:.2f} cups'
			input_val = f'{inti_val:.2f} gals'
			input_val_1 = f'{inti_val*4:.2f} quarts'
		elif selected_metric == 'Metrics':
			input_val_neg = f'{inti_val*1000:.2f} mL'
			input_val = f'{inti_val:.2f} L'
			input_val_1 = f'{inti_val/1000:.4f} Cubic metre'

	return input_val_neg, input_val, input_val_1


if __name__ == '__main__':
    app.run_server(debug=True, port=8053)