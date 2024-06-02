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
dropdown_choices = ['Choice 1', 'Choice 2', 'Choice 3']

# Dash Set up
num_tab = 2
port = 8000
app = dash.Dash()
app.layout = html.Div([
				html.P('Select:'),
				dcc.Dropdown(id='dropdown-choices',
					options=dropdown_choices,
					value=dropdown_choices[0],
					style={'width':'70%','text-align':'left'}
					),
				html.P(id='display')
				])



# Display Income Statement
@app.callback([Output('display','children')],
    [Input('dropdown-choices','value')])
def display_choice(choice):
    return [choice]

# Initiate dashboard
if __name__ == '__main__':
    app.run_server(debug=True, port=port)
