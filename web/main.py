# -*- coding: utf-8 -*-

import time
import dash
from dash.dependencies import Input, Output
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as go
import serial

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': 'admin'
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

dataset = [0]
port = serial.Serial()
buffer_string = ''

app.layout = html.Div(children=[
    html.Div([
        html.H1('About your room:'),
        html.Div(
            [
                html.P("Air humidity"),
                html.P(id='current-data'),
            ]),
        html.P(' Normal is less less then 60 and more than 40')
    ]),

    dcc.Graph(
        id='air humidity',
        animate=False,
        figure={
            'data': [
                {'x': [1], 'y': dataset}
            ]
        }
    ),

    dcc.Interval(
        id='graph-update',
        interval=1 * 1000
    )

])


@app.callback([Output('air humidity', 'figure'),
               Output('current-data', 'children')],
              [Input('graph-update', 'n_intervals')])
def update_graph(input_data):
    global buffer_string
    buffer_string = buffer_string + port.read(port.inWaiting()).decode("utf-8")
    if '\n' in buffer_string:
        lines = buffer_string.split('\n')
        try:
            dataset.append((int)(lines[-2]))
            if len(dataset) > 10:
                del dataset[0]
        except ValueError:
            pass
        buffer_string = lines[-1]

    n = len(dataset)
    times = np.linspace(1, n, n)

    data = plotly.graph_objs.Scatter(
        x=list(times),
        y=list(dataset),
        name='Air humidity',
        mode='lines+markers'
    )

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[1, 10]),
                                                yaxis=dict(range=[0, 100]))}, \
           "curent air humidity is " + str(dataset[n - 1])


if __name__ == '__main__':
    port = serial.Serial('COM2', timeout=None, baudrate=9600, xonxoff=False, rtscts=False, dsrdtr=False)
    app.run_server(debug=False)
