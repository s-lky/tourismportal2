from django.contrib import admin
from .models import Attraction, AttractionImage, AttractionLike


class AttractionImageInline(admin.TabularInline):
    """内联显示景点图片"""
    model = AttractionImage
    extra = 1


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'attraction_type', 'region', 'price', 'view_count', 'like_count', 'created_at')
    list_filter = ('city', 'attraction_type', 'region', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('view_count', 'like_count', 'created_at', 'updated_at')
    inlines = [AttractionImageInline]
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'region', 'city', 'attraction_type', 'description')
        }),
        ('价格与时间', {
            'fields': ('price', 'opening_hours')
        }),
        ('图片与地图', {
            'fields': ('image', 'map_image')
        }),
        ('统计数据', {
            'fields': ('view_count', 'like_count', 'created_at', 'updated_at')
        }),
    )


@admin.register(AttractionImage)
class AttractionImageAdmin(admin.ModelAdmin):
    list_display = ('attraction', 'order', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('attraction__name',)


@admin.register(AttractionLike)
class AttractionLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'attraction', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'attraction__name')