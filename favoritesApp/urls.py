from django.urls import path
from . import views

app_name = 'favoritesApp'

urlpatterns = [
    path('toggle/<int:attraction_id>/', views.toggle_favorite, name='toggle_favorite'),  # 切换收藏
    path('my_favorites/', views.my_favorites, name='my_favorites'),  # 我的收藏
]