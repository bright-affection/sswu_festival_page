from django.contrib import admin
from .models import Info

class Info(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'image', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']