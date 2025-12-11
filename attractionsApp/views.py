from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Attraction
# Create your views here.

def attraction_list(request):
    # 获取所有景点数据
    attractions = Attraction.objects.all()
    # 把数据打包成字典传给模板，键名叫 'attractions'
    return render(request, 'attractions/list.html', {'attractions': attractions})
