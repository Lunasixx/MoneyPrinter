from webbrowser import get

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render


from printer.CoingeckoInterface import GeckoInterface

from .models import Coin
from .session import Session

# Create your views here.
session = None

async def index(response,contract="0x111111111117dc0aa78b770fa6a738034120c302",coinid="wbnb"):
        global session
        session = Session("eur")
        coin  = await session.initialize(contract)
        return render(response,"printer/main.html",context={"coin":coin})

#             currency = models.CharField(max_length=50,blank=True, null=True)
#     currentprice = models.FloatField(blank=True, null=True)
#     market_cap = models.BigIntegerField(blank=True, null=True)
#     twentyfour_hour_vol = models.BigIntegerField(blank=True, null=True)
#     twentyfour_hour_change = models.BigIntegerField(blank=True, null=True)
#     last_updated_at = models.DateTimeField(auto_now_add=True)

async def getprice(response):
        price =  await session.get_current_price(response.GET.get("coin"),response.GET.get("currency"))
        return JsonResponse({"currentprice": price.currentprice, "marketcap": price.market_cap, "twentyfour_hour_vol": price.twentyfour_hour_vol, "twentyfour_hour_change" : price.twentyfour_hour_change, "last_updated_at":price.last_updated_at})
