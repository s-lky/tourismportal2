from django.urls import path
from . import views

app_name = 'bookingApp'

urlpatterns = [
    path('create/<int:attraction_id>/', views.create_booking, name='create_booking'),  # 创建预订
    path('my_bookings/', views.my_bookings, name='my_bookings'),  # 我的订单
    path('detail/<int:booking_id>/', views.booking_detail, name='booking_detail'),  # 订单详情
]