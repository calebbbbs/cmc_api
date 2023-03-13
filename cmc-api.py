import requests
from requests import Session
import secrets_1
from pprint import pprint as pp

url = "https://pro-api.coinmarketcap.com"

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': secrets_1.API_KEY,
}
r = requests.get(url, headers=headers)


class CMC:

    def __init__(self, token):
        self.apiurl = url
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': token,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def getAllCoins(self):
        url = self.apiurl + "/v1/cryptocurrency/map"
        r = self.session.get(url)
        data = r.json()['data']
        return data

    def getId(self, symbol):
        url = self.apiurl + "/v1/cryptocurrency/map"
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)
        id = r.json()['data'][0]['id']
        return id

    def getPrice(self, symbol):
        url = self.apiurl + "/v2/cryptocurrency/quotes/latest"
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()['data'][symbol][0]["quote"]['USD']['price']
        pricedict = {}
        amt = '${}'
        pricedict[symbol] = amt.format(int(data))
        return pricedict

    def getLatestListingPrices(self):
        url = self.apiurl + "/v1/cryptocurrency/listings/latest"
        r = self.session.get(url)
        data = r.json()['data']
        thisdict = {}
        for x in data:
            amt = '${}'
            thisdict[x['name']] = amt.format(int(x['quote']['USD']['price']))
        return thisdict

    def getMarketCap(self, symbol):
        url = self.apiurl + "/v2/cryptocurrency/quotes/latest"
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)
        marketCapDict = {}
        data = r.json()['data'][symbol][0]['quote']['USD']['market_cap']
        marketCapDict[symbol] = f'{int(data):,}'
        return marketCapDict

    def get90DayMove(self, symbol):
        url = self.apiurl + "/v2/cryptocurrency/quotes/latest"
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)
        percentdict = {}
        percent = '{}%'
        data = r.json(
        )['data'][symbol][0]['quote']['USD']['percent_change_90d']
        percentdict[symbol] = percent.format(f'{int(data):,}')
        return percentdict


cmc = CMC(secrets_1.API_KEY)

# pp(cmc.getAllCoins())
# pp(cmc.getID('BTC'))
# pp(cmc.getPrice('ETH'))
# pp(cmc.getLatestListingPrices())
# pp(cmc.getMarketCap('BTC'))
pp(cmc.get90DayMove('ETH'))