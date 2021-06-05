import requests
import json
import asyncio

class GeckoInterface:
    #value used through out api-calls //up to setting
    currency=None

    def __init__(self,currency):
        self.currency = currency

    async def change_currency(self, currency):
        self.currency = currency

    #makes actual request, takes whatever url and return json
    async def request(self,url):
        r = requests.get(url)
        if r.status_code==200:
            return r.json()
        else:
            return "none"

    #=====================PING-SECTION============================
    #check server availability
    async def ping_gecko(self, url):
        return await self.request("https://api.coingecko.com/api/v3/ping")


    #====================SIMPLE-SECTION===========================
    #current price of given id compared to currency (coins)
    async def simple_price(self, id):
        return await self.request(f"https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies={self.currency}&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")

    #given platform (e.G. binance-smart-chain) & contract-adresse (0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82) -returns current price
    async def simple_token_price(self,platform,contract):
        return await self.request(f"https://api.coingecko.com/api/v3/simple/token_price/{platform}?contract_addresses={contract}&vs_currencies={self.currency}")

    #returns list of all supported currencies to compare against
    async def simple_supported_vs_currencies(self):
        return await self.request(f"https://api.coingecko.com/api/v3/simple/supported_vs_currencies")


    #====================COINS-SECTION============================
    #returns all coins + id,symbol,name,platforms
    async def coins_list(self):
        return await self.request("https://api.coingecko.com/api/v3/coins/list?include_platform=true")

    #given an array of one/multiple coin-ids -returns coin/token specific values
    async def coins_markets(self,ids=[],filter="",timespan="24h"):
        qstring=""
        for id in ids:
            qstring +=id + ","
        qstring = qstring[:-1]
        return await self.request(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={self.currency}&ids={qstring}&order={filter}&per_page=250&page=1&sparkline=false&price_change_percentage={timespan}")

    #given the id - returns social data of certain coin/token
    async def coins(self,id,ticker_data=False,market_data=False,community_data=True,developer_data=True,sparkline_data=False):
        return await self.request(f"https://api.coingecko.com/api/v3/coins/{id}?localization=false&tickers={ticker_data}&market_data={market_data}&community_data={community_data}&developer_data={developer_data}&sparkline={sparkline_data}")

    #given id and days- returns chart data of past x days /default=7
    async def coins_market_chart(self, id, days="7"):
        return await self.request(f"https://api.coingecko.com/api/v3/coins/{id}/market_chart?vs_currency={self.currency}&days={days}")

    #given an id and a two unix timestamps fromtime to totime - returns chart data from timespan
    async def coins_market_chart_range(self, id, currency, fromtime, totime):
        return await self.request(f"https://api.coingecko.com/api/v3/coins/{id}/market_chart/range?vs_currency={self.currency}&from={fromtime}&to={totime}")

    #given an id returns status upda
    async def coins_status_updates(self, id):
        return await self.request(f"https://api.coingecko.com/api/v3/coins/{id}/status_updates")

    #given id and days, returns ohcl data
    async def coins_ohcl(self,id,days="7"):
        return await self.request(f"https://api.coingecko.com/api/v3/coins/{id}/ohlc?vs_currency={self.currency}&days={days}")

    #==========================ASSET_PLATFORMS CATEGORY=========================
    #returns asset platforms
    async def asset_platforms(self):
        return await self.request(f"https://api.coingecko.com/api/v3/asset_platforms")

    #==========================CATEGORIES CATEGORY==============================
    #returns list of categories
    async def categories_list(self):
        return await self.request(f"https://api.coingecko.com/api/v3/coins/categories/list")

    #=========================EXCHANGES CATEGORYS================================
    #returns all exchanges
    async def exchanges(self):
        return await self.request("https://api.coingecko.com/api/v3/exchanges?per_page=250&page=1")

    #returns all exchanges
    #use this to obtain ids of exchanges
    async def exchanges_list(self):
        return await self.request("https://api.coingecko.com/api/v3/exchanges/list")

    #given an exchange id (from exchanges_list) returns exchange volume in btc and tickers max 100
    async def exchanges_id(self,id):
        return await self.request(f"https://api.coingecko.com/api/v3/exchanges/{id}")

    #given an exchange id returns exchange tickers (filter by coin id e.G. aave, bitcoin,)
    async def exchanges_id_tickers(self,id,filterbycoin=""):
        return await self.request(f"https://api.coingecko.com/api/v3/exchanges/{id}/tickers?coin_ids={filterbycoin}&include_exchange_logo=true&page=1&depth=true&order=true")

    #given an exchange and a timespan returns volume chart data of exchange
    async def exchanges_id_volume_chart(self,id,days="7"):
        return await self.request(f"https://api.coingecko.com/api/v3/exchanges/{id}/volume_chart?days={days}")

    #============================FINANCE CATEGORY=============================================
    #returns finance platforms
    async def finance_platforms(self):
        return await self.request(f"https://api.coingecko.com/api/v3/finance_products")

    #returns finance products
    async def finance_products(self):
        return await self.request(f"https://api.coingecko.com/api/v3/finance_products")

    #=========================STATUS UPDATES CATEGORY==========================================
    #returns status updates
    async def status_updates(self):
        return await self.request("https://api.coingecko.com/api/v3/status_updates")

    #=========================TRENDING CATEGORY====================================
    #returns TOP-7 trending coins searched by user on coingecko in past 24 hours
    async def search_trending(self):
        return await self.request("https://api.coingecko.com/api/v3/search/trending")


