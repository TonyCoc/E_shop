from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render,redirect
from django.views.generic import ListView
from eshop_products.models import Product

def admin_home(request):
    return render(request, "admin_panel/Home/admin_home.html")

class user_list(ListView):
    template_name = "admin_panel/Users/User_lists.html"
    model = User
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["nav_type"] = "user_list"
        return context
    def get_queryset(self):
        q = self.request.GET.get('users-search')
        qs = super().get_queryset()
        try:
            if q is None:
                return qs
            else:
                qs = User.objects.filter(Q(username__contains=q) | Q(username__icontains=q) | Q(username__exact=q) )
                return qs
        except:
            pass
class product_list(ListView):
    template_name = "admin_panel/Products/product_list.html"
    model = Product
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["nav_type"] = "product_list"
        return context
    def get_queryset(self):
        q = self.request.GET.get('products-search')
        qs = super().get_queryset()
        try:
           if q is None:
                return qs
           else:
               qs = Product.objects.filter(Q(title__icontains=q) | Q(title__icontains=q) | Q(description__icontains=q))
               return qs
        except:
            pass

def user_edit(request,pk):
    user = User.objects.filter(id=pk).first()
    context ={
        "user" : user
    }
    if request.method == "POST":
        request.get()
    return render(request,"admin_panel/Users/user_edit.html",context)













#partials

def _sidebar_partial(request):
    return render(request, "admin_panel/partials/_sidebar.html")