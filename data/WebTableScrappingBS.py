from bs4 import BeautifulSoup
import requests
import pandas as pd 

# néttoie les doublon d'une liste
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist


url = 'https://liquipedia.net/rocketleague/List_of_player_camera_settings'


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table',{'class':'sortable rl-responsive-table-sortable'}).tbody
rows = table.find_all('tr')

# columns = [v.text.replace('\n','') for v in rows[0].find_all('th')]

# Camera col name
columns = ['Player','Team','Camera_Shake','FOV','Height','Angle','Distance','Stiffness','Swivel_Speed','Transition_Speed','Ball_Camera','Last_Update']

# Deadzone col name
# columns = ['Player','Team','Deadzone_Shape','Deadzone','Dodge_Deadzone','Aerial_Sensivity','Steering_Sensivity','Last_Update']

df = pd.DataFrame(columns=columns)

for i in range(1, len(rows)):
    tds = rows[i].find_all('td')

    if len(tds) == 12:
        values = [tds[0].text.replace('\n',''), tds[1].text.replace('\n',''), tds[2].text.replace('\n',''), tds[3].text.replace('\n',''), tds[4].text.replace('\n',''), tds[5].text.replace('\n',''), tds[6].text.replace('\n',''), tds[7].text.replace('\n',''), tds[8].text.replace('\n',''), tds[9].text.replace('\n',''), tds[10].text.replace('\n',''), tds[11].text.replace('\n','')]
    else:
        values = [td.text for td in tds]
    
    df = df.append(pd.Series(values, index=columns), ignore_index=True)


df2 = df 

new_col = [''.join(unique_list(i.split())) for i in df2["Player"]]
df2["Player"] = new_col

print(df2)

df2.to_excel('data/rocket-league/camera_settings_2.xls', index=False)

