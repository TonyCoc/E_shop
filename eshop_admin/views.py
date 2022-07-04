from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import ListView


def admin_home(request):
    return render(request, "admin_panel/Home/admin_home.html")

class user_list(ListView):
    template_name = "admin_panel/Users/User_lists.html"
    model = User


def _sidebar_partial(request):
    return render(request, "admin_panel/partials/_sidebar.html")