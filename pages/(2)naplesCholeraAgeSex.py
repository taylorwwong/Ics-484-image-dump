import dash
from dash import html, dcc, dash_table
from plotly.graph_objs.scatter.marker import Line
import pandas as pd
import plotly.graph_objects as go
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

naples = pd.read_csv(DATA_PATH.joinpath('naplesCholeraAgeSexData.csv'))


# table
table2 = dash_table.DataTable(
    id='datatable_naples',
    columns=[
        {'name': i, 'id': i}
        for i in naples.columns
    ],
    data=naples.to_dict('records'),
    page_size=15,
    style_data={
        'textAlign': 'right'
    },
    style_data_conditional=[
        {'if': {'column_id': 'age'},
         'width': '130px',
         'textAlign': 'left'},
    ],
    style_header={'textAlign': 'center'}
)

# bar chart Males vs Females
fig = go.Figure()
fig.add_trace(go.Bar(name='Male', x=naples.age, y=naples.male))
fig.add_trace(go.Bar(name='Female', x=naples.age, y=naples.female))
fig.update_layout(
    title={
        'text': 'Males to Females by Age',
    },
    xaxis_title='Deaths',
    yaxis_title='Ages',
    legend_title='Gender'
)

# register as a new page
dash.register_page(__name__)

# layout
layout = html.Div([
    html.H1(children='Naples cholera age/sex data', style={'text-align': 'center'}),
    html.Div([
        html.Div([table2], style={'width': '25%', 'display': 'inline', 'float': 'left', 'margin-left': '100px',
                                  'margin-top': '80px'}),
        html.Div([dcc.Graph(figure=fig)],
                 style={'width': '40%', 'display': 'inline', 'margin-left': '200px', 'float': 'left'})
    ], style={'display': 'center'})
])
