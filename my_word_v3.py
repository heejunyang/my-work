import urllib.request
import bs4
import pandas as pd
import json
import re

h = {'User-Agent': 'Mozilla/5.0'}
table_fix = ["ticker", "항목", "기간1", "기간2", "기간3", "기간4"]


def company_name_list():
    url = "https://www.slickcharts.com/sp500"
    req = urllib.request.Request(url, headers=h)
    html = urllib.request.urlopen(req)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")

    table_class = bs_obj.find("tbody")
    trs = table_class.findAll("tr")

    name_list = []

    for i in range(505):
        companies_division = trs[i].findAll("td")
        company_name = companies_division[1].text
        name_list.append(company_name)

    return name_list


def company_ticker_list():
    url = "https://www.slickcharts.com/sp500"
    req = urllib.request.Request(url, headers=h)
    html = urllib.request.urlopen(req)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")

    table_class = bs_obj.find("tbody")
    trs = table_class.findAll("tr")

    ticker_list = []
    clean_data = []

    for i in range(505):
        companies_division = trs[i].findAll("td")
        company_ticker = companies_division[2].text
        ticker_list.append(company_ticker)
        re_data = re.sub('[./!@#$%%]', '', ticker_list[i])
        clean_data.append(re_data)

    return clean_data


def search_company(company_code):
    url = "https://kr.investing.com/search/?q=" + company_code
    req = urllib.request.Request(url, headers=h)
    html = urllib.request.urlopen(req)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")
    first_a = bs_obj.findAll("a", {"class": "js-inner-all-results-quote-item row"})
    href=''
    for i in range(len(first_a)):
        i_class=first_a[i].find("i").get("class")[2]
        if i_class!="USA":
            continue
        else:
            href=first_a[i].get("href")
    print(href)
    return href

search_company("NFLX")

# def data_list(company_code):
#     second_url = "https://kr.investing.com" + search_company(company_code) + "-financial-summary"
#     second_req = urllib.request.Request(second_url, headers=h)
#     second_html = urllib.request.urlopen(second_req)
#     second_bs_obj = bs4.BeautifulSoup(second_html, "html.parser")
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
#
# tickers=company_ticker_list()
# for i in range(len(tickers)):
#     print(tickers[i])
#     data_list(tickers[i])