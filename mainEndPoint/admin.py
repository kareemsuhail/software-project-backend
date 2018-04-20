from django.contrib import admin
from .models import Category,Budget,Expense

# Register your models here.
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['name','owner','start_date','end_date','balance','amount']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','budget','balance','amount']
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['label','category','amount','date']

