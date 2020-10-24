import urllib.request
import bs4
import pandas
import json


h={'User-Agent':'Mozilla/5.0'}

def search_company(company_code):
    url="https://kr.investing.com/search/?q="+company_code
    req=urllib.request.Request(url,headers=h)
    html=urllib.request.urlopen(req)
    bs_obj=bs4.BeautifulSoup(html,"html.parser")
    first_a=bs_obj.find("a",{"class":"js-inner-all-results-quote-item row"}).get('href') #.get(href)를 통해 아래 결과에서 href 추출
    return first_a


def data_list(company_code):
    second_url="https://kr.investing.com"+search_company(company_code)+"-financial-summary"
    second_req=urllib.request.Request(second_url,headers=h)
    second_html=urllib.request.urlopen(second_req)
    second_bs_obj=bs4.BeautifulSoup(second_html,"html.parser")
    first_table=second_bs_obj.find("table",{"class":"genTbl openTbl companyFinancialSummaryTbl"})
    first_table_date=first_table.findAll("th") #날짜 데이터
    first_table_tbody = first_table.find("tbody") # 재무 데이터 시작
    items_list = first_table_tbody.findAll("tr") #총수익, 총이익 등 항목 고르기
    total_revenue_list=items_list[0].findAll("td")
    gross_profit_list=items_list[1].findAll("td")
    operating_income_list=items_list[2].findAll("td")
    net_income_list=items_list[3].findAll("td")

    fiscal_time=["Symbol"]
    total_revenue=[company_code]
    gross_profit=[company_code]
    operating_income=[company_code]
    net_income=[company_code]
    json_revenue = {}
    json_gross_profit = {}
    json_operating_income = {}
    json_net_income = {}
    excel_list = []

    for number in range(5):
        fiscal_time_data=first_table_date[number].text
        total_revenue_data=total_revenue_list[number].text
        gross_profit_data = gross_profit_list[number].text
        operating_income_data=operating_income_list[number].text
        net_income_data=net_income_list[number].text
        fiscal_time.append(fiscal_time_data)
        total_revenue.append(total_revenue_data)
        gross_profit.append(gross_profit_data)
        operating_income.append(operating_income_data)
        net_income.append(net_income_data)

    for i in range(6):
        json_revenue[fiscal_time[i]]=total_revenue[i]
        json_gross_profit[fiscal_time[i]]=gross_profit[i]
        json_operating_income[fiscal_time[i]]=operating_income[i]
        json_net_income[fiscal_time[i]]=net_income[i]

    excel_list.append(json_revenue)
    excel_list.append(json_gross_profit)
    excel_list.append(json_operating_income)
    excel_list.append(json_net_income)
    return excel_list

company_codes="PLD"
list1=data_list(company_codes)

print(list1)




