#webSite: https://marketstack.com/ 

#note maybe I need to get the one month plan to see if the intraday works as I need it


import requests

params = {
  'access_key': 'bfaf26d006f1243f13038efdfbe04ac5'
}

#urls:http://api.marketstack.com/v1/tickers/aapl/eod
#'http://api.marketstack.com/v1/tickers/TWTR?/eod&date_from=2022-02-24&date_to=2022-02-25'

api_result = requests.get('http://api.marketstack.com/v1/tickers/TWTR/eod', params)

api_response = api_result.json()



#conn.request("GET", "/api/v1/prices/TWTR?resolution=MINUTE_10&max=10&from=2022-02-24T00:00:00&to=2022-02-24T01:00:00", payload, headers)

print(api_response['data']['eod'])
#for stock_data in api_response['data']:
# print(u'Ticker %s has a day high of  %s on %s' % (stock_data['symbol'], stock_data['high'],stock_data['date']))
