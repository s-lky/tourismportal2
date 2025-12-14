from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'attraction', 'visit_date', 'quantity', 'status', 'created_at')
    list_filter = ('status', 'visit_date', 'created_at')
    search_fields = ('user__username', 'attraction__name')
    date_hierarchy = 'created_at'
