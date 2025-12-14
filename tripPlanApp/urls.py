from django.urls import path
from . import views

app_name = 'tripPlanApp'

urlpatterns = [
    path('', views.trip_plan_list, name='trip_plan_list'),  # 攻略列表
    path('detail/<int:plan_id>/', views.trip_plan_detail, name='trip_plan_detail'),  # 攻略详情
    path('create/', views.create_trip_plan, name='create_trip_plan'),  # 创建攻略
    path('my_plans/', views.my_trip_plans, name='my_trip_plans'),  # 我的攻略
]