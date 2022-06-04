import requests
from bs4 import BeautifulSoup
import csv

URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
r = requests.get(URL)

def scrape () :
    for i in range (0,1):
        headers = ["V Mag.(mV)","Proper name","Bayer designation","Distance(ly)","Spectral class","Mass(M)","Radius(R)","Luminosity(L)"]
        star_data = []
        soup = BeautifulSoup(requests.page_source,"html.parser")
        for th_tag in soup.find_all("th",attrs = {"class","headerSort"}) :
            a_tags = th_tag.find_all("a")
            temp_list =[]
            for index,a_tags in enumerate(a_tags):
                if(index==0):
                    temp_list.append(a_tags[0].contents[0])
                else :
                    try:
                        temp_list.append(a_tags.contents[0])
                    except :
                        temp_list.append("")

            star_data.append(temp_list)

        request.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]').click()
    
    with open("scraper_1.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerow(planet_data)

scrape()



