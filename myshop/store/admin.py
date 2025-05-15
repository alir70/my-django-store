from django.contrib import admin

# Register your models here.

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'price', 'created_at',)  # Add 'created_at' here

admin.site.register(Product, ProductAdmin)
