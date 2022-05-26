from django.shortcuts import render, redirect

from eshop_products.forms import CommentForm
from eshop_products.models import Product
from .models import CommentModel


def comment_add(request):
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        p_id = comment_form.cleaned_data.get('product_id')
        product = Product.objects.filter(id=p_id).first()
        text = comment_form.cleaned_data.get('text')
        comment = CommentModel.objects.create(text=text,product_id=p_id,person_id=comment_form.cleaned_data.get('person_id'))
        comment.save()
    return redirect(f'products/{product.id}/{product.slug}')
