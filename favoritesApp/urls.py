from django.urls import path
from . import views

app_name = 'favoritesApp'

urlpatterns = [
    path('func5',views.func5,name = 'func5'),    #二级网页功能5
    path('func6',views.func6,name = 'func6'),    #二级网页功能6

]