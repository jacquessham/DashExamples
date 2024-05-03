import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
"""
Import other necessary packages
"""

"""
Load your data here
"""

# Dash Set up
num_tab = 2
port = 8000
app = dash.Dash()
app = layout(app, num_tab)


# Initiate dashboard
if __name__ == '__main__':
    app.run_server(debug=True, port=port)