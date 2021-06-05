from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from printer.CoingeckoInterface import GeckoInterface

# Create your views here.

def index(response):
    x = GeckoInterface()
    return render(response,"printer/main.html", {})
