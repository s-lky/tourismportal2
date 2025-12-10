from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    html = '<html><nody>首页</doby></html>'
    return HttpResponse(html)