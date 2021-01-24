from django.contrib import admin

from .models import Grocerylist, PantryItem, Category, AmountType
# Register your models here.
admin.site.register(Grocerylist)
admin.site.register(PantryItem)
admin.site.register(Category)
admin.site.register(AmountType)