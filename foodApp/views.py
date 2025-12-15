from django.shortcuts import render
from .models import Food

# Create your views here.

def food_gallery(request):
    """美食地图/图鉴 - 瀑布流展示"""
    foods = Food.objects.all().order_by('-created_at')
    return render(request, 'food/gallery.html', {'foods': foods})
