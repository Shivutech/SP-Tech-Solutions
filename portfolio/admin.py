from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'created_at',
    )

    list_filter = (
        'category',
        'created_at',
    )

    search_fields = (
        'title',
        'category',
    )

    ordering = ('-created_at',)