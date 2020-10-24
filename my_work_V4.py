import urllib.request
import bs4
import pandas as pd
import json
import re

h = {'User-Agent': 'Mozilla/5.0'}

def url_check():
    url="https://kr.investing.com/equities/StocksFilter?noconstruct=1&smlID=595&sid=&tabletype=price&index_id=166"
    req=urllib.request.Request(url,headers=h)
    html=urllib.request.urlopen(req)
    bs_obj=bs4.BeautifulSoup(html,"html.parser")
    tbody=bs_obj.find("tbody")
    trs=tbody.findAll("tr")
    href_list=[]
    for i in range(len(trs)):
        td=trs[i].find("td",{"class":"bold left noWrap elp plusIconTd"})
        a=td.find("a").get("href")
        href_list.append(a)
    return href_list

def ticker_list():
    href_list=url_check()
    ticker_list = []
    for i in range(1):
        url2="https://kr.investing.com"+href_list[i]
        req2=urllib.request.Request(url2,headers=h)
        html2=urllib.request.urlopen((req2))
        bs_obj2=bs4.BeautifulSoup(html2,"html.parser")
        ticker=bs_obj2.find("script",{"type":"application/ld+json"}).string
        ticker_json = json.loads(ticker)
        ticker_list.append(ticker_json["tickersymbol"])
    return ticker_list


import re
def data_list(number):
    company_url=url_check()
    second_url = "https://kr.investing.com" + company_url[number] + "-financial-summary"
    second_req = urllib.request.Request(second_url, headers=h)
    second_html = urllib.request.urlopen(second_req)
    second_bs_obj = bs4.BeautifulSoup(second_html, "html.parser")
    company_name=second_bs_obj.find("h1",{"class":"float_lang_base_1 relativeAttr"}).text
    print(company_name)
    symbol_pattern = '\(.*\)'
    symbol = re.findall(symbol_pattern,company_name)[0]
    company_name = re.sub(symbol_pattern, '', company_name)
    symbol = symbol[1:-1]

    print(company_name)
    print(symbol)

data_list(0)

#     first_table = second_bs_obj.find("table", {"class": "genTbl openTbl companyFinancialSummaryTbl"})
#     first_table_date = first_table.findAll("th")  # 날짜 데이터
#
#     date_list=[]
#     for i in range(len(first_table_date)):
#         dates=first_table_date[i].text
#         date_list.append(dates)
#
#     total_revenue_list = []
#     gross_profit_list=[]
#     operating_protfit_list=[]
#     net_income_list = []
#     first_table_tbody = first_table.find("tbody")  # 재무 데이터 시작
#     items_list = first_table_tbody.findAll("tr")
#
#     for number in range(len(items_list)):
#         tag_name = items_list[number].findAll("td")
#         if tag_name[0].text=="총수익":
#             for i in range(len(tag_name)):
#                 revenue_data=tag_name[i].text
#                 total_revenue_list.append(revenue_data)
#         elif tag_name[0].text == "총 이익":
#             for i in range(len(tag_name)):
#                 gross_profit_data = tag_name[i].text
#                 gross_profit_list.append(gross_profit_data)
#         elif tag_name[0].text == "영업 이익":
#             for i in range(len(tag_name)):
#                 operating_protfit_data = tag_name[i].text
#                 operating_protfit_list.append(operating_protfit_data)
#         elif tag_name[0].text == "순이익":
#             for i in range(len(tag_name)):
#                 net_income_data = tag_name[i].text
#                 net_income_list.append(net_income_data)
#
#     print(date_list)
#     print(total_revenue_list)
#     print(gross_profit_list)
#     print(operating_protfit_list)
#     print(net_income_list)
#
# company_url=url_check()
# for i in range(len(company_url)):
#     print(company_url)
#     data_list(i)