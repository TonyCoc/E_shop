from .views import *
from django.urls import path

urlpatterns = [
    path('products/search/', search.as_view())

]
