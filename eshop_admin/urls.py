from django.urls import include,path
from .views import *
urlpatterns = [
    path('admin-panel',admin_home)
]