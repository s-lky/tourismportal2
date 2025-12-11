from django.urls import path
from . import views

app_name = 'attractionsApp'

urlpatterns = [
    path('attraction_list/',views.attraction_list,name = 'attraction_list'),    #功能3

]