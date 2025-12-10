from django.urls import path
from . import views

app_name = 'bookingApp'

urlpatterns = [
    path('func1',views.func1,name = 'func1'),    #booking的二级网页功能1
    path('func2',views.func2,name = 'func2'),    #booking的二级网页功能2

]