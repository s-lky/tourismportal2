from django.contrib import admin
from .models import TripPlan

@admin.register(TripPlan)
class TripPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'days', 'created_at')
    list_filter = ('created_at', 'days')
    search_fields = ('title', 'content', 'user__username')
    date_hierarchy = 'created_at'
