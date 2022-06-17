from http import server
import itertools
from django.http import JsonResponse

from django.shortcuts import render, Http404
from django.core.paginator import Paginator
from eshop_comment.models import CommentModel
from eshop_favlist.forms import Fave_list_form
from eshop_order.forms import order_form
from .forms import image_input, CommentForm
from .models import *
from eshop_favlist.models import Favorite_list
from eshop_tag.models import Tag
from eshop_products_category.models import category
from e_shop.utils import my_grouper, price_show
from .serializer import Product_serializer

def products(request):
    query = None
    splited = None
    try:
        query = request.GET.get('price')
        splited = query.split(',')
        min = int(splited[0])
        max = int(splited[1])
        Products = Product.objects.filter(active=True, price__range=(min, max))
    except:
        Products = Product.objects.active_check()
    for item in Products:
        item.price = price_show(item.price)
    paginaitor = Paginator(Products, 4)
    page_number = request.GET.get('page')
    page_obj = paginaitor.get_page(page_number)

    try:
        if int(page_number) > page_obj.number:
            raise Http404('صفحه مورد نظر یافت نشد')
    except:
        pass

    context = {
        'obj': Products,
        'page_obj': page_obj,
    }

    return render(request, 'shop_list.html', context)


def product_detail(request, slug=None, p_id=None):
    product = Product.objects.get_by_slug_id(slug, p_id)
    comments_count = product.commentmodel_set.count()
    comments = CommentModel.objects.filter(product_id=product.id)
    comment_form = CommentForm(request.POST or None, initial={'product_id': product.id, 'person_id': request.user.id})
    try:
        order_Form = order_form(request.POST or None, initial={'product_id': product.id})
    except:
        return render(request, '404.html')
    try:
        fav_Form = Fave_list_form(request.POST or None, initial={'product_id': product.id})
    except:
        return render(request, '404.html')
    product_category_title = product.categories.first()
    galleries = Product_gallery.objects.filter(product_id=p_id)
    related_category = category.objects.filter(title=product_category_title)
    related_products = related_category.first().product_set.all().distinct()
    grouped_related_products = list(my_grouper(3, related_products))
    grouped_galleries = list(my_grouper(3, galleries))
    try:
        user_list = Favorite_list.objects.filter(user_id=request.user.id).first()
    except:
        pass
    if product is None:
        return render(request, '404.html')
    product.views += 1
    product.save()
    product.price = price_show(product.price)
    item_in_fave_list = None
    try:
        check_list = []
        for item in user_list.details_set.all():
            check_list.append(item.product)
        if product in check_list:
            item_in_fave_list = True
    except:
        pass
    context = {
        'obj': product,
        'galleries': grouped_galleries,
        'rel_products': grouped_related_products,
        "form": order_Form,
        "add_fav_form": fav_Form,
        "is_in_list": item_in_fave_list,
        'comments': comments,
        'comment_form': comment_form,
        'comments_count': comments_count
    }
    return render(request, 'product-details.html', context)


def product_by_category(request, category_slug=None):
    products = Product.objects.active_check()
    products = products.filter(categories__name__exact=category_slug)
    if products.filter(categories__active=False):
        return render(request, '404.html')
    for item in products:
        item.price = price_show(item.price)
    paginaitor = Paginator(products, 10)

    page_number = request.GET.get('page')
    page_obj = paginaitor.get_page(page_number)

    try:
        if int(page_number) > page_obj.number:
            return render(request, '404.html')
    except:
        pass

    if products.count() == 0:
        return render(request, '404.html')

    context = {
        'obj': products,
        'page_obj': page_obj,
        'category': category.objects.all()
    }
    return render(request, 'shop_list.html', context)


def category_partial(request):
    categories = category.objects.all()
    context = {
        "category": categories
    }
    return render(request, 'partial/category_partial.html', context)


def edit_product(request):
    product = Product.objects.get(id=4)
    Form = image_input()
    context = {
        'form': Form
    }
    if request.method == "POST":
        image = request.FILES['image']
        product.image = image
        product.save()
    return render(request, 'edit.html', context)

def product_api(request):
    products = Product.objects.all()
    serializer = Product_serializer(products,many=True)
    return JsonResponse(serializer.data,safe=False)