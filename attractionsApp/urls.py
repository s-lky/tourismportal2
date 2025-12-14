from django.urls import path
from . import views

app_name = 'attractionsApp'

urlpatterns = [
    path('attraction_list/',views.attraction_list,name = 'attraction_list'),    #功能3
    path('detail/<int:attraction_id>/', views.attraction_detail, name='attraction_detail'),  # 景点详情页
]