import urllib.request
import bs4
import numpy as np
import pandas as pd
import re

h={"User-Agent":"Mozilla/5.0"}
url="https://www.slickcharts.com/sp500"
req=urllib.request.Request(url,headers=h)
html=urllib.request.urlopen(req)
bs_obj=bs4.BeautifulSoup(html,"html.parser")

table_class=bs_obj.find("tbody")
trs=table_class.findAll("tr")

name_list=[]
ticker_list=[]
table_fix=["name","ticker"]
json_list={}


for i in range(505):
    companies_division=trs[i].findAll("td")
    company_name=companies_division[1].text
    name_list.append(company_name)
    company_ticker=companies_division[2].text
    ticker_list.append(company_ticker)

clean_data=[]

for i in range(505):
    re_data=re.sub('[./!@#$%%]','',ticker_list[i])
    clean_data.append(re_data)

print(clean_data)

# company_name=companies_division[i+1].text
# print(company_name)



