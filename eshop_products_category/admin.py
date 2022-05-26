from django.contrib import admin

# Register your models here.
from eshop_products_category.models import category


class categoty_product(admin.ModelAdmin):
    list_display = ['title', 'active']

    class Meta:
        model = category


admin.site.register(category, categoty_product)
