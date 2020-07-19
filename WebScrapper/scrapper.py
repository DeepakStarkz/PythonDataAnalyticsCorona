import requests
import selenium 

url="https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Tamil_Nadu#covid19-container"
data=requests.get(url)
capturedData=data.split("By_district")[1]
print(capturedData)