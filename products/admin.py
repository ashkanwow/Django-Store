from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'entity','submit_time', 'price', 'is_published')

admin.site.register(Product, ProductAdmin)

