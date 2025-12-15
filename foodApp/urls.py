from django.urls import path
from . import views

app_name = 'foodApp'

urlpatterns = [
    path('gallery/', views.food_gallery, name='food_gallery'),  # 美食地图/图鉴
]