from django.urls import path, include
from .views import membership
urlpatterns = [
    path('Membership/',membership)
]