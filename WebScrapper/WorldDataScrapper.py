import pandas as pd 
import json
import requests as req

url="https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search"

res=json.loads(req.get(url).text)
resData=res["data"]["rows"]
totalPages=res["data"]["paginationMeta"]["totalPages"]

for page in range(2,totalPages):
    paramUrl=url+"?page"+str(page)
    resData+=json.loads(req.get(url).text)["data"]["rows"]

jsonData=json.dumps(resData)
path=r"C:\Users\Deepak\Documents\GitHub\PythonDataAnalyticsCorona\CollectedData\WorldCoronaCount.csv"
worldData=pd.read_json(jsonData)
worldData.drop(["flag"],axis=1,inplace=True)
print(worldData)
worldData.to_csv(path)

