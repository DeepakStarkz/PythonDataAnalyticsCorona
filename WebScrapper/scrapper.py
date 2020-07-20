import requests
import pandas as pd 
date="14 July 2020"
url="https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Tamil_Nadu#covid19-container"
data=requests.get(url)
capturedData=data.text.split("The data below are based on Health and Family Welfare Department of Tamil Nadu daily reports.")[1].split(">By cluster<")[0]
capturedData2=capturedData.split(date)[1:37]
cleanedData=[cd.split("<td>") for cd in capturedData2]
cleanedData2=[[cd2.replace("\n</td>\n",'') for cd2 in cd] for cd in cleanedData ]
for  cd in cleanedData2:
    for i in range(len(cd)):
     if i==0:
         try:
          cd[i]=cd[i].split("district\">")[1].split("</a>")[0]
         except:
          cd[i]=cd[i].split("District\">")[1].split("</a>")[0] 
     if i==5:
         cd[i]=cd[i].split("\">")[1].split("</span>")[0]
     if i==7:
         cd.pop(i)


coronaData=pd.DataFrame(cleanedData2)
coronaData.columns=["District","DiagonisedCases","Deaths","RecoveredCases","ActiveCases","Population","CasesPerMillion"]
coronaData.set_index("District",inplace=True)
path=r"C:\Users\Deepak\Documents\GitHub\PythonDataAnalyticsCorona\CollectedData\TNCoronaCount.csv"
coronaData.to_csv(path)        
    
     
         
     