from django.urls import path
from . import views

app_name = 'foodApp'

urlpatterns = [
    path('gallery/', views.food_gallery, name='food_gallery'),  # 美食地图/图鉴
    path('recommend/', views.food_recommend, name='food_recommend'),  # 美食投稿/推荐
    path('recommendations/', views.RecommendationListView.as_view(), name='recommendation_list'),  # 推荐列表
]