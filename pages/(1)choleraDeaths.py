import dash
from dash import html, dcc, dash_table
from plotly.graph_objs.scatter.marker import Line
import pandas as pd
import plotly.graph_objects as go
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
IMAGE_PATH = PATH.joinpath("../images/Cholera_kills.png").resolve()

deaths = pd.read_csv(DATA_PATH.joinpath('choleraDeaths.tsv'), sep='\t')

# sum the 2 columns
deaths['Total'] = deaths.sum(axis=1, numeric_only=True)

# table
table1 = dash_table.DataTable(
    id='datatable_deaths',
    columns=[
        {'name': i, 'id': i}
        for i in deaths.columns
    ],
    data=deaths.to_dict('records'),
    page_size=15,
    style_data={
        'textAlign': 'right'
    },
    style_data_conditional=[
        {'if': {'column_id': 'Date'},
         'width': '130px',
         'textAlign': 'left'},
    ],
    style_header={'textAlign': 'center'}
)

# line chart att/deaths/total
grandTotal = []
counter = 0
for value in deaths['Total']:
    if counter == 0:
        newValue = value
        grandTotal.append(newValue)
        counter += 1
    else:
        newValue = grandTotal[counter-1] + value
        grandTotal.append(newValue)
        counter += 1

deaths['Grand Total'] = grandTotal

# Make the chart
data = [
    go.Scatter(x=deaths.Date, y=deaths.Attack),
    go.Scatter(x=deaths.Date, y=deaths.Death),
    go.Scatter(x=deaths.Date, y=deaths.Total),
    go.Scatter(x=deaths.Date, y=deaths['Grand Total'])
    ]
line = go.Figure(data=data, layout=dict())
line.update_layout(
    xaxis_title='Date',
    yaxis_title='Count',
    legend_title='Instances'
)


dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H1(children='Cholera deaths and attacks', style={'text-align': 'center'}),
    html.Div([table1], style={'width': '30%', 'float': 'left', 'margin-left': '100px'}),
    html.Div([html.Img(src='https://github.com/taylorwwong/Ics-484-project1/blob/main/images/Cholera_kills.png?raw=true')],
             style={'width': '45%', 'float': 'left', 'margin-left': '100px'})
])
