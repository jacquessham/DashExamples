from random import randint
import dash
import dash_core_components as dcc
import dash_html_components as html


# Declare Dash properties
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

num = randint(1,11)
num2 = randint(11,21)
my_github = 'https://github.com/jacquessham'
text = '''
			# Let's draw two random numbers!
			Let's draw a number between 1 and 10, and a number between
			11 and 20.
			## Draw a number between 1 and 10
			Between 1 and 10, I have drawn a {}. 
			## Draw a number between 11 and 20
			Between 11 and 20, I have drawn a {}.
			## External site
			Free feel to visit my [Github]({})
       '''.format(num, num2, my_github)
       # In Dash markdown, <br> does not work, simply put extra nextline


app.layout = html.Div([
	html.H1(children='Example 6: Markdown'), # Position 0, headline
	html.P('''
			This example demostrates how to use markdown in Dash.
		'''), # Position 1, description
	html.Hr(),
	dcc.Markdown(text) # Position 2, markdown
])

if __name__ == '__main__':
	app.run_server(debug=True, port=8054)