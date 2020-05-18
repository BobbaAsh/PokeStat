#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:51:34 2020

@author: bobba
"""

from sqlalchemy import create_engine
import pandas as pd
import time


engine = create_engine("mysql+pymysql://root:password@localhost/pokemon")


column = "#     Name    Type    Total  HP      Attack      Defense         SpAtk       SpDef       Speed"
    
def chargement(x, link, table):
    
    print("Lecture des données")
    col = x.split()
    start_time = time.time()
    df = pd.read_excel(link, encoding="UTF-8")
    df.columns = col
    print("Données lu")
    df.to_sql(table, con = engine, if_exists='append', index=False)
    return print("Temps d execution : %s secondes ---" % (time.time() - start_time))

chargement(column,'pokemon.xls', 'pkmn')
