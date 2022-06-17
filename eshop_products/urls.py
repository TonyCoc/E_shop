from django.urls import path
from .views import *

urlpatterns = [
    path('products/', products),
    path('products/<p_id>/<slug>', product_detail),
    path('products/categories-<category_slug>/', product_by_category),
    path('products_api_get',product_api)
    # path('edit-product/',edit_product),
    # path('partial_category_load',category_partial,name='category_partial'),
]
