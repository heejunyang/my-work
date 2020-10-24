import pandas as pd
import json
import openpyxl
import numpy

json_data={"항목":"총수익","name":"APPLE","TICKER":"APPL","기간1":"1월","기간2":"2월","기간3":"3월","기간4":"4월"}
json_data2={"항목":"총수익","name":"블리자드","TICKER":"ATVI","기간1":"8월","기간2":"5월","기간3":"7월","기간4":"10월"}
list=[json_data,json_data2]
file=open("./json_test.json","w+")
file.write(json.dumps(list))

