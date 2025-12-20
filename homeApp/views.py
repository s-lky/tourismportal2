from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm
from .models import UserProfile

# Create your views here.
def home(request):
    """首页"""
    from attractionsApp.models import Attraction
    from foodApp.models import Food
    from tripPlanApp.models import TripPlan
    # 显示最新的6个景点
    featured_attractions = Attraction.objects.all()[:6]
    # 显示最新的3个美食
    featured_foods = Food.objects.all()[:3]
    # 显示最新的3个攻略
    featured_plans = TripPlan.objects.all()[:3]
    return render(request, 'home/index.html', {
        'featured_attractions': featured_attractions,
        'featured_foods': featured_foods,
        'featured_plans': featured_plans,
    })

def user_login(request):
    """用户登录"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('home')
        else:
            messages.error(request, '用户名或密码错误')
    
    return render(request, 'home/login.html')

def user_register(request):
    """用户注册"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 自动登录
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'home/register.html', {'form': form})

def user_logout(request):
    """用户退出"""
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')


@login_required
def user_profile(request):
    """用户中心 - 显示和编辑用户资料"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('homeApp:user_profile')
        else:
            messages.error(request, '请检查表单输入')
    else:
        form = UserProfileForm(instance=profile, user=request.user)
    
    return render(request, 'home/profile.html', {
        'form': form,
        'profile': profile
    })