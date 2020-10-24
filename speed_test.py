import urllib.request
import bs4

h={"User-Agent":"Mozilla/5.0"}

url="https://www.investing.com/"
req=urllib.request.Request(url,headers=h)
html=urllib.request.urlopen(req)
bs_obj=bs4.BeautifulSoup(html,"html.parser")

print(bs_obj)