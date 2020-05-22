import numpy as np
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from .layout import html_layout
import pymysql
import plotly.graph_objects as go

def create_dashboard(server):
    dash_app = dash.Dash(server=server, name = 'fortnite',
                         routes_pathname_prefix='/fortnite/',
                         external_stylesheets=['/static/dist/css/styles.css',
                                               'https://fonts.googleapis.com/css?family=Lato']
                         )


    db = pymysql.connect("localhost", "root", "", "gamedata")
    sql_query_sober = pd.read_sql_query("SELECT * FROM fortnite WHERE mental = 'sober'", db)
    df_sober = pd.DataFrame(sql_query_sober)
    sql_query_high = pd.read_sql_query("SELECT * FROM fortnite WHERE mental = 'high'", db)
    df_high = pd.DataFrame(sql_query_high)
    dash_app.index_string = html_layout
    
    dash_app.layout = html.Div([
    dcc.Graph(
        id = 'graph1',
        figure = {
            'data': [
                { 'x': df_sober["hs"], 'y': df_sober["damage_to_players"], 'type': 'bar' },
            ],
                            'layout': {
            'title': 'Damage Players To Headshot when Players is Sober',
            }
        }   
    ),
    dcc.Graph(
        id = 'graph2',
        figure = {
            'data': [
                { 'x': df_high["hs"], 'y': df_high["damage_to_players"], 'type': 'bar' },
            ],
                            'layout': {
            'title': 'Damage Players To Headshot when Players is High',
            }                    
        }
    ),    
    ])


    return dash_app.server
