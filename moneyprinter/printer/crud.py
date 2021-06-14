import time

from asgiref.sync import sync_to_async



from .models import Coin, Prices


class CRUD():

    @sync_to_async()
    def get_coin_by_contract(self,contract):
        result =   list(Coin.objects.filter(contract1=contract) | Coin.objects.filter(contract2=contract) |  Coin.objects.filter(contract3=contract))
        return result


    @sync_to_async()
    def get_coin_by_id(self,coinid):
        result =   list(Coin.objects.filter(coin=coinid))
        return result





    @sync_to_async()
    def get_current_price_by_id(self,id,currency):
        #get querey set
        if currency=="eur":
            set = Coin.objects.filter(coin=id).prefetch_related("prices_eur")
        else:
            set = Coin.objects.filter(coin=id).prefetch_related("prices_usd")

        result = list(set)

        if currency == "eur":
            if result[0].prices_eur == None:
                price = Prices(currency="eur")
                price.save()
                set.update(prices_eur = price)
                result = list(set)
                return result[0]
            else:
                coin = result[0]
                return coin.prices_eur
                
        elif currency == "usd":
            if result[0].prices_usd == None:
                price = Prices(currency="usd")
                price.save()
                set.update(prices_usd = price)
                result = list(set)
                return result[0]
            else:
                coin = result[0]
                return coin.prices_usd
        else:
            return None
        
       
        

    
