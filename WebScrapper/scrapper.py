import requests
import selenium 
date="14 July 2020"
url="https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Tamil_Nadu#covid19-container"
data=requests.get(url)
capturedData=data.text.split("The data below are based on Health and Family Welfare Department of Tamil Nadu daily reports.")[1].split(">By cluster<")[0]
capturedData2=capturedData.split(date)
print(capturedData2[0])