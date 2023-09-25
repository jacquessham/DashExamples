import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Read data
df = pd.read_csv('../Data/grades.csv')
students = df['name'].unique()
num_student = len(students)

# Prepare colorscale for each line
colours = ['gold','green','red','lightblue','pink']
nums = [num*1.0/(num_student-1) for num in range(0,num_student-1)] + [1.0]

colourscale_metadata = [[num, colour] 
		for num, colour in zip(nums , colours)]

# Prepare labels
labels = df.columns.tolist()[2:]


# Prepare the setup of the visualization
fig = go.Figure(data=go.Parcoords(
		line={
			'color': df['student_id'],
			'colorscale': colourscale_metadata,
			'showscale': True,
			'cmin':75
		},
		dimensions=[
			{'range':[70,100],
			  'constraintrange':[90,101],
			  'label': labels[0],
			  'values': df[labels[0]]
			},
			{'range':[70,100],
			  'constraintrange':[70,101],
			  'label': labels[1],
			  'values': df[labels[1]],
			  'tickvals':[80, 90, 100],
			  'ticktext':['Fair','Great','Excellent']
			},
			{'range':[70,100],
			  'label': labels[2],
			  'values': df[labels[2]]
			},
			{'range':[70,100],
			  'label': labels[3],
			  'values': df[labels[3]],
			  'tickvals':[70, 80, 90, 100],
			  'ticktext':['C','B','A','A+']
			}
		]
	))

# Layout
fig.update_layout(
    plot_bgcolor = 'white',
    paper_bgcolor = 'white'
)

plotly.offline.plot(fig, filename='advance_pcate.html')