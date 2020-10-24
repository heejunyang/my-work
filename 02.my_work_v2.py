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
    first_a = bs_obj.find("a", {"class": "js-inner-all-results-quote-item row"}).get(
        'href')  # .get(href)를 통해 아래 결과에서 href 추출
    return first_a


def data_list(company_code):
    second_url = "https://kr.investing.com" + search_company(company_code) + "-financial-summary"
    second_req = urllib.request.Request(second_url, headers=h)
    second_html = urllib.request.urlopen(second_req)
    second_bs_obj = bs4.BeautifulSoup(second_html, "html.parser")
    first_table = second_bs_obj.find("table", {"class": "genTbl openTbl companyFinancialSummaryTbl"})

    first_table_date = first_table.findAll("th")  # 날짜 데이터
    first_table_tbody = first_table.find("tbody")  # 재무 데이터 시작
    items_list = first_table_tbody.findAll("tr")
    total_revenue_list = items_list[0].findAll("td")
    gross_profit_list = items_list[1].findAll("td")
    operating_income_list = items_list[2].findAll("td")
    net_income_list = items_list[3].findAll("td")

    date = [company_code]
    total_revenue = [company_code]

    gross_profit = [company_code]
    operating_income = [company_code]
    net_income = [company_code]
    json_date = {}
    json_revenue = {}
    json_gross_profit = {}
    json_operating_income = {}
    json_net_income = {}
    excel_list = []

    for number in range(5):
        dates = first_table_date[number].text
        date.append(dates)
        revenues = total_revenue_list[number].text
        total_revenue.append(revenues)
        gross_profits = gross_profit_list[number].text
        gross_profit.append(gross_profits)
        operating_incomes = operating_income_list[number].text
        operating_income.append(operating_incomes)
        net_incomes = net_income_list[number].text
        net_income.append(net_incomes)

    for number in range(6):
        json_date[table_fix[number]] = date[number]
        json_revenue[table_fix[number]] = total_revenue[number]
        json_gross_profit[table_fix[number]] = gross_profit[number]
        json_operating_income[table_fix[number]] = operating_income[number]
        json_net_income[table_fix[number]] = net_income[number]

    # print(json_date)
    # print(json_revenue)
    # print(json_gross_profit)
    # print(json_operating_income)
    # print(json_net_income)
    excel_list.append(json_date)
    excel_list.append(json_revenue)
    excel_list.append(json_gross_profit)
    excel_list.append(json_operating_income)
    excel_list.append(json_net_income)

    return excel_list


company_codes=company_ticker_list()
print(company_codes)
print(len(company_codes))

new_list=[]

for i in range(504):
    company_codes[i]=data_list(company_codes[i])
    new_list=new_list+company_codes[i]


print(new_list)


# file=open("./excel.json","w+")
# file.write(json.dumps(new_list))
