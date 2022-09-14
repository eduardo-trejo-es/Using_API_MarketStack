#webSite: https://marketstack.com/ 

#note maybe I need to get the one month plan to see if the intraday works as I need it


import requests

import pandas as pd

from pathlib import Path




#for stock_data in api_response['data']:
# print(u'Ticker %s has a day high of  %s on %s' % (stock_data['symbol'], stock_data['high'],stock_data['date']))


def SavingDataPrices(From, to,csvFileName):
  
  HistoricalPriceRequests="http://api.marketstack.com/v1/intraday?symbols=TWTR&date_from={}&date_to={}".format(From,to)
  
  params = {
    'access_key': 'bfaf26d006f1243f13038efdfbe04ac5'
  }
  #'http://api.marketstack.com/v1/intraday?symbols=TWTR&interval=1hour&date_from=2022-09-12 13:00:00&date_to=2022-09-13 13:00:00'
  #date_format: 2022-09-13T00:00:00+0000
  #url='http://api.marketstack.com/v1/tickers/aapl/eod'
  

  api_result = requests.get(HistoricalPriceRequests, params)

  api_response = api_result.json()



  #conn.request("GET", "/api/v1/prices/TWTR?resolution=MINUTE_10&max=10&from=2022-02-24T00:00:00&to=2022-02-24T01:00:00", payload, headers)
  #print(api_response)
  try:
    for i in api_response['data']:
      print(i)
  except:
    print(api_response)
  #####      Saving Data In CSV file   ####

  columnsNames=["openPrice","closePrice","highPrice","lowPrice","lastTradedVolume"]
  DateIndexName=[]
  columnsValues=[]
  DataGrouped=[]
  for i in api_response['data']:
      DateIndexName.append(i["date"])
      columnsValues.append(i["open"])
      columnsValues.append(i["high"])
      columnsValues.append(i["low"])
      columnsValues.append(i["close"])
      columnsValues.append(i["volume"])
      DataGrouped.append(columnsValues)
      columnsValues=[]

  df = pd.DataFrame(DataGrouped,index=DateIndexName, columns=columnsNames)
  
  try:
      existing=pd.read_csv(csvFileName, index_col="Unnamed: 0")
      #print(existing)
      #print(type(existing))
      existing = existing.append(df)
      print("was try")
      print(existing)
      existing.to_csv(path_or_buf=csvFileName,index=True)
      
  except :
      print("was execpt")
      df.to_csv(path_or_buf=csvFileName,index=True)

SavingDataPrices("2022-08-01 13:00:00", "2022-08-29 00:00:00","TestingDataCSV.csv")