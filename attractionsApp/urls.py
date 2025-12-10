from django.urls import path
from . import views

app_name = 'attractionsApp'

urlpatterns = [
    path('func3',views.func3,name = 'func3'),    #功能3
    path('func4',views.func4,name = 'func4'),    #功能4

]