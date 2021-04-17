import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import utils

app = dash.Dash(__name__)

api_handler = utils.APIBMEHandler()
master = api_handler.get_ticker_master('IBEX')
lista_tikers = list(master.ticker)

data_close = api_handler.get_close_data_ticker('IBEX', 'SAN')


fig = px.line(data_close, y=data_close.values, x=data_close.index)

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
            options=[
                {'label': tck, 'value': tck}
                for tck in lista_tikers
            ],
            value='SAN',
            id='menu-ticker',
        ),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)