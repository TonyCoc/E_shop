from django.test import TestCase
from .models import Product

class product_Test(TestCase):

    def setUp(self):
        product = Product.objects.create(title="testProduct_modl",description="test",price=1000,active=True,image="./assets/images/cart/two.png")
    def test_model(self):
        product = Product.objects.get(title="testProduct_modl")
        self.assertEqual(product.title,"testProduct_modl")
    def test_url(self):
        product = Product.objects.get(title="testProduct_modl")
        print(product.title)
        response = self.client.get('/products/'+str(product.id)+"/"+product.slug)
        self.assertEqual(response.status_code,200)