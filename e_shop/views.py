from eshop_products_category.models import category
from eshop_sliders.models import Slider
from django.shortcuts import render, redirect
from eshop_settings.models import Settings
from eshop_products.models import Product
from e_shop.utils import my_grouper,price_show


def home(request):
    sliders = Slider.objects.all()
    catrgories = category.objects.all()[:9]
    product_by_view = Product.objects.order_by('-views')[:8]
    for item in product_by_view :
        item.price = price_show(item.price)
    product_by_last = Product.objects.order_by("-id")[:8]
    for item in product_by_last:
        item.price = price_show(item.price)
    context = {
        'sliders': sliders,
        'by_view': my_grouper(4, product_by_view),
        'by_last': my_grouper(4,product_by_last),
        'category': catrgories
    }
    return render(request, 'home_page.html', context)


def header(request):
    context = {
        "user": request.user.id
    }
    return render(request, 'shared/Header.html', context)


def footer(request):
    context = {
        'about_us': 'به اولین وبسایت من(کیان بهجتی) خوش اومدین ، این وبسایت هیچ محصولی به فروش نمی رساند فقط برای رزومه نوشته شده است :)'
    }
    return render(request, 'shared/Footer.html', context)


def about_us(request):
    about_Us = Settings.objects.first()
    context = {
        'about_us': about_Us
    }
    return render(request, 'about_us.html', context)

