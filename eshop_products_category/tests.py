from django.test import TestCase
from eshop_products.models import Product
from .models import category


# Create your tests here.
class categoryTest(TestCase):
    def setUp(self):
        Category = category.objects.create(title="TestCategory",name="TestName",active=True)
        product = Product.objects.create(title="testProduct_model",description="test",price=1000,active=True)
        Category.product_set.add(product)

    def test_category(self):
        product = Product.objects.get(title="testProduct_model")
        Category = category.objects.create(title="TestCategory", name="TestName", active=True)
        self.assertEqual(product.categories.first().name,"TestName")


