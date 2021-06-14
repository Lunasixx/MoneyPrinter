from django.db import models
from datetime import datetime


class Prices(models.Model):
    
    currency = models.CharField(max_length=50,blank=True, null=True)
    currentprice = models.FloatField(blank=True, null=True)
    market_cap = models.BigIntegerField(blank=True, null=True)
    twentyfour_hour_vol = models.BigIntegerField(blank=True, null=True)
    twentyfour_hour_change = models.BigIntegerField(blank=True, null=True)
    last_updated_at = models.DateTimeField(default=datetime(1994,3,14,0,0,0))


class Coin(models.Model):
    coin = models.CharField(max_length=255,blank=True, null=True)
    symbol = models.CharField(max_length=50,blank=True, null=True)
    name = models.CharField(max_length=255,blank=True, null=True)
    platform1 = models.CharField(max_length=50,blank=True, null=True)
    platform2 = models.CharField(max_length=50,blank=True, null=True)
    platform3 = models.CharField(max_length=50,blank=True, null=True)
    contract1 = models.CharField(max_length=32,blank=True, null=True)
    contract2 = models.CharField(max_length=32,blank=True, null=True)
    contract3 = models.CharField(max_length=32,blank=True, null=True)
    prices_eur = models.ForeignKey(Prices,related_name="prices_eur", on_delete=models.CASCADE,blank=True, null=True)
    prices_usd = models.ForeignKey(Prices,related_name="prices_usd", on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return str(self.name)
