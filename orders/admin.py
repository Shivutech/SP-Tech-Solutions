from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'service',
        'email',
        'phone',
        'status',
        'created_at',
        'project_file',
        
    )

    list_filter = ('service', 'created_at')

    search_fields = (
        'name',
        'email',
        'phone',
    )

    ordering = ('-created_at',)
