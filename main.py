import requests
import json
from bs4 import BeautifulSoup

bankStocks = ['TD.TO','BNS.TO','BMO.TO']
stockData=[]

def getData(symbol):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers = headers)
    soup=BeautifulSoup(r.text, 'html.parser')
    stock={

    'symbol' : symbol,
    'price' : soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
    'change' : soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    'changePercentage' : soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text,
    }
    return stock

for item in bankStocks:
    stockData.append(getData(item))
    print('Getting: ',item)

with open('stockData.json','w') as f:
    json.dump(stockData, f)

print('Fin')