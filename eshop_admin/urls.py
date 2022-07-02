from django.urls import include,path
from .views import *
urlpatterns = [
    path('admin_home',admin_home)
]