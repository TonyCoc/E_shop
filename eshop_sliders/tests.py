from django.test import TestCase
from eshop_products.models import Product
from .models import Slider

class sliderTest(TestCase):

    def setUp(self):
        product = Product.objects.create(title="testProduct_model", description="test", price=1000, active=True)
        slider = Slider.objects.create(product_id=product.id)

    def test_slider(self):
        product = Product.objects.get(title="testProduct_model")
        self.assertEqual(product.slider.product.title,"testProduct_model")