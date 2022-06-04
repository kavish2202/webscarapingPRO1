import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
r = requests.get(URL)
#print(r)

soup = BeautifulSoup(r.text,"html.parser")
star_table = soup.find("table")
temp_list = []
table_rows = star_table.find_all("tr")
for tr in table_rows :
    td = tr.find_all("td")
    row = [ i.text.rstrip() for i in td ]
  #  print(row)
    temp_list.append(row)
    
print(temp_list[1])
star_names = []
star_distance = []
star_radius = []
star_mass = []

for i in range (1,len(temp_list)) :
    star_names.append(temp_list[i][1])
    star_distance.append(temp_list[i][3])
    star_radius.append(temp_list[i][6])
    star_mass.append(temp_list[i][5])

df2 = pd.DataFrame(list(zip(star_names,star_distance,star_mass,star_radius)),columns=['Star_name','Distance','Mass','Radius'])
df2.to_csv("bright_stars.csv")