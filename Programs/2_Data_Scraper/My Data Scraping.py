import requests
from bs4 import BeautifulSoup
import pandas as pd
import os 
from csv import DictWriter
import time

url_list = [
    "https://www.ngobase.org/ciswa/PK.SD.KHI/EDU.EN/entrepreneurship-and-collaboration-karachi",
    "https://www.ngobase.org/ciswa/PK.SD.KHI/EDU.CB/capacity-building-and-training-karachi",
    "https://www.ngobase.org/ciswa/PK.SD.KHI/EDU.EL/education-and-literacy-karachi",
    "https://www.ngobase.org/ciswa/PK.SD.KHI/EDU.EL/education-and-literacy-karachi?page=2",
    "https://www.ngobase.org/ciswa/PK.SD.KHI/EDU.EL/education-and-literacy-karachi?page=3",
    "https://www.ngobase.org/ciswa/PK.SD.KHI/EDU.EL/education-and-literacy-karachi?page=4",
    "https://www.ngobase.org/ciswa/PK.SD.KHI/EDU.EL/education-and-literacy-karachi?page=5",
    "https://www.ngobase.org/ciswa/PK.SD.KHI/EDU.EL/education-and-literacy-karachi?page=6",
    "https://www.ngobase.org/ciswa/PK.SD.KHI/EDU.EL/education-and-literacy-karachi?page=7",
    "https://www.ngobase.org/ciswa/PK.SD.KHI/EDU.EL/education-and-literacy-karachi?page=8",
    "https://www.ngobase.org/ciswa/PK.SD.KHI/EDU.EL/education-and-literacy-karachi?page=9",
]

link = "https://www.ngobase.org"
all_link = []
name = []
real_link = []
description = []

try:
    for myurl in url_list:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        res = requests.get(myurl, headers=headers)

        print(res.url) 


        mysoup = BeautifulSoup(res.text, "html.parser")
        # with open("extractfile2.html", "w", encoding='utf-8') as Scrape_file:
        #     Scrape_file.write(mysoup.prettify())

        # print(mysoup.prettify()[:1000])


        for i in mysoup.find_all("span", {"itemprop": "name"}):
            my_link = i.find_next("a")["href"]
            my_name = i.find_next("a").string
            
            if my_link:
                all_link.append(link + my_link)
            
            else:
                all_link.append(" ")
            
            if my_name:
                name.append(my_name)
            
            else:
                name.append(" ")

        for i in mysoup.find_all("div", {"class": "row brief_intro_row"}):
            desc = i.find_next("div", {"class": "col"}).string
            if desc != "":
                description.append(desc.strip().replace("\n", " "))
            
            else:
                description.append("")
                
            
        for i in mysoup.find_all("div", {"class": "col-md-3"}):
            if i.find("div", {"class": "row"}):
                j = i.find("div", {"class": "row"})
                
                if j:
                    k = j.find("div", {"class": "col"})
                    
                    if k.find("span").find("a") == None:
                        continue
                        
                    elif k.find("span").find("a"):
                        l = j.find("span").find("a", {"itemprop": "url"})
                        real_link.append(l["href"])
        
        time.sleep(5)

except Exception as e:
    print(e)

data = pd.DataFrame({
    "Real Link": real_link,
    "Name": name,
    "Link": all_link,
    "Description": description
})

print(data)
data.to_csv("My_data.csv", index=False)

   