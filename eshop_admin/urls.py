from django.urls import include,path
from .views import *
urlpatterns = [
    path('admin-panel',admin_home),
    path('admin-panel/users',user_list.as_view()),
    path("admin-panel/products",product_list.as_view()),
    path('admin-panel/users/<pk>',user_edit)
]