from django.urls import path
from . import views

app_name = 'tripPlanApp'

urlpatterns = [
    path('func7',views.func7,name = 'func7'),    #二级网页功能7
    path('func8',views.func8,name = 'func8'),    #二级网页功能8

]