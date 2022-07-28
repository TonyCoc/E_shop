from django.test import TestCase
from .models import Product

class product_Test(TestCase):

    def setUp(self):
        product = Product.objects.create(title="testProduct_modl",description="test",price=1000,active=True)
    def test_model(self):
        product = Product.objects.get(title="testProduct_modl")
        self.assertEqual(product.title,"testProduct_modl")