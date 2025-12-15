from django.urls import path
from . import views

app_name = 'attractionsApp'

urlpatterns = [
    path('attraction_list/', views.AttractionListView.as_view(), name='attraction_list'),  # 景点总览页 - 使用ListView
    path('detail/<int:attraction_id>/', views.attraction_detail, name='attraction_detail'),  # 景点详情页
]