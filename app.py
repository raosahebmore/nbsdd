# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from plotly import graph_objs as go
N = 100000


app = dash.Dash()
app.config['suppress_callback_exceptions']=True


app.layout = html.Div(
    html.H1(children='Hello Dash'))

if __name__ == '__main__':
    app.run_server()
