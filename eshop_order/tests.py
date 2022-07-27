from django.test import TestCase
from .models import order,order_detail
from django.contrib.auth.models import User
from eshop_products.models import Product


class order_Test(TestCase):

    def setUp(self):
        user = User.objects.create(username="TestUser", password="TEST", email="test@test.com")
        product = Product.objects.create(title="testProduct", description="test", price=1000, active=True)
        Order = order.objects.create(owner_id=user.id)
        detail = order_detail.objects.create(order_id=Order.id,product_id=product.id,price=200000,count=3)
    def test_order_model(self):
        user = User.objects.get(username="TestUser")
        product = Product.objects.get(title="testProduct")
        Order = order.objects.get(owner_id=user.id)
        self.assertEqual(Order.order_detail_set.first().product.title,product.title)
