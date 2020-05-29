#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:09:39 2020

@author: utilisateur
"""

import pandas as pd
from sqlalchemy import create_engine

table_sql = 'rocket_deadzone_settings'
engine = create_engine('mysql+pymysql://root:password@localhost/gamedata')

dateparse = lambda x: pd.datetime.strptime(x, '%d %B %Y')
df = pd.read_excel('deadzone_settings.xls',sep=",")
# Création de pourcentage.


# Ascending index by values
# df = df.sort_values(by = 'A_Distance', ascending = False)


df.to_sql(table_sql, con=engine, if_exists='append', index=False)

print(df)



