from django.urls import path

from .views import *

urlpatterns = [
    path('comment_add', comment_add)
]
