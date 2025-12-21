from django.contrib import admin
from .models import TripPlan, TripPlanImage

class TripPlanImageInline(admin.TabularInline):
    model = TripPlanImage
    extra = 1
    fields = ('image', 'order')

@admin.register(TripPlan)
class TripPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'days', 'created_at')
    list_filter = ('created_at', 'days')
    search_fields = ('title', 'content', 'user__username')
    date_hierarchy = 'created_at'
    inlines = [TripPlanImageInline]

@admin.register(TripPlanImage)
class TripPlanImageAdmin(admin.ModelAdmin):
    list_display = ('trip_plan', 'order', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('trip_plan__title',)
