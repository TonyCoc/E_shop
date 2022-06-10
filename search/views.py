from django.shortcuts import render
from eshop_products.models import Product
from eshop_tag.models import Tag
from django.core.paginator import Paginator
from django.shortcuts import Http404
from django.views.generic import ListView


class search(ListView):
    template_name = 'search_list/search_list.html'
    def get_queryset(self):
        products = None
        request = self.request
        query = request.GET.get('q')
        try:
            query_2 = request.GET.get('price')
            if query_2 is not None:
                splited = query_2.split(',')
                min = int(splited[0])
                max = int(splited[1])
                products = Product.objects.search_and_price(query,min_price=min,max_price=max)

            else:
                products = Product.objects.search(query)
        except:
            pass

        return products

