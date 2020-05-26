#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:51:34 2020

@author: bobba
"""

from sqlalchemy import create_engine
import pandas as pd
import time


engine = create_engine("mysql+pymysql://root@localhost/gamedata")

# col pokemon
# column = "#     Name    Type    Total  HP      Attack      Defense         SpAtk       SpDef       Speed"

column = "date     time    rank    mental      eliminations      assist        revive       accuracy        hit            hs           distance            material            material_used               damage          damage_to_players            damage_to_structures"
    
def chargement(x, link, table):
    
    print("Lecture des données")
    col = x.split()
    start_time = time.time()
    df = pd.read_excel(link, encoding="UTF-8")
    df.columns = col
    print("Données lu")
    df.to_sql(table, con = engine, if_exists='append', index=False)
    return print("Temps d execution : %s secondes ---" % (time.time() - start_time))

#path pokemon
#chargement(column,'data/pokemon.xls', 'pkmn')
chargement(column,'data/fortnite.xlsx', 'fortnite')

    # dash_app.layout = html.Div([
    #     go.Bar(
    #     id = 'graph1',
    #     figure = {
    #         'data' [
    #             { 'x': df_sober["hs"], 'y': df_sober["damage_to_players"]},
               
    #         ],
    #     }
    # ),
    #     go.Bar(
    #     id = 'graph2',
    #     figure = {
    #         'data': [
    #             { 'x': df_high["hs"], 'y': df_high["damage_to_players"] },
    #         ],
    #     }
    # ),
    # ])

    