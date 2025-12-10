from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def func7(request):
    html = '<html><nody>功能7</doby></html>'
    return HttpResponse(html)
def func8(request):
    html = '<html><nody>功能8</doby></html>'
    return HttpResponse(html)