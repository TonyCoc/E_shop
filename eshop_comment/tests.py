from django.contrib.auth.models import User
from django.test import TestCase
from .models import CommentModel
from eshop_products.models import Product

class comment_Test(TestCase):
    def setUp(self):
        product = Product.objects.create(title="test",description="test",price=1000,active=True)
        person = User.objects.create(username="Test",password="test",email="test@test.com")
        person = User.objects.get(username="Test")
        product = Product.objects.get(title="test")
        comment = CommentModel.objects.create(person_id=person.id,product=product,text="test",)
    def test_comment_model(self):
        product = Product.objects.get(title="test")
        comment = product.commentmodel_set.first()
        self.assertEqual(comment.text ,"test")