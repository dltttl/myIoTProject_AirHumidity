# -*- coding: utf-8 -*-

import dash
from dash.dependencies import Input, Output
import dash_auth
import dash_enterprise_auth as auth
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': 'admin'
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

adress = 'C:\data.txt'
data = np.loadtxt(adress, delimiter=', ', skiprows=0)
# file = pd.read_csv(adress, sep=',')
n = data.shape[0]
times = np.linspace(1,n)
out = ''

app.layout = html.Div(children=[

    html.Div([
        html.H1('About your room:'),
        html.Div([
            html.P(out),
            html.P('Now your air humidity is ' + str(data[n-1]) + ', normal is more than 50 and less than 80'),
        ])
    ]),
    dcc.Graph(
        id='temperature',
        figure={
            'data': [
                {'x': times, 'y': data},
            ],
            'layout': {
                'title': 'Air humiduty'
            }
        }
    ),
])

if __name__ == '__main__':
    app.run_server(debug=False)