from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TripPlan
from .forms import TripPlanForm

# Create your views here.
def trip_plan_list(request):
    """攻略列表"""
    trip_plans = TripPlan.objects.all().order_by('-created_at')
    return render(request, 'tripPlan/list.html', {'trip_plans': trip_plans})

def trip_plan_detail(request, plan_id):
    """攻略详情"""
    plan = get_object_or_404(TripPlan, id=plan_id)
    return render(request, 'tripPlan/detail.html', {'plan': plan})

@login_required
def create_trip_plan(request):
    """创建攻略"""
    if request.method == 'POST':
        form = TripPlanForm(request.POST, request.FILES)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            messages.success(request, '攻略发布成功！')
            return redirect('tripPlanApp:trip_plan_detail', plan_id=plan.id)
    else:
        form = TripPlanForm()
    
    return render(request, 'tripPlan/create.html', {'form': form})

@login_required
def my_trip_plans(request):
    """我的攻略"""
    trip_plans = TripPlan.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tripPlan/my_plans.html', {'trip_plans': trip_plans})