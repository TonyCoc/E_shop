from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_form),
    path('register/', register_form),
    path('logout/', log_out),
    path('user-panel',user_panel),
    path('user-edit',user_edit),
    path('reset-password',reset_password)
]
