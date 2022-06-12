from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import Fave_list_form
from django.contrib.auth.models import User
from .models import *

@login_required(login_url="/login")
def favorite_list_show(request):
    fav_list = Favorite_list.objects.filter(user_id=request.user.id).first()
    item_list = []
    context = {
        'list': None,
        'error':None
    }
    if fav_list == None:
        context['error'] = "have_no_list"
    else:
        for item in fav_list.details_set.all():
            item_list.append(item.product)
        context['list'] = item_list
    return render(request,"favorite_list.html",context)
@login_required(login_url="/login")
def add_product_to_list(request):
    fave_list = Fave_list_form(request.POST or None)
    if fave_list.is_valid():
        List = Favorite_list.objects.filter(user_id=request.user.id).first()
        if List is None:
            List = Favorite_list.objects.create(user_id=request.user.id)
        product = Product.objects.get(id=fave_list.cleaned_data.get("product_id"))
        check_list = []
        for item in List.details_set.all():
            check_list.append(item.product)
        if product not in check_list:
            List.details_set.create(product=product)
        else:
            return redirect(f'products/{product.id}/{product.slug}')
    return redirect('/')
def delete_from_list(request , *args ,**kwargs):
    item_detail = kwargs.get('product_id')
    product = Product.objects.filter(id=item_detail).first()
    list = Favorite_list.objects.filter(user_id=request.user.id).first()
    list.details_set.filter(product_id=product.id).first().delete()
    return redirect('/favorite_list')
