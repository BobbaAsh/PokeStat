#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:09:39 2020

@author: utilisateur
"""

import pandas as pd
from sqlalchemy import create_engine

table_sql = 'rocket_cam_settings_2'
engine = create_engine('mysql+pymysql://root@localhost/gamedata')

dateparse = lambda x: pd.datetime.strptime(x, '%d %B %Y')
df = pd.read_excel('data/rocket-league/camera_settings_2.xls',sep=",", parse_dates=['Last_Update'],dateparser=dateparse)

# Création de pourcentage.

df['A_FOV'] = (df.FOV / df.FOV.sum())*100
df['A_Height'] = (df.Height / df.Height.sum())*100
df['A_Angle'] = (df.Angle / df.Angle.sum())*100
df['A_Stiffness'] = (df.Stiffness / df.Stiffness.sum())*100
df['A_Distance'] = (df.Distance / df.Distance.sum())*100



# Ascending index by values
# df = df.sort_values(by = 'A_Distance', ascending = False)


df.to_sql(table_sql, con=engine, if_exists='append', index=False)

print(df)



