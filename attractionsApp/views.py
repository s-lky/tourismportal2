from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Attraction
# Create your views here.

def attraction_list(request):
    # 获取所有景点数据
    attractions = Attraction.objects.all()
    # 支持按区域筛选
    region = request.GET.get('region')
    if region:
        attractions = attractions.filter(region=region)
    # 把数据打包成字典传给模板，键名叫 'attractions'
    return render(request, 'attractions/list.html', {'attractions': attractions, 'current_region': region})

def attraction_detail(request, attraction_id):
    # 获取景点详情，如果不存在则返回404
    attraction = get_object_or_404(Attraction, id=attraction_id)
    # 检查用户是否已收藏
    is_favorited = False
    if request.user.is_authenticated:
        from favoritesApp.models import Favorite
        is_favorited = Favorite.objects.filter(user=request.user, attraction=attraction).exists()
    
    return render(request, 'attractions/detail.html', {
        'attraction': attraction,
        'is_favorited': is_favorited
    })
