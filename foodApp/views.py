from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from .models import Food, FoodRecommendation
from .forms import FoodRecommendationForm

# Create your views here.

def food_gallery(request):
    """美食地图/图鉴 - 瀑布流展示"""
    foods = Food.objects.all().order_by('-created_at')
    return render(request, 'food/gallery.html', {'foods': foods})

@login_required
def food_recommend(request):
    """美食投稿/推荐 - 表单提交"""
    if request.method == 'POST':
        form = FoodRecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.user = request.user
            recommendation.status = 'pending'  # 默认为待审核状态
            recommendation.save()
            messages.success(request, '感谢您的推荐！我们会尽快审核您的投稿。')
            return redirect('foodApp:recommendation_list')
    else:
        form = FoodRecommendationForm()
    
    return render(request, 'food/recommend_form.html', {'form': form})

class RecommendationListView(ListView):
    """美食推荐列表 - 查看所有推荐"""
    model = FoodRecommendation
    template_name = 'food/recommendation_list.html'
    context_object_name = 'recommendations'
    paginate_by = 10
    
    def get_queryset(self):
        """获取推荐列表，优先显示已通过的"""
        queryset = FoodRecommendation.objects.all()
        
        # 如果用户已登录，可以查看自己的所有推荐
        if self.request.user.is_authenticated:
            # 管理员可以看到所有，普通用户只能看到已通过的
            if not self.request.user.is_staff:
                queryset = queryset.filter(status='approved')
        else:
            # 未登录用户只能看到已通过的
            queryset = queryset.filter(status='approved')
        
        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        """添加上下文数据"""
        context = super().get_context_data(**kwargs)
        # 统计信息
        context['total_count'] = FoodRecommendation.objects.count()
        context['approved_count'] = FoodRecommendation.objects.filter(status='approved').count()
        if self.request.user.is_authenticated:
            context['my_count'] = FoodRecommendation.objects.filter(user=self.request.user).count()
        return context
