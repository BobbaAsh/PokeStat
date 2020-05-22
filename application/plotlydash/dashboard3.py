# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:34:52 2020

@author: Bobba Ash
"""

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
                         routes_pathname_prefix='/lol/',
                         external_stylesheets=['/static/dist/css/styles.css',
                                               'https://fonts.googleapis.com/css?family=Lato']
                         )


    db = pymysql.connect("localhost", "root", "", "gamedata")
    sql_query = pd.read_sql_query("SELECT * FROM pkmn", db)
    df = pd.DataFrame(sql_query)


    dash_app.index_string = html_layout
    
    dash_app.layout = html.Div(
        children=[dcc.Dropdown(
            id='histogram-graph',
             options=[{'label': i, 'value': i} for i in df['Name']
                      ],
             
             placeholder="Select Pokemon",
             multi=True,
            clearable=True
        ),
            #create_data_table(df)
    ],
        id='dash-container'
    )

    @dash_app.callback(
                    dash.dependencies.Output('dash-container', 'children'),
                    [dash.dependencies.Input('histogram-graph', 'value')])

    def update_output(value):
                                    query = pd.read_sql_query("SELECT * FROM pkmn WHERE Name in {}".format(value).replace("[", "(").replace("]" , ")"), db)
                                    fig = go.Figure(data=[
                                    go.Bar(name='Sp Atk', y=query['SpAtk'], x=value),
                                    go.Bar(name='Sp Def', y=query['SpDef'], x=value),
                                    go.Bar(name='Speed', y=query['Speed'], x=value),
                                    go.Bar(name='Attack', y=query['Attack'], x=value),
                                    go.Bar(name='Defense', y=query['Defense'], x=value),
                                    go.Bar(name='HP', y=query['HP'], x=value)
                            ])
                                    fig.update_layout(barmode='group')
                                    return fig.show()
            
    return dash_app.server


