import pandas as pd

df=pd.read_json("excel.json")

writer=pd.ExcelWriter("excel.xlsx")
df.to_excel(writer,"sheet1")
writer.save()
