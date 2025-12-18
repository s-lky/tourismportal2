"""tourismportal2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from homeApp.views import home, user_login, user_register, user_logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('homeApp/', include('homeApp.urls')),
    path('attractionsApp/', include('attractionsApp.urls')),
    path('bookingApp/', include('bookingApp.urls')),
    path('favoritesApp/', include('favoritesApp.urls')),
    path('tripPlanApp/', include('tripPlanApp.urls')),
    path('foodApp/', include('foodApp.urls')),  # 寻味岭南美食模块
]
#让Django在开发模式可以找到在后台上传的图片
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
