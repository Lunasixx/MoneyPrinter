from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(response):
    return render(response,"printer/main.html", {})
