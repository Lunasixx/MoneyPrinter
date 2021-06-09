from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from printer.CoingeckoInterface import GeckoInterface

# Create your views here.

async def index(response,contract=""):
    x = GeckoInterface("eur")
    y = await x.status_updates()
    print(y)
    return render(response,"printer/main.html", {"y":y})
