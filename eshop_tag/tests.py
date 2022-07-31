from django.test import TestCase
from eshop_products.models import Product
from .models import Tag


class tagTest(TestCase):

    def setUp(self):
        tag = Tag.objects.create(title="test_tag")
        product = product = Product.objects.create(title="testProduct_modl",description="test",price=1000,active=True)
        product.tag_set.add(tag)
    def test_tag(self):
        product = Product.objects.get(title="testProduct_modl")
        self.assertEqual(product.tag_set.first().title ,"test_tag")
