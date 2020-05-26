#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:13:46 2020

@author: bobba
"""

# tutorial VOD : https://www.youtube.com/watch?list=PLuVTNX0oceI87L2sPUTODZmwn-ORos-9Z&time_continue=1&v=egYVP-TeSg8&feature=emb_logo

import requests
import lxml.html as lh
import pandas as pd

url='https://pokemondb.net/pokedex/all'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//tr')
col=[]
i=0

#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    print('%d:"%s"'%(i,name))
    col.append((name,[]))

for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=10:
        break
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1
        
Dict={title:column for (title,column) in col}

df=pd.DataFrame(Dict)

df.to_excel('rocketleague.xls', encoding='utf-8')