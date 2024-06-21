from django.contrib import admin

from .models import Expense


@admin.register(Expense)
class Expense(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['title']
