#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:09:39 2020

@author: utilisateur
"""

import pandas as pd
from sqlalchemy import create_engine

# table_sql = 'rocket_deadzone_settings'
table_sql = 'rocket_cam_settings'
engine = create_engine('mysql+pymysql://root@localhost/gamedata')

# 'data/rocket-league/deadzone_settings.xls'


dateparse = lambda x: pd.datetime.strptime(x, '%d %B %Y')
df = pd.read_excel('data/rocket-league/camera_settings.xls', sep=",", parse_dates=['Last_Update'])

print(df)

# df2 = df

# df2['Last_Update'] = pd.to_datetime(df2.Last_Update, format='%Y-%m-%d')

df.to_sql(table_sql, con=engine, if_exists='append', index=False)