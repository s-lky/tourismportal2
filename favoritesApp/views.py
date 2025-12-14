from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Favorite
from attractionsApp.models import Attraction

# Create your views here.
@login_required
def toggle_favorite(request, attraction_id):
    """切换收藏状态"""
    attraction = get_object_or_404(Attraction, id=attraction_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, attraction=attraction)
    
    if not created:
        # 如果已存在，则取消收藏
        favorite.delete()
        messages.success(request, '已取消收藏')
    else:
        messages.success(request, '收藏成功')
    
    return redirect('attractionsApp:attraction_detail', attraction_id=attraction_id)

@login_required
def my_favorites(request):
    """我的收藏列表"""
    favorites = Favorite.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'favorites/list.html', {'favorites': favorites})