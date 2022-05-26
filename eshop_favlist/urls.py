from django.urls import path
from .views import *

urlpatterns = [
    path('favorite_list', favorite_list_show),
    path('add_product_favorite', add_product_to_list),
    path('delete_item_favorite/<product_id>',delete_from_list)
]
