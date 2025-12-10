from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def func3(request):
    html = '<html><nody>功能3</doby></html>'
    return HttpResponse(html)
def func4(request):
    html = '<html><nody>功能4</doby></html>'
    return HttpResponse(html)