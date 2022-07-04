from django.urls import include,path
from .views import *
urlpatterns = [
    path('admin-panel',admin_home),
    path('admin-panel/users-list',user_list.as_view())
]