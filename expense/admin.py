from django.contrib import admin

# Register your models here.
from .models import Category, ExpensesList, Transaction, Account
admin.site.register(Category)
admin.site.register(ExpensesList)
admin.site.register(Transaction)
admin.site.register(Account)