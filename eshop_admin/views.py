from django.shortcuts import render,redirect



def admin_home(request):
    return render(request, "admin_panel/partials/blank-page.html")

def _sidebar_partial(request):
    return render(request, "admin_panel/partials/_sidebar.html")