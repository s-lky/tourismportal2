from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def func5(request):
    html = '<html><nody>功能5</doby></html>'
    return HttpResponse(html)
def func6(request):
    html = '<html><nody>功能6</doby></html>'
    return HttpResponse(html)