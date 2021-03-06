import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from .layout import html_layout
import pymysql
import plotly.graph_objects as go
    
db = pymysql.connect("localhost", "root", "password", "gamedata")

def create_dashboard(server):
    dash_app = dash.Dash(server=server,
                         routes_pathname_prefix='/dashapppkmn/',
                         external_stylesheets=['/static/dist/css/styles.css',
                                               'https://fonts.googleapis.com/css?family=Lato']
                         )
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
        html.Button(id='submit-button-state', n_clicks= 0, children='Submit')
         #create_data_table(df)
    ],
        id='dash-container'
    )

    @dash_app.callback(
                    dash.dependencies.Output('dash-container', 'children'),
                    [dash.dependencies.Input('submit-button-state', 'n_clicks')],
                    [dash.dependencies.State('histogram-graph', 'value')]) 


    def update_output(n_clicks,value):
                                           if n_clicks > 0:
                                                    query = pd.read_sql_query("SELECT * FROM pkmn WHERE Name in {}".format(value).replace("[", "(").replace("]" , ")"), db)
                                                    fig = go.Figure(data=[
                                                    go.Bar(name='Sp Atk', y=query['SpAtk'], x=value),
                                                    go.Bar(name='Sp Def', y=query['SpDef'], x=value),
                                                    go.Bar(name='Speed', y=query['Speed'], x=value),
                                                    go.Bar(name='Attack', y=query['Attack'], x=value),
                                                    go.Bar(name='Defense', y=query['Defense'], x=value),
                                                    go.Bar(name='HP', y=query['HP'], x=value)
                                            ])
                                                    fig.update_layout(title = "Pokemon compare", barmode='group')
                                                    return fig.show() 
                                                           
                                           else:
                                                return dash_app.layout
    return dash_app.server
