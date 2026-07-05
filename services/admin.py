from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'starting_price',
        'delivery_time',
        'is_active',
    )

    list_filter = ('is_active',)

    search_fields = ('title',)

    ordering = ('title',)