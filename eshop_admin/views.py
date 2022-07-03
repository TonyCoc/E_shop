from django.shortcuts import render,redirect



def admin_home(request):
    return render(request, "admin_panel/Home/admin_home.html")

def _sidebar_partial(request):
    return render(request, "admin_panel/partials/_sidebar.html")