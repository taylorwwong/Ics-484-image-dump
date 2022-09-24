import dash
from dash import html, dcc, dash_table
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import pathlib


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

uk = pd.read_csv(DATA_PATH.joinpath('UKcensus1851.csv'), skiprows=3)

table3 = dash_table.DataTable(
    id='UK',
    columns=[{'name': i, 'id': i} for i in uk.columns],
    data=uk.to_dict('records'),
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

# pie (total)
menTotal = uk.male.sum()
femaleTotal = uk.female.sum()
overall = [menTotal, femaleTotal]
labels = ['Male', 'Female']
totalPie = px.pie(values=overall, names=labels, title='Males to Females in the UK')

# pie (Age Men & Female)
pieAgeM = px.pie(values=uk.male, names=uk.age, title='Ages of Males in the UK')
pieAgeF = px.pie(values=uk.female, names=uk.age, title='Ages of Females in the UK')

# bar (Age Men & Female)
barAgeM = px.bar(uk, x=uk.age, y=uk.male, labels={'male': 'Count', 'age': 'Age'})
barAgeF = px.bar(uk, x=uk.age, y=uk.female, labels={'female': 'Count', 'age': 'Age'})


# register as a new page
dash.register_page(__name__)

# layout
layout = html.Div([
    html.H1(children='UK census data (1851)', style={'text-align': 'center'}),

    # 1st row
    html.Div([
        html.Div([table3], style={'width': '25%', 'display': 'inline', 'float': 'left', 'margin-left': '100px',
                                  'margin-top': '80px'}),
        html.Div([dcc.Graph(figure=totalPie)],
                 style={'width': '40%', 'display': 'inline', 'margin-left': '200px', 'float': 'left'})
    ], style={'display': 'center'}),

    # 2nd row
    html.Div([
        html.Div([dcc.Graph(figure=barAgeM)],
                 style={'width': '40%', 'display': 'inline', 'float': 'left'}),
        html.Div([dcc.Graph(figure=pieAgeM)],
                 style={'width': '40%', 'display': 'inline', 'float': 'left'})
    ], style={'display': 'center'}),

    # 3rd row
    html.Div([
        html.Div([dcc.Graph(figure=barAgeF)],
                 style={'width': '40%', 'display': 'inline', 'float': 'left'}),
        html.Div([dcc.Graph(figure=pieAgeF)],
                 style={'width': '40%', 'display': 'inline', 'float': 'left'})
    ], style={'display': 'center'})

])
