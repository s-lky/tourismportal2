from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Attraction

# Create your views here.

class AttractionListView(ListView):
    """景点总览页 - 使用ListView类视图"""
    model = Attraction
    template_name = 'attractions/list.html'
    context_object_name = 'attractions'
    paginate_by = 12  # 每页显示12个景点
    
    def get_queryset(self):
        """重写queryset方法，实现搜索和筛选功能"""
        queryset = Attraction.objects.all()
        
        # 搜索功能：按名字搜索
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        
        # 筛选功能：按城市筛选
        city = self.request.GET.get('city', '')
        if city:
            queryset = queryset.filter(city=city)
        
        # 筛选功能：按类型筛选
        attraction_type = self.request.GET.get('type', '')
        if attraction_type:
            queryset = queryset.filter(attraction_type=attraction_type)
        
        # 按区域筛选（保留原有功能）
        region = self.request.GET.get('region', '')
        if region:
            queryset = queryset.filter(region=region)
        
        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        """添加上下文数据，包括筛选选项的当前值"""
        context = super().get_context_data(**kwargs)
        context['current_search'] = self.request.GET.get('search', '')
        context['current_city'] = self.request.GET.get('city', '')
        context['current_type'] = self.request.GET.get('type', '')
        context['current_region'] = self.request.GET.get('region', '')
        # 传递选项数据供模板使用
        context['city_choices'] = Attraction.CITY_CHOICES
        context['type_choices'] = Attraction.TYPE_CHOICES
        return context

def attraction_detail(request, attraction_id):
    # 获取景点详情，如果不存在则返回404
    attraction = get_object_or_404(Attraction, id=attraction_id)
    # 检查用户是否已收藏
    is_favorited = False
    if request.user.is_authenticated:
        from favoritesApp.models import Favorite
        is_favorited = Favorite.objects.filter(user=request.user, attraction=attraction).exists()
    
    return render(request, 'attractions/detail.html', {
        'attraction': attraction,
        'is_favorited': is_favorited
    })
