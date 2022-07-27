from django.test import TestCase
from eshop_products.models import Product
from .models import details,Favorite_list
from django.contrib.auth.models import User

class favlist_Test(TestCase):
    def setUp(self):
        user = User.objects.create(username="Test",password="TEST",email="test@test.com")
        product = Product.objects.create(title="test",description="test",price=1000,active=True)
        fav_list = Favorite_list.objects.create(user_id=user.id)
        detail = details.objects.create(favorite_list_id=fav_list.id,product_id=product.id,)
    def test_fav_model(self):
        user = User.objects.get(username="Test")
        favlist = Favorite_list.objects.get(user_id=user.id)
        self.assertEqual(favlist.user_id,user.id)
        self.assertEqual(favlist.details_set.first().product.title,"test")