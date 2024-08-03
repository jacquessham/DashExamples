import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
"""
Import other necessary packages
"""

"""
Load your data here
"""

"""
Define Figure here
"""
# Replace dropdown list here
dropdown_choices1 = ['Choice 1', 'Choice 2', 'Choice 3']
dropdown_choicesA = ['Choice A', 'Choice B', 'Choice C']
dropdown_alignment = 'left' # left, center, right

# Dash Set up
num_tab = 2
port = 8000
app = dash.Dash()
app.layout = html.Div([
				html.Div([
					html.P('Select:'),
					dcc.Dropdown(id='dropdown-choices1',
						options=dropdown_choices1,
						value=dropdown_choices1[0],
						style={'width':'70%','text-align':dropdown_alignment}
						),
					
					], style={'width':'80%', 'display':'inline-block'}),
				html.Div([
					html.P('Select:'),
					dcc.Dropdown(id='dropdown-choicesA',
						options=dropdown_choicesA,
						value=dropdown_choicesA[0],
						style={'width':'70%','text-align':dropdown_alignment}
						),
					
					], style={'width':'18%', 'display':'inline-block'}),
				html.P(id='display1'),
				html.P(id='displayA')
				])



# Display Numerical Choice
@app.callback([Output('display1','children')],
    [Input('dropdown-choices1','value')])
def display_choice(choice):
    return [choice]

# Display Alphabetical Choice
@app.callback([Output('displayA','children')],
    [Input('dropdown-choicesA','value')])
def display_choice(choice):
    return [choice]

# Initiate dashboard
if __name__ == '__main__':
    app.run_server(debug=True, port=port)
