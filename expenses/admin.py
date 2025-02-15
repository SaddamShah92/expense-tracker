from django.contrib import admin
from .models import Expenses

# Register your models here.

@admin.register(Expenses)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'date', 'description')
    list_filter = ('category', 'date')
    search_fields = ('category', 'description')
