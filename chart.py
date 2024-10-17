import plotly.graph_objects as go

import pandas as pd
import json

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=[go.Surface(z=z_data.values)])

fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

# Convert figure to JSON
fig_json = fig.to_json()

# Write JSON to file
with open('/home/michal/projects/plotly-react-example/figure.json', 'w') as file:
    file.write(fig_json)