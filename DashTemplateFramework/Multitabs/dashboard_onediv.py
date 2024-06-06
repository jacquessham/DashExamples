import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dashboard_structure import layout
"""
Import other necessary packages
"""

"""
Load your data here
"""

"""
Define Figure here
"""
def figure1():
    return {'data': [{
                        'x': [1, 2, 3],
                        'y': [3, 1, 2],
                        'type': 'bar'
                    }]}

def figure2():
    return {'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]}

# Dash Set up
num_tab = 2
port = 8000
app = dash.Dash()
app = layout(app, num_tab)

# Display Income Statement
@app.callback([Output('content','children')],
    [Input('dashboard-tabs','value')])
def display_income_statement(tab):
    if tab == 'label_1':
        return [html.Div(dcc.Graph(figure=figure1()))]
    return [html.Div(dcc.Graph(figure=figure2()))]

# Initiate dashboard
if __name__ == '__main__':
    app.run_server(debug=True, port=port)
