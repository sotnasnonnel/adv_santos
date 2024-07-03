import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3
import logging

# Configuração de logging
logging.basicConfig(level=logging.DEBUG)

from app import app
from components import sidebar

# Layout com sidebar
app.layout = dbc.Container(children=[
    dcc.Location(id="url"),
    dbc.Row([
        dbc.Col([
            sidebar.layout
        ], md=2, style={'padding': '0px'}),
        dbc.Col([
            html.Div(id="page-content")
        ], md=10, style={'padding': '0px'}),
    ])
], fluid=True)

@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def render_page_content(pathname):
    logging.debug(f"Rendering page for pathname: {pathname}")
    if pathname == '/' or pathname == '/home':
        return html.Div("Welcome to the home page!")
    return html.Div("Page not found.")

if __name__ == '__main__':
    app.run_server(debug=True)
