import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

import utils

app = dash.Dash(__name__)

api_handler = utils.APIBMEHandler()

app.layout = html.Div(
    children=[
        html.H1(children='MIAX API'),
        html.Div(children='''
            Close Data
        '''),

        html.Label('MARKET: '),
        dcc.Dropdown(
            id='menu-index',
            options=[
                {'label': 'IBEX', 'value': 'IBEX'},
                {'label': 'DAX', 'value': 'DAX'},
                {'label': 'EUROSTOXX', 'value': 'EUROSTOXX'}
            ],
            value='IBEX'
        ),

        html.Label('TICKERS: '),
        dcc.Dropdown(
            id='menu-ticker',
        ),

        dcc.Graph(
            id='example-graph',
        )
    ])


@app.callback(
    Output('menu-ticker', 'options'),
    Input('menu-index', 'value'))
def update_ticker_options(market):
    master = api_handler.get_ticker_master(market)
    lista_tikers = list(master.ticker)
    options = [{'label': tck, 'value': tck} for tck in lista_tikers]
    return options

@app.callback(
    Output('menu-ticker', 'value'),
    Input('menu-ticker', 'options'))
def update_ticker_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('example-graph', 'figure'),
    Input('menu-ticker', 'value'),
    State('menu-index', 'value'))
def update_graph(ticker, market):
    data_close = api_handler.get_close_data_ticker(market, ticker)
    fig = px.line(data_close, y=data_close.values, x=data_close.index)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)