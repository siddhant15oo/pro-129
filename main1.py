from bs4 import BeautifulSoup as bs    
import requests
import pandas as pd 

startURL='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page=requests.get(startURL)
print(page)

soup=bs(page.text,'html.parser')
planets_table=soup.find_all('table')
planets_table1=planets_table.find('table_4')


temlist=[]
table_rows=planets_table1.find_all('tr')
for i in table_rows:
    td=i.find_all('td')
    row=[j.text.strip()for j in td]
    temlist.append(row)


dwarf_name=[]
dwarf_mass=[]
dwarf_distance=[]
dwarf_radius=[]

for i in range(0,len(temlist)):
    dwarf_name.append(temlist[i][1])
    dwarf_distance.append(temlist[i][3])
    dwarf_mass.append(temlist[i][5])
    dwarf_radius.append(temlist[i][7])

df=pd.DataFrame(list(dwarf_name,dwarf_mass,dwarf_radius,dwarf_distance),columns=['Name','Mass','Radius','Distance'])
df.to_csv('dwarf_planet.csv')

