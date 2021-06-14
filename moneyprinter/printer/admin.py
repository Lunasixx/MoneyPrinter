from django.contrib import admin
from .models import Coin, Prices
#  Register your models here.
admin.site.register(Coin)
admin.site.register(Prices)