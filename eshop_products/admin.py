from django.contrib import admin

from .models import *


# Register your models here.


class Product_pre_view(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']

    class Meta:
        model = Product


admin.site.register(Product, Product_pre_view)
admin.site.register(Product_gallery)