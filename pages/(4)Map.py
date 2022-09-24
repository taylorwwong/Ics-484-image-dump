import dash
from dash import html, dcc, dash_table
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import pathlib
import numpy as np

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

pump = pd.read_csv(DATA_PATH.joinpath('choleraPumpLocations.csv'), header=None)
death = pd.read_csv(DATA_PATH.joinpath('choleraDeathLocations.csv'), header=None)

# map token
token = 'pk.eyJ1IjoidGF5bG9yc3ciLCJhIjoiY2w4ZjRveG9oMDAwcTN3cGZuamJzeWJ1NCJ9.FMi87cj2dRaDV2Szjak7aA'
px.set_mapbox_access_token(token)

# map figure
fig = go.Figure()

fig.add_trace(go.Scattermapbox(lon=death.iloc[:, 1], lat=death.iloc[:, 2], marker=go.scattermapbox.Marker(
            size=8,
            color='rgb(0, 0, 0)',
            opacity=0.7)))

fig.add_trace(go.Scattermapbox(lon=pump.iloc[:, 0], lat=pump.iloc[:, 1], marker=go.scattermapbox.Marker(
            size=15,
            color='rgb(0, 0, 255)',
            opacity=0.7)))

fig.update_layout(
    autosize=True,
    width=1920,
    height=1080,
    showlegend=False,
    mapbox=dict(
        accesstoken=token,
        zoom=15,
        center=dict(lat=51.513341, lon=-0.136668)
    )
)

# register as a new page
dash.register_page(__name__)

layout = html.Div([
    html.H1(children='Snow map recreation', style={'text-align': 'center'}),
    html.Div([dcc.Graph(figure=fig)])
])