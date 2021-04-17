import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df =  # DATOS DEL SANTANDER

fig = px.bar(df, y="Fruit", x="Amount")

app.layout = html.Div(
    children=[
        html.H1(children='MIAX API'),
        html.Div(children='''
            Close Data
        '''),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
    