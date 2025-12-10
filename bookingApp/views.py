from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def func1(request):
    html = '<html><nody>功能1</doby></html>'
    return HttpResponse(html)
def func2(request):
    html = '<html><nody>功能2</doby></html>'
    return HttpResponse(html)