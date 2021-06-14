from .crud import CRUD
from .CoingeckoInterface import GeckoInterface
from datetime import datetime , timedelta
from asgiref.sync import sync_to_async
from django.utils import timezone

class Session:

    Gecko = None

    def __init__(self,currency="eur"):
        global Gecko
        Gecko = GeckoInterface(currency)

    async def get_current_price(self,coinid,currency):
        fmt = '%Y-%m-%d %H:%M:%S:%f'
        currentprice = await CRUD.get_current_price_by_id(coinid,currency)
        print(currentprice.last_updated_at)
        print(datetime.now())
        lastupdate = datetime.strftime(currentprice.last_updated_at, fmt)
        now = datetime.strftime(datetime.now(), fmt)
        if lastupdate < now:
            price = await Gecko.simple_price(coinid)
            currentprice.last_updated_at = datetime.now(tz=timezone.utc) + timedelta(seconds=10)
            currentprice.currentprice = price[coinid][currency]
            currentprice.market_cap = price[coinid][currency+"_market_cap"]
            currentprice.twentyfour_hour_vol = price[coinid][currency+"_24h_vol"]
            currentprice.twentyfour_hour_change = price[coinid][currency+"_24h_change"]
            await self.save_obj(currentprice)
            return currentprice
        else:
            return currentprice

    @sync_to_async()
    def save_obj(self,obj):
        obj.save()

    async def initialize(self,contract):
        global Coin
        coins = list(await CRUD.get_coin_by_contract(contract))
        coin = coins[0]
        return coin

    async def create_view_model(self,Coin):
        price = await self.get_current_price(Coin.coinid)
        return price


   

