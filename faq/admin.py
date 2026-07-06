from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "order")
    ordering = ("order",)
    search_fields = ("question",)