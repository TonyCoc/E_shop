from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render,redirect
from django.views.generic import ListView
from eshop_products.models import Product
@staff_member_required
def admin_home(request):

    return render(request, "admin_panel/Home/admin_home.html")


@staff_member_required
def user_list(request):
    context = {
        "nav_type" : "user_list",
        "object_list": None
    }
    q = request.GET.get('users-search')
    try:
        if q is None:
            context["object_list"] = User.objects.all()
        else:
            qs = User.objects.filter(Q(username__contains=q) | Q(username__icontains=q) | Q(username__exact=q))
            context["object_list"] = qs
    except:
        pass
    return render(request, "admin_panel/Users/User_lists.html" ,context)
@staff_member_required
def product_list(request):
    context = {
        "object_list" : None,
        "nav_type" : "product_list"
    }
    q = request.GET.get('products-search')
    qs = Product.objects.all()
    try:
       if q is None:
            context["object_list"] = qs
       else:
           qs = Product.objects.filter(Q(title__icontains=q) | Q(title__icontains=q) | Q(description__icontains=q) )
           context["object_list"] = qs
    except:
        pass
    return render(request,"admin_panel/Products/product_list.html",context)
@staff_member_required
def user_edit(request,pk):
    user = User.objects.filter(id=pk).first()
    context ={
        "user" : user
    }

    if request.method == "POST":
        form_data = {
            'is_baned': None
        }
        if request.POST.get('is_baned') == "on":
            form_data["is_baned"] = True
        else:
            form_data["is_baned"] = False
        if user.reset_password.is_baned == form_data["is_baned"]:
            pass
        else :

            user.reset_password.is_baned = form_data["is_baned"]
            user.reset_password.save()
    return render(request,"admin_panel/Users/user_edit.html",context)


@staff_member_required
def product_edit(request,pk):
    product = Product.objects.filter(id=pk).first()

    context = {
        "obj" : product
    }
    if request.method == "POST":
        title = request.POST.get("title")
        Description = request.POST.get("description")
        try:
            img = request.FILES['img']
            product.image = img
        except:
            pass
        price = request.POST.get("price")
        is_free = request.POST.get("is_Free")
        is_active = request.POST.get("is_active")
        if is_free == "on":
            is_free = True
        else:
            is_free = False
        if is_active == "on":
            is_active = True
        else:
            is_active = False


        if title != product.title:
            product.title = title
        if Description != product.description:
            product.description = Description
        if price != product.price:
            product.price = price
        if is_free != product.free:
            product.free = is_free
        if is_active != product.active:
            product.active = is_active
        product.save()



    return render(request,"admin_panel/Products/product_edit.html",context)





#partials

def _sidebar_partial(request):
    return render(request, "admin_panel/partials/_sidebar.html")