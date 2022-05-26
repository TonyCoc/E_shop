from django.shortcuts import render
from eshop_products.models import Product
from eshop_tag.models import Tag
from django.core.paginator import Paginator
from django.shortcuts import Http404
from django.views.generic import ListView


class search(ListView):
    template_name = 'search_list/search_list.html'
    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        print(Product.objects.search(query))
        return Product.objects.search(query)

