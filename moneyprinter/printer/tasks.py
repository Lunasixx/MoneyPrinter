import requests
from celery import shared_task
from .celery import app
from .models import Coin 

@shared_task
def get_coins():
    r = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if r.status_code==200:
        
        x = r.json()
        
        
        for coin in x:
            try:
                dbobjects = Coin.objects.filter(coin=coin['id'])
                if not dbobjects:
                    newcoin, created = Coin.objects.get_or_create(coin=coin['id'])
                    newcoin.symbol=coin["symbol"]
                    newcoin.name=coin["name"]
                    i = 0
                    for key in coin["platforms"]:
                        if i == 0:
                            newcoin.platform1 = key
                            newcoin.contract1 = coin["platforms"][key]
                        elif i == 1:
                            newcoin.platform2 = key
                            newcoin.contract2 = coin["platforms"][key]
                        elif i == 2:
                            newcoin.platform3 = key
                            newcoin.contract3 = coin["platforms"][key]
                        elif i == 3:
                            pass
                        i+=1
                    newcoin.save()
            except Exception as e:
                print(coin)
                print(e)

