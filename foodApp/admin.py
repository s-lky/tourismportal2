from django.contrib import admin
from .models import Food, FoodRecommendation


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    """美食管理"""
    list_display = ('name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'image', 'description')
        }),
        ('推荐信息', {
            'fields': ('rating',)
        }),
        ('时间信息', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(FoodRecommendation)
class FoodRecommendationAdmin(admin.ModelAdmin):
    """美食推荐管理"""
    list_display = ('food_name', 'user', 'location', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('food_name', 'location', 'reason', 'user__username')
    readonly_fields = ('user', 'created_at', 'updated_at')
    fieldsets = (
        ('推荐信息', {
            'fields': ('user', 'food_name', 'location', 'reason')
        }),
        ('审核信息', {
            'fields': ('status',)
        }),
        ('时间信息', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """保存时自动设置用户（如果是新建）"""
        if not change:  # 新建时
            obj.user = request.user
        super().save_model(request, obj, form, change)
