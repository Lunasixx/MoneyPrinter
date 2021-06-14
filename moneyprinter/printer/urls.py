from django.contrib import admin
from django.urls import path
from printer import views as v


urlpatterns = [
    path('getprice/', v.getPrice),
]